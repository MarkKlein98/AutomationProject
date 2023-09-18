from imports.imports import *



class General(TestCase):

    def setUp(self) -> None:
        self.my_driver = Driver()
        self.my_driver.driver.get(link)
# --------------------------------------------------------------------------------------------------------


    # [Login button]
    def test_login_button(self):
        Actions.click_element(self, 'LINK_TEXT', login_button)
        Actions.url_change(self)
        self.assertEqual(self.my_driver.driver.current_url, 'http://localhost/login')


    # [Icon]
    def test_click_menu_icon(self):
        Actions.click_element(self, 'XPATH', menu_active)
        Actions.click_element(self, 'XPATH', menu_icon)
        Actions.url_change(self)
        self.assertEqual(self.my_driver.driver.current_url, 'http://localhost/dashboard')


    # [Dashboard]
    def test_click_menu_dashboard(self):
        Actions.click_element(self, 'XPATH', menu_active)
        Actions.click_element(self, 'XPATH', menu_dashboard)
        Actions.url_change(self)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/dashboard')


    # [Active]
    def test_click_menu_active(self):
        Actions.click_element(self, 'XPATH', menu_active)
        Actions.url_change(self)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/active')


    # [Mapping]
    def test_click_menu_mapping(self):
        Actions.click_element(self, 'XPATH', menu_mapping)
        Actions.url_change(self)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/mapping')


    # [Profiles]
    def test_click_menu_profiles(self):
        Actions.click_element(self, 'XPATH', menu_profiles)
        Actions.url_change(self)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/profiles')


    # [Devices]
    def test_click_menu_devices(self):
        Actions.click_element(self, 'XPATH', menu_devices)
        Actions.url_change(self)
        self.assertTrue(self.my_driver.driver.current_url == 'http://localhost/devices')


    # [Plasma logo]
    def test_click_plasma_logo(self):
        Actions.click_element(self, 'XPATH', menu_active)
        Actions.click_element(self, 'XPATH', plasma_logo)
        Actions.url_change(self)
        self.assertEqual(self.my_driver.driver.current_url, 'http://localhost/dashboard')

    # --------------------------------------------------------------------------------------------------------
    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.driver.quit()