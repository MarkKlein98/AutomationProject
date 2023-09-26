from imports.imports import *



class Actions:
    def __init__(self, driver):
        self.my_driver = driver



    def click_element(self, locator, value):
        locator_type = getattr(By, locator)
        find = WebDriverWait(self.my_driver, 10).until(EC.element_to_be_clickable((locator_type, value)))
        find.click()
        time.sleep(0.7)

    def is_clickable(self, locator, value):
        locator_type = getattr(By, locator)
        WebDriverWait(self.my_driver, 10).until(EC.element_to_be_clickable((locator_type, value)))
        time.sleep(0.7)

    def is_visible(self, locator, value):
        locator_type = getattr(By, locator)
        WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located((locator_type, value)))
        time.sleep(0.7)

    def url_change(self):
        WebDriverWait(self.my_driver, 10).until(EC.url_changes(self))

