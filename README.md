<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion">
    <img src="images/logo.png" >
  </a>

<h1 align="center">Chrome Screenshot to Notion</h1>

  <p align="center">
    This script automatically takes screenshots of web pages and uploads them to a specific Notion database page. It works with Notion's API and uses Selenium for web crawling and Cloudinary for external image serving.
    <br />
    <a href="https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://kinpoeray.notion.site/AIGC-Bookmarks-5202cde5c291464eaf61092f824f67ec">View Demo</a>
    ·
    <a href="https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#configuration">Configuration</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#logging">Logging</Ca></li>
    <li><a href="#error-handling">Error Handling</Ca></li>
    <li><a href="#limitations">Limitations</Ca></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<h3 align="center">AIGC bookmarks</h3>

<img src="https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2f9bfe61-f42f-4e15-8046-c3d5a6bb62f8%2Fe3e2775a-24d6-4452-af4b-77fbd2c539a2%2F20240815-114-chrome.png?table=block&id=65736ee2-5d36-4138-a117-79c0638a08f4&spaceId=2f9bfe61-f42f-4e15-8046-c3d5a6bb62f8&width=2000&userId=a3e4f707-2b9b-4cd7-87c9-6fa39cb89a52&cache=v2"/>

<h3 align="center">Favorite Tools</h3>

<img src="https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2f9bfe61-f42f-4e15-8046-c3d5a6bb62f8%2Ffb3a84f1-e59e-4f99-a7dd-671df9c8bd99%2F20240815-117-chrome.png?table=block&id=3fa461d4-135a-4f4d-82d2-c27bde918795&spaceId=2f9bfe61-f42f-4e15-8046-c3d5a6bb62f8&width=2000&userId=a3e4f707-2b9b-4cd7-87c9-6fa39cb89a52&cache=v2"/>

### Built With

This project utilizes several key Python libraries and frameworks:

`Selenium`: Used for web scraping and taking screenshots of web pages.

`Cloudinary`: Provides cloud-based image hosting services.

`Requests`: Used for making HTTP requests to the Notion API.

`webdriver_manager`: Simplifies the management of ChromeDriver for Selenium.

`json`: Used for parsing and creating JSON data.

`logging`: Provides a flexible framework for generating log messages.

`base64`: Used for encoding and decoding the screenshot data.

`time`: Used for adding delays and handling timeouts.

#### _All coding driven by AI. ( `Claude` , `ChatGPT` , `Mistral` )_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FEATURES -->
## Features

- Fetches pages from a specified Notion database
- Takes screenshots of URLs found in the database pages
- Uploads screenshots to Cloudinary
- Updates Notion pages with the screenshot URLs
- Implements retry logic and error handling
- Tracks processed URLs to avoid duplicates


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

- Python 3.7+
- Chrome browser
- Notion API key
- Cloudinary account

### Installation


1. Clone this repository:
   ```
   git clone https://github.com/kinpoe-ray/chrome-screenshot-to-notion
   cd chrome-screenshot-to-notion
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Install ChromeDriver (if not already installed):
   ```
   pip install webdriver_manager
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONFIGURATION STEPS -->
## Configuration

1. Open the script and update the following variables:
   - `notion_api_key`: Your Notion API key
   - `database_id`: The ID of your Notion database
   - Cloudinary configuration in the `upload_to_image_hosting_service` function
     - `cloud_name`: Your user name 
     - `api_key`: Your API key
     - `api_secret`: Your API secret

2. Adjust the `max_screenshots` variable if needed (default is 50)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Run the script with:

```
python chrome-screenshot-to-notion.py
```

The script will:
1. Fetch pages from the specified Notion database
2. Take screenshots of URLs found in the pages
3. Upload screenshots to Cloudinary
4. Update Notion pages with the screenshot URLs

<video src="https://file.notion.so/f/f/2f9bfe61-f42f-4e15-8046-c3d5a6bb62f8/d0cf6d88-ed8a-458e-82bc-79690d6086d7/%E6%89%B9%E9%87%8F%E5%B0%86%E7%BD%91%E9%A1%B5%E6%88%AA%E5%9B%BE%E8%87%B3Notion%E7%9A%84%E8%84%9A%E6%9C%AC%E6%BC%94%E7%A4%BA.mp4?table=block&id=db284de6-6337-4d97-a27e-8d166a84a737&spaceId=2f9bfe61-f42f-4e15-8046-c3d5a6bb62f8&expirationTimestamp=1723896000000&signature=p2FNtnyRtGdUaupQ1B47FT9haFL2eDHs3O67_oK6K_w&downloadName=%E6%89%B9%E9%87%8F%E5%B0%86%E7%BD%91%E9%A1%B5%E6%88%AA%E5%9B%BE%E8%87%B3Notion%E7%9A%84%E8%84%9A%E6%9C%AC%E6%BC%94%E7%A4%BA.mp4"/>}

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LOGGING -->
## Logging

The script logs its progress and any errors to the console. You can adjust the logging level in the script if needed.
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- ERROR HANDLING -->
## Error Handling

- The script implements retry logic for API calls
- It uses exponential backoff for failed attempts
- Processed URLs are saved to avoid duplicates even if the script is interrupted
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- LIMITATIONS -->
## Limitations

- The script is set to run headless. Modify Chrome options if you need to see the browser while running
- It's designed to work with specific Notion page properties ('file' and 'url'). Adjust as needed for your database structure
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kinpoe-ray/Chrome-Screenshot-to-Notion" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->
## License

MIT License

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Kinpoe.Ray - [@kinpoe_ray](https://twitter.com/kinpoe_ray) - contact@kinpoeray.store

Project Link: [https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion](https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kinpoe-ray/Chrome-Screenshot-to-Notion.svg?style=for-the-badge
[contributors-url]: https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kinpoe-ray/Chrome-Screenshot-to-Notion.svg?style=for-the-badge
[forks-url]: https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion/network/members
[stars-shield]: https://img.shields.io/github/stars/kinpoe-ray/Chrome-Screenshot-to-Notion.svg?style=for-the-badge
[stars-url]: https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion/stargazers
[issues-shield]: https://img.shields.io/github/issues/kinpoe-ray/Chrome-Screenshot-to-Notion.svg?style=for-the-badge
[issues-url]: https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion/issues
[license-shield]: https://img.shields.io/github/license/kinpoe-ray/Chrome-Screenshot-to-Notion.svg?style=for-the-badge
[license-url]: https://github.com/kinpoe-ray/Chrome-Screenshot-to-Notion/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
