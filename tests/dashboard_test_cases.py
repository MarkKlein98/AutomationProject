from imports.imports import *



class Dashboard(TestCase):

    def setUp(self) -> None:
        self.my_driver = Driver()
        self.my_driver.driver.get(link)
    # --------------------------------------------------------------------------------------------------------


    def test_complete_activation(self):
        Actions.click_element(self, 'XPATH', dashboard_complete_activation)


    def test_partial_activation(self):
        Actions.click_element(self, 'XPATH', dashboard_partial_activation)
        self.assertTrue(self.my_driver.driver.find_element(By.XPATH, dashboard_partial_activation_choosing_text))


    def test_complete_deActivation(self):
        Actions.click_element(self, 'XPATH', dashboard_complete_deActivation)



    # --------------------------------------------------------------------------------------------------------
    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.driver.quit()