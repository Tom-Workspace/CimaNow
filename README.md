# CimaNow Web Scraping Tool

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Selenium](https://img.shields.io/badge/Selenium-3.x-brightgreen.svg) ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-yellow.svg)

A powerful Python tool for scraping movies and series information from [CimaNow](https://bs.cimanow.cc/), utilizing Selenium and BeautifulSoup for robust data extraction.

## Features

- **Search for Movies and Series**: Retrieve search results based on your query.
- **Get Seasons and Episodes**: Extract season and episode details for series.
- **Fetch Streaming Links**: Get all available streaming options for episodes.
- **Download Links**: Retrieve quality-specific download links for episodes.
- **Robust Handling**: Supports pagination and various media types (`movies`, `series`, `all`).

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Tom-Workspace/CimaNow.git

   
## Usage

1. **Search for Movies**
   
  
      ```python
      from apiv2 import Client

      client = Client(False)
      search_name = "ghosted"
      search_results = search(search_name)
      print(search_results)

      
2. **Search for Series**
   
  
      ```python
      from apiv2 import Client

      client = Client(False)
      search_name = "ghosted"
      search_results = search(search_name)
      print(search_results)

      
3. **Get Series Seasons**
   
  
      ```python
      series_url = "https://bs.cimanow.cc/selary/"
      seasons = get_series_season(series_url)
      print(seasons)


      
4. **Get Series Episodes**
   
  
      ```python
      season_url = "https://bs.cimanow.cc/selary/"
      episodes = get_series_episode(season_url)
      print(episodes)


      
5. **Get iFrame Links**
   
  
      ```python
      episode_url = "https://bs.cimanow.cc/watching/"
      iframe_links = get_iframe_links(episode_url)
      print(iframe_links)

      
6. **Get Download Links**
   
  
      ```python
      download_links = get_download_links(episode_url)
      print(download_links)

<br/>
<br/>
<br/>


## Contributing

***Contributions are welcome! Please follow these steps:***

1. **Fork the project.**
2. **Create a new branch (git checkout -b feature/YourFeature).**
3. **Commit your changes (git commit -m 'Add a new feature').**
4. **Push to the branch (git push origin feature/YourFeature).**
5. **Open a pull request.**




## License

- **This project is licensed under the MIT License. See the LICENSE file for details.**




## Disclaimer

- **This tool is for educational purposes only.<br/>Scraping websites without permission may violate the terms of service of the site. Use responsibly.**


<br/>

## Contact


- **Created by ِ[Ahmed](https://t.me/BE_PY) - feel free to contact me!**


<br/>
<br/>
<br/>

