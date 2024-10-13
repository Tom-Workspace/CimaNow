from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from apiv2.methods import Methods
from apiv2.logger import Logger


class Client(webdriver.Chrome, Methods):

    options: webdriver.ChromeOptions = webdriver.ChromeOptions()

    def __init__(
        self,
        headless: bool = False,
        wait_until_duration: int = 30,
    ):
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--window-size=1500,1200")
        if headless:
            self.options.add_argument("--headless=new")
        service = Service(executable_path=ChromeDriverManager().install())
        super().__init__(options=self.options, service=service)
        self.wait: WebDriverWait = WebDriverWait(self, wait_until_duration)
