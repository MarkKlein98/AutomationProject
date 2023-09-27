from imports.imports import *


class Mapping(TestCase):

    def setUp(self) -> None:
        self.driver_object = Driver()
        self.my_driver = self.driver_object.driver
        self.my_driver.get(link)

    @classmethod
    def setUpClass(cls):
        # Navigate to the folder and run 'npm start' in the background
        cls.server_process = subprocess.Popen(
            "cd C:/Users/omrik/sources/Plasma-Dashboard && npm start",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Give the server some time to start
        time.sleep(5)

    # --------------------------------------------------------------------------------------------------------

    # [Mapping]
    def test_click_menu_mapping(self):
        Actions(self.my_driver).click_element('XPATH', menu_mapping)
        Actions(self.my_driver).url_change()
        self.assertTrue(self.my_driver.current_url == 'http://localhost/mapping')

    def test_click_Clear(self):
        self.test_click_menu_mapping()
        Actions(self.my_driver).click_element('XPATH', mapping_Clear)

    def test_click_Map(self):
        self.test_click_menu_mapping()
        Actions(self.my_driver).click_element('XPATH', mapping_Map)

    def test_click_Export_to_CSV(self):
        self.test_click_menu_mapping()
        Actions(self.my_driver).click_element('XPATH', mapping_Export_to_CSV)

    def test_click_Domain(self):
        self.test_click_menu_mapping()
        Actions(self.my_driver).click_element('XPATH', mapping_Domain)

    def test_click_Hostname(self):
        self.test_click_menu_mapping()
        Actions(self.my_driver).click_element('XPATH', mapping_Hostname)

    def test_click_OS(self):
        self.test_click_menu_mapping()
        Actions(self.my_driver).click_element('XPATH', mapping_OS)

    def test_click_OS_Version(self):
        self.test_click_menu_mapping()
        Actions(self.my_driver).click_element('XPATH', mapping_OS_Version)

    def test_click_last_login(self):
        self.test_click_menu_mapping()
        Actions(self.my_driver).click_element('XPATH', mapping_last_login)

    # --------------------------------------------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()

    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.quit()
