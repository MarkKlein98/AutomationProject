from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    def __init__(self):
        options = Options()
        service = Service(ChromeDriverManager().install())
        options.add_argument('--disable-extentions')
        options.add_argument('--start-maximized')
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(service=service, options=options)


link = 'http://localhost:80/'