from typing import List, Dict
import apiv2
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from typing import List, Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException


class GetItem:
    def get_item(
        client: "apiv2.Client", url: str, timeout: int = 5, movie_type: str = "all"
    ) -> List[Dict[str, str]]:
        """
        Retrieve items from a URL and handle pagination if necessary.

        Args:
            client (apiv2.Client): The API client used for making requests.
            url (str): The URL to fetch data from.
            timeout (int, optional): The maximum time to wait for page load. Default is 10 seconds.
            movie_type (str, optional): The type of movie to filter links by. Default is "all".

        Returns:
            List[Dict[str, str]]: A list of dictionaries with scraped data.
        """
        posts_list = []

        try:
            client.get(url)

            WebDriverWait(client, timeout).until(
                lambda driver: driver.execute_script("return document.readyState")
                == "complete"
            )

            WebDriverWait(client, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            current_link = client.current_url
            page_links = client.get_page_links()

            if not page_links:
                return "No links found."

            for page_url in page_links:
                try:
                    if page_url == current_link:
                        posts_list.extend(client.scrape_page(movie_type))
                    else:
                        client.get(page_url)
                        WebDriverWait(client, timeout).until(
                            lambda driver: driver.execute_script(
                                "return document.readyState"
                            )
                            == "complete"
                        )
                        WebDriverWait(client, timeout).until(
                            EC.presence_of_element_located((By.TAG_NAME, "body"))
                        )
                        posts_list.extend(client.scrape_page(movie_type))
                except TimeoutException:
                    print(f"Timeout occurred while processing {page_url}")
                except WebDriverException as e:
                    print(f"WebDriver error on {page_url}: {e}")

        except TimeoutException:
            print(f"Timeout occurred while opening the main URL: {url}")
        except WebDriverException as e:
            print(f"WebDriver error on main URL: {url}, error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

        return posts_list
