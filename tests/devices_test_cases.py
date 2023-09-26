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
            "cd C:/Users/shale/sources/Plasma-Dashboard && npm start",
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
        self.assertEqual(amount_of_devices, int(plasma_devices.text))

    # --------------------------------------------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()

    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.quit()
