import base64
import cloudinary.uploader
import json
import logging
import os
import requests
import time

from requests.exceptions import ConnectionError, Timeout
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def upload_to_image_hosting_service(screenshot_data):
    cloudinary.config(
        cloud_name="your_user_name",
        api_key="your_api_key",
        api_secret="your_api_secret"
    )   # 输入Cloudinary的信息
    result = cloudinary.uploader.upload(screenshot_data)
    return result.get('secure_url')
def setup_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)
def take_screenshot(driver, url):
    try:
        driver.get(url)
        WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')
        # Scroll to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)  # Wait for any animations to complete
        result = driver.execute_cdp_cmd('Page.captureScreenshot', {'format': 'png', 'fromSurface': True})
        return base64.b64decode(result['data'])
    except Exception as e:
        logging.error(f"Error taking screenshot for URL {url}: {str(e)}")
    return None
def upload_to_notion_direct(screenshot_data, page_id, notion_api_key, retries=3, backoff_factor=2):
    headers = {
        "Authorization": f"Bearer {notion_api_key}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    # Upload the screenshot to Cloudinary and get the URL
    screenshot_url = upload_to_image_hosting_service(screenshot_data)
    data = {
        "properties": {
            "file": {
                "files": [{"name": "Screenshot", "type": "external", "external": {"url": screenshot_url}}]
            }
        }
    }
    for attempt in range(1, retries + 1):
        try:
            update_url = f"https://api.notion.com/v1/pages/{page_id}"
            response = requests.patch(update_url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                logging.info(f"Successfully uploaded screenshot to Notion page {page_id}")
                return True
            else:
                logging.error(f"Failed to upload screenshot to Notion page {page_id}: {response.status_code} - {response.text}")
        except ConnectionError as e:
            logging.warning(f"Connection error during attempt {attempt}/{retries}: {str(e)}")
            if attempt == retries:
                raise  # Re-raise the error after all retries are exhausted
        # Exponential backoff
        time.sleep(backoff_factor ** attempt)
    return False  # If all retries fail
def get_database_pages(database_id, notion_api_key, start_cursor=None):
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    headers = {
        "Authorization": f"Bearer {notion_api_key}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    body = {}
    if start_cursor:
        body["start_cursor"] = start_cursor
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        data = response.json()
        return data['results'], data.get('next_cursor'), data.get('has_more')
    else:
        logging.error(f"Failed to get database pages: {response.status_code}")
        return [], None, False
def load_processed_urls(file_path="processed_urls.json"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return set(json.load(f))
    return set()
def save_processed_urls(processed_urls, file_path="processed_urls.json"):
    with open(file_path, 'w') as f:
        json.dump(list(processed_urls), f)
def main():
    notion_api_key = "your_notion_api_key_here"
    database_id = "your_database_id_here"
    max_screenshots = 50
    screenshots_taken = 0
    start_cursor = None
    processed_urls = load_processed_urls()
    driver = setup_chrome_driver()
    try:
        while screenshots_taken < max_screenshots:
            pages, next_cursor, has_more = get_database_pages(database_id, notion_api_key, start_cursor)

            for page in pages:
                if screenshots_taken >= max_screenshots:
                    break

                file_property = page['properties'].get('file', {})
                url_property = page['properties'].get('url', {})

                if file_property.get('type') == 'files' and url_property.get('type') == 'url':
                    url = url_property.get('url')
                    if url and url not in processed_urls:
                        logging.info(f"Processing URL: {url}")
                        screenshot_data = take_screenshot(driver, url)
                        if screenshot_data:
                            if upload_to_notion_direct(screenshot_data, page['id'], notion_api_key):
                                screenshots_taken += 1
                                processed_urls.add(url)
                                save_processed_urls(processed_urls)
                            else:
                                logging.error(f"Failed to add screenshot to Notion page for {url}")
                        else:
                            logging.warning(f"Failed to take screenshot for {url}, skipping...")
                    elif url in processed_urls:
                        logging.info(f"URL {url} already processed, skipping...")
                    else:
                        logging.warning("URL property is empty")
                else:
                    logging.warning("File or URL property not found or not of correct type")

                time.sleep(2)  # Add a small delay between requests

            if not has_more or not next_cursor:
                break

            start_cursor = next_cursor

        logging.info(f"Total screenshots taken: {screenshots_taken}")
    finally:
        driver.quit()
if __name__ == "__main__":
    main()
