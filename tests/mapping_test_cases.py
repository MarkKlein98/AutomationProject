from imports.imports import *


class Mapping(TestCase):

    def setUp(self) -> None:
        self.my_driver = Driver()
        self.my_driver.driver.get(link)
    # --------------------------------------------------------------------------------------------------------





    # --------------------------------------------------------------------------------------------------------
    def tearDown(self) -> None:
        time.sleep(1)
        self.my_driver.driver.quit()
