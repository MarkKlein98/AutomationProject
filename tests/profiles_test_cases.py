import tests.devices_test_cases
from imports.imports import *



class Profiles(TestCase):

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

    # [Profiles]
    def test_click_menu_profiles(self):
        Actions(self.my_driver).click_element('XPATH', menu_profiles)
        Actions(self.my_driver).url_change()
        self.assertTrue(self.my_driver.current_url == 'http://localhost/profiles')


    def test_click_export_to_CSV(self):
        self.test_click_menu_profiles()
        Actions(self.my_driver).click_element('XPATH', profiles_export_to_csv)


    def test_correct_amount_of_profiles(self):
        self.test_click_menu_profiles()
        time.sleep(1)
        self.my_driver.find_element(By.XPATH, profiles_ID_category).click()
        Actions(self.my_driver).scroll_down(4)
        amount_of_profiles = len(self.my_driver.find_elements(By.CSS_SELECTOR, profiles_plasma_profile))
        print(f'Total amount of plasma profiles: {amount_of_profiles}')
        Actions(self.my_driver).click_element('XPATH', menu_dashboard)
        Actions(self.my_driver).url_change()
        plasma_profiles = self.my_driver.find_element(By.CSS_SELECTOR, dashboard_plasma_devices)
        # self.assertEqual(amount_of_profiles, int(plasma_profiles.text))


    def test_click_profile_id(self):
        self.test_click_menu_profiles()
        Actions(self.my_driver).click_element('CSS_SELECTOR', profiles_ID)
        Actions(self.my_driver).url_change()
        # self.assertEqual(self.my_driver.current_url, 'http://localhost/base/profile')


    def test_click_profile_app_name(self):
        self.test_click_profile_id()
        Actions(self.my_driver).click_element('XPATH', profiles_app_name)


    def test_profile_click_export_to_CSV(self):
        self.test_click_profile_id()
        Actions(self.my_driver).click_element('XPATH', profiles_export_to_csv_profile)
        time.sleep(1)

    # --------------------------------------------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()

    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.quit()



