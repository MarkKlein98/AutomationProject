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
        Actions(self.my_driver).click_element('XPATH', devices_Export_to_csv)

    def test_click_Domain(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH', devices_Domain)

    def test_click_Hostname(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH', devices_Hostname)

    def test_click_Os(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH', devices_Os)

    def test_click_EDR(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH', devices_EDR)

    def test_click_Plasma_installation(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH', devices_Plasma_installation)

    def test_click_Last_Connection(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH', devices_Last_Connection)

    def test_click_my_first_device(self):
        self.test_click_menu_devices()
        Actions(self.my_driver).click_element('XPATH', devices_my_first_device)

    def test_click_device_Export_to_csv(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        Actions(self.my_driver).click_element('XPATH', devices_Export_to_csv_device)

    def test_click_APP_name(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        Actions(self.my_driver).click_element('XPATH', devices_APP_name)

    def test_click_select_all(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH', devices_select_all)

    def test_click_add_button(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        Actions(self.my_driver).click_element('XPATH', devices_add_button)

    def test_click_Add_applications(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        self.test_click_select_all()
        Actions(self.my_driver).click_element('XPATH', devices_Add_applications)

    def test_search_my_first_device(self):
        self.test_click_menu_devices()
        self.test_click_my_first_device()
        search = self.my_driver.find_element(By.XPATH, devices_search_my_first_device)
        search.send_keys('WebView2 Runtime')

    def test_correct_amount_of_devices(self):
        self.test_click_menu_devices()
        time.sleep(1)
        self.my_driver.find_element(By.XPATH, devices_plasmaID).click()
        Actions(self.my_driver).scroll_down()
        amount_of_devices = len(self.my_driver.find_elements(By.CSS_SELECTOR, plasma_profile))
        print(f'Total amount of plasma devices: {amount_of_devices}')
        Actions(self.my_driver).click_element('XPATH', menu_dashboard)
        Actions(self.my_driver).url_change()
        plasma_devices = self.my_driver.find_element(By.XPATH, dashboard_plasma_devices)
        # self.assertEqual(amount_of_devices, int(plasma_devices.text))

    # --------------------------------------------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()

    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.quit()
