"""
created by : https://t.me/BE_PY
"""


from typing import Dict, List
from apiv2 import Client
from apiv2.methods import QualityInformation

client = Client(False)

def search(search_name: str, timeout: int = 15, type: str = "movie" # or "all" 
           ) -> List[Dict[str, str]]:
    """
    Retrieve items from a URL and handle pagination if necessary.

    Args:
        client (apiv2.Client): The API client used for making requests.
        url (str): The URL to fetch data from.
        timeout (int, optional): The maximum time to wait for page load. Default is 10 seconds.
        movie_type (str, optional): The type of (movie) to filter links by. Default is "all".

    Returns:
        List[Dict[str, str]]: A list of dictionaries with scraped data.
    """
    url = f"https://bs.cimanow.cc/?s={search_name}"
    search = client.get_item(url, timeout, type)

    return search

# search("ghosted")

def search_series(search_name: str) -> List[Dict[str, str]]:
    url = f"https://bs.cimanow.cc/?s={search_name}"
    search = client.handle_series_links(url)

    return search

# search_series("game")


def get_series_season(series_url: str) -> List[Dict[str, str]]:

    return client.get_series_seasons(series_url)


# print(get_series_season("https://bs.cimanow.cc/selary/مسلسل-squid-game-the-challenge-ج1-مترجم/"))


def get_series_episode(season_url: str) -> List[Dict[str, str]]:

    return client.get_series_episodes(season_url)


# print(get_series_episode("https://bs.cimanow.cc/selary/%d9%85%d8%b3%d9%84%d8%b3%d9%84-squid-game-the-challenge-%d8%ac1-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/"))



def get_iframe_links(episode_url: str) -> List[Dict[str, str]]:

    return client.get_all_iframe_buttons(episode_url)


# print(get_iframe_links("https://bs.cimanow.cc/%d9%85%d8%b3%d9%84%d8%b3%d9%84-squid-game-the-challenge-%d8%a7%d9%84%d8%ad%d9%84%d9%82%d8%a9-5-%d8%a7%d9%84%d8%ae%d8%a7%d9%85%d8%b3%d8%a9-%d9%85%d8%aa%d8%b1%d8%ac%d9%85%d8%a9/watching/"))








def get_download_links(episode_url: str) -> List[Dict[str, str]]:

    return QualityInformation(episode_url)


# print(get_download_links("https://bs.cimanow.cc/%d9%85%d8%b3%d9%84%d8%b3%d9%84-squid-game-the-challenge-%d8%a7%d9%84%d8%ad%d9%84%d9%82%d8%a9-5-%d8%a7%d9%84%d8%ae%d8%a7%d9%85%d8%b3%d8%a9-%d9%85%d8%aa%d8%b1%d8%ac%d9%85%d8%a9/watching/"))








