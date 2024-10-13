from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from typing import List
import apiv2


class GetSeriesSeasons:
    def get_series_seasons(client: "apiv2.Client", url: str) -> List[dict]:
        try:
            client.get(url)
            client.wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            section = client.find_element(
                By.CSS_SELECTOR, "section[aria-label='seasons']"
            )
            soup = BeautifulSoup(section.get_attribute("outerHTML"), "lxml")

            return [
                {
                    "title": item.select_one("a").text,
                    "url": item.select_one("a").get("href"),
                }
                for item in soup.select("ul > li")
            ]
        except Exception as e:
            print(f"error: {e}")
            return []
