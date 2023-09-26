from imports.imports import *



class Devices(TestCase):

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

    # [Devices]
    def test_click_menu_devices(self):
        Actions(self.my_driver).click_element('XPATH', menu_devices)
        Actions(self.my_driver).url_change()
        self.assertTrue(self.my_driver.current_url == 'http://localhost/devices')

    def test_click_Export_to_csv(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH',devices_Export_to_csv)

    def test_click_Domain(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH',devices_Domain)

    def test_click_Hostname(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH',devices_Hostname)

    def test_click_Os(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH',devices_Os)

    def test_click_EDR(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH',devices_EDR)

    def test_click_Plasma_installation(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH',devices_Plasma_installation)

    def test_click_Last_Connection(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH',devices_Last_Connection)

    def test_click_my_first_device(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH','//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/table/tbody/tr[4]/td[2]/a')

    def test_click_Export_to_csv(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        Actions(self.my_driver).click_element('XPATH','//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div[3]/button')

    def test_click_APP_name(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        Actions(self.my_driver).click_element('XPATH','//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/table/thead/tr/th[2]')

    def test_click_select_all(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH',"//input[@id='checkAll']")


    def test_click_add_button(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        Actions(self.my_driver).click_element('XPATH','//tbody/tr[1]/td[7]/button[1]')

    def test_click_Add_applications(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        self.test_click_select_all()
        Actions(self.my_driver).click_element('XPATH',"//button[contains(text(),'Add Applications')]")
    def test_search_my_first_device(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        search = self.my_driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/input')
        search.send_keys('WebView2 Runtime')





    # --------------------------------------------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()

    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.quit()