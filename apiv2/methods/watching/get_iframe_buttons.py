from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from typing import List, Dict
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from apiv2.utils import data_return, is_valid_url
import apiv2
from bs4 import BeautifulSoup


class GetIframeButtons:

    def get_all_iframe_buttons(
        client: "apiv2.Client", url: str
    ) -> List[Dict[str, str]]:
        iframe_info_list = []
        try:
            client.get(url)
            client.wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            client.remove_ads()

            watch_section = client.find_element(By.CSS_SELECTOR, "#watch")
            li_elements = watch_section.find_elements(By.TAG_NAME, "li")

            for index, li in enumerate(li_elements, 1):
                try:
                    if li.get_attribute("aria-label") == "embed":
                        iframe = li.find_element(By.CSS_SELECTOR, "iframe")
                        src = iframe.get_attribute("src")
                        if is_valid_url(src):
                            iframe_info_list.append(
                                {
                                    "id": f"iframe_embed_{index}",
                                    "name": "Embedded Iframe",
                                    "src": src,
                                }
                            )
                    elif "active" in li.get_attribute("class"):
                        iframe = li.find_element(By.TAG_NAME, "iframe")
                        src = iframe.get_attribute("src")
                        if is_valid_url(src):
                            iframe_info_list.append(data_return(index, src))
                    else:
                        try:
                            client.wait.until(
                                EC.element_to_be_clickable((By.TAG_NAME, "li"))
                            )
                            client.execute_script("arguments[0].scrollIntoView();", li)
                            li.click()
                            sleep(0.3)

                            iframe = client.find_element(By.TAG_NAME, "iframe")
                            src = iframe.get_attribute("src")
                            if is_valid_url(src):
                                iframe_info_list.append(
                                    {
                                        "id": f"iframe_{index}",
                                        "name": li.text or f"Unnamed_{index}",
                                        "src": src,
                                    }
                                )
                        except Exception as e:
                            print(f"Couldn't click element {index}: {e}")
                            try:
                                actions = ActionChains(client)
                                actions.move_to_element(li).click().perform()
                                sleep(0.2)

                                iframe = client.find_element(By.TAG_NAME, "iframe")
                                src = iframe.get_attribute("src")
                                if is_valid_url(src):
                                    iframe_info_list.append(data_return(index, src, li))

                            except Exception as e2:
                                print(f"Failed again to click element {index}: {e2}")
                                continue
                except Exception as e:
                    print(f"Couldn't process element {index}: {e}")
                    continue

        except Exception as e:
            print(f"error while processing the page: {e}")

        return iframe_info_list
