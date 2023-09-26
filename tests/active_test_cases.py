from imports.imports import *



class Active(TestCase):

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

    # [Active]
    def test_click_menu_active(self):
        Actions(self.my_driver).click_element('XPATH', menu_active)
        Actions(self.my_driver).url_change()
        self.assertTrue(self.my_driver.current_url == 'http://localhost/active')

    def test_Export_to_CSV(self):
        self.test_click_menu_active()
        Actions(self.my_driver).click_element('XPATH',Active_Export_to_CSV)

    def test_PlasmaID_click(self):
        self.test_click_menu_active()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH',Active_PlasmaID)

    def test_Hostname_click(self):
        self.test_click_menu_active()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH',Active_Hostname)



    # --------------------------------------------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()

    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.quit()