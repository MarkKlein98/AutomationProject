from imports.imports import *



class Dashboard(TestCase):

    def setUp(self) -> None:
        self.driver_object = Driver()
        self.my_driver = self.driver_object.driver
        self.my_driver.get(link)

    @classmethod
    def setUpClass(cls):
        # Navigate to the folder and run 'npm start' in the background
        cls.server_process = subprocess.Popen(
            "cd C:/Users/omrik/Source/Plasma-Dashboard && npm start",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Give the server some time to start
        time.sleep(5)

    # --------------------------------------------------------------------------------------------------------

    # [Dashboard]
    def test_click_menu_dashboard(self):
        Actions(self.my_driver).click_element('XPATH', menu_active)
        Actions(self.my_driver).click_element('XPATH', menu_dashboard)
        Actions(self.my_driver).url_change()
        self.assertTrue(self.my_driver.current_url == 'http://localhost/dashboard')


    # [Complete activation]
    def test_complete_activation(self):
        Actions(self.my_driver).click_element('XPATH', dashboard_complete_activation)


    # [Partial activation]
    def test_partial_activation(self):
        Actions(self.my_driver).click_element('XPATH', dashboard_partial_activation)
        self.assertTrue(self.my_driver.find_element(By.XPATH, dashboard_partial_activation_choosing_text))


    def test_partial_activation_cancel(self):
        self.test_partial_activation()
        Actions(self.my_driver).click_element('XPATH', dashboard_partial_activation_cancel)


    def test_partial_activation_activate(self):
        self.test_partial_activation()
        self.assertFalse()

    def test_Domain_click(self):
        self.test_partial_activation()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH',dashboard_Domain_Partial)

    def test_Hostname_click(self):
        self.test_partial_activation()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH',dashboard_Hostname_Partial)

    def test_OS_click(self):
        self.test_partial_activation()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH',dashboard_OS_Partial)

    def test_EDR_Click(self):
        self.test_partial_activation()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH',dashboard_EDR_Partial)

    def test_Plasma_installation_click(self):
        self.test_partial_activation()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH',dashboard_Plasma_installation_Partial)

    def test_Last_connection_click(self):
        self.test_partial_activation()
        time.sleep(1)
        Actions(self.my_driver).click_element('XPATH',dashboard_Last_connection_Partial)




    # [Complete deActivation]
    def test_complete_deActivation(self):
        Actions(self.my_driver).click_element('XPATH', dashboard_complete_deActivation)



    # --------------------------------------------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()

    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.quit()