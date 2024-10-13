from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from typing import List, Dict
import apiv2


class GetSeriesEpisodes:
    def get_series_episodes(client: "apiv2.Client", url: str) -> List[Dict]:
        try:
            client.get(url)
            client.wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            section = client.find_element(
                By.CSS_SELECTOR, "section[aria-label='details']"
            )

            soup = BeautifulSoup(section.get_attribute("outerHTML"), "lxml")
            return [
                {
                    "eposide": item.select_one("a em").text,
                    "url": f'{item.select_one("a").get("href")}watching/',
                }
                for item in soup.select("#eps > li")
            ]
        except Exception as e:
            print(f"error: {e}")
            return []
