from imports.imports import *



class Actions:
    def __init__(self):
        """
        This function is being called right before a test is about to be performed.
        :return:
        """
        self.my_driver = Driver()
        self.my_driver.driver.get(link)


    def click_element(self, locator, value):
        locator_type = getattr(By, locator)
        find = WebDriverWait(self.my_driver.driver, 10).until(EC.element_to_be_clickable((locator_type, value)))
        find.click()
        time.sleep(0.7)

    def element_visibility(self, locator, value):
        locator_type = getattr(By, locator)
        WebDriverWait(self.my_driver.driver, 10).until(EC.visibility_of_element_located((locator_type, value)))
        time.sleep(0.7)

    def url_change(self):
        WebDriverWait(self.my_driver.driver, 10).until(EC.url_changes(self))

