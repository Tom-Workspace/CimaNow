from selenium.webdriver.common.by import By
from typing import List
from bs4 import BeautifulSoup
import apiv2


class GetPagesLinks:

    def get_page_links(client: "apiv2.Client") -> List[str]:
        """Retrieve all page links from pagination"""
        page_links = []
        try:
            current_link = client.current_url
            pagination = client.find_element(
                By.CSS_SELECTOR, "ul[aria-label='pagination']"
            )
            soup = BeautifulSoup(pagination.get_attribute("outerHTML"), "lxml")
            links = soup.select("li > a[href]")
            if links == []:
                page_links.append(current_link)
            for link in links:
                page_links.append(link["href"])

        except Exception as e:
            print(f"error while fetching pagination links: {e}")

        return page_links
