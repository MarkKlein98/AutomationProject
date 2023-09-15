from imports.imports import *



class Menu(TestCase):

    def setUp(self) -> None:
        self.my_driver = Driver()
        self.my_driver.driver.get(link)


                    # [Icon tests.]

    def test_click_menu_icon(self):
        Actions.click_element(self, 'XPATH', menu_active)
        Actions.click_element(self, 'XPATH', menu_icon)
        self.assertEqual(self.my_driver.driver.current_url, 'http://localhost/dashboard')



                    # [Dashboard tests.]

    def test_click_menu_dashboard(self):
        Actions.click_element(self, 'XPATH', menu_active)
        Actions.click_element(self, 'XPATH', menu_dashboard)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/dashboard')



                    # [Active tests.]

    def test_click_menu_active(self):
        Actions.click_element(self, 'XPATH', menu_active)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/active')



                    # [Mapping tests.]

    def test_click_menu_mapping(self):
        Actions.click_element(self, 'XPATH', menu_mapping)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/mapping')



                    # [Profiles tests.]

    def test_click_menu_profiles(self):
        Actions.click_element(self, 'XPATH', menu_profiles)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/profiles')



                    # [Devices tests.]

    def test_click_menu_devices(self):
        Actions.click_element(self, 'XPATH', menu_devices)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/devices')








    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.driver.quit()