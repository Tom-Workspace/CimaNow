from selenium.webdriver.common.by import By
from typing import List, Dict
from bs4 import BeautifulSoup
import apiv2
from urllib.parse import quote, unquote


class ScrapePage:
    def scrape_page(
        client: "apiv2.Client", movie_type: str = "all"
    ) -> List[Dict[str, str]]:
        """Scrape data from the current page"""
        posts_list = []
        try:
            posts = client.find_elements(By.CSS_SELECTOR, "article[aria-label='post']")
            item_id = 1
            for posti in posts:
                try:
                    html = posti.get_attribute("outerHTML")
                    soup = BeautifulSoup(html, "lxml")

                    quality_elements = soup.select("li[aria-label='ribbon']")
                    quality = (
                        list(set(el.get_text() for el in quality_elements))
                        if quality_elements
                        else ["Unknown Quality"]
                    )

                    title_element = soup.select_one("li[aria-label='title']")
                    if title_element and title_element.em:
                        title_element.em.decompose()
                    title = (
                        title_element.get_text(strip=True)
                        if title_element
                        else "No Title"
                    )

                    item_link_element = soup.select_one("a")
                    item_link = item_link_element["href"] if item_link_element else None
                    if not item_link:
                        print("No item link found, skipping this post")
                        continue
                    keyword = quote("مسلسل")

                    if movie_type == "movie" and (
                        item_link.startswith("https://bs.cimanow.cc/selary/")
                        or keyword.lower() in item_link.lower()
                    ):
                        continue

                    year_element = soup.select_one("li[aria-label='year']")
                    year = (
                        year_element.get_text(strip=True)
                        if year_element
                        else "Unknown Year"
                    )

                    item = {
                        "id": item_id,
                        "item_link": unquote(item_link),
                        "quality": quality,
                        "year": year,
                        "title": title,
                    }
                    posts_list.append(item)
                    item_id += 1

                except Exception as e:
                    print(f"Error while processing a post (ID: {item_id}): {e}")

        except Exception as e:
            print(f"Error while scraping the current page: {e}")

        return posts_list
