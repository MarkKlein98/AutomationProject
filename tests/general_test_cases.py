import math
import secrets

from imports.imports import *



class General(TestCase):

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


    # [Login button]
    def test_login_button(self):
        Actions(self.my_driver).click_element('LINK_TEXT', login_button)
        Actions(self.my_driver).url_change()
        self.assertEqual(self.my_driver.current_url, 'http://localhost/login')


    # [Icon]
    def test_click_menu_icon(self):
        Actions(self.my_driver).click_element('XPATH', menu_active)
        Actions(self.my_driver).click_element('XPATH', menu_icon)
        Actions(self.my_driver).url_change()
        self.assertEqual(self.my_driver.current_url, 'http://localhost/dashboard')


    # [Plasma logo]
    def test_click_plasma_logo(self):
        Actions(self.my_driver).click_element('XPATH', menu_active)
        Actions(self.my_driver).click_element('XPATH', plasma_logo)
        Actions(self.my_driver).url_change()
        self.assertEqual(self.my_driver.current_url, 'http://localhost/dashboard')

    # --------------------------------------------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()

    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.quit()



