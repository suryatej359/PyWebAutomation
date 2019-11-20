from libAuto.common.driver_manager import DriverManager
from libAuto.logging.logger import LogProvider

log = LogProvider(file_path='../../logs/facebook.log',log_level='INFO')


class CommonUtil:

    def __init__(self, driver=None):
        self.driver=driver
        if not self.driver:
            self.initialize_driver()

    def initialize_driver(self):
        driverMgr = DriverManager()
        self.driver = driverMgr.get_chrome_driver()

    # Fetching the elements
    def get_element_by_xpath(self, xpath, name):
        resp = None
        try:
            # print("path to find element","'"+id+"'")
            # xpath = "'"+xpath+"'"
            resp = self.driver.find_element_by_xpath(xpath)
            if resp:
                log.info_log(f"Element : {name} found successfully")
                print(f"Element : {name} found successfully")
        except Exception as e:
            log.error_log(f"Fail to find element: {name}")
            print(f'Fail to find element: {name}')
        return resp

    def get_element_by_id(self, id, name):
        id_ele = None
        try:
            # print("path to find element","'"+id+"'")
            # xpath = "'"+xpath+"'"
            id_ele = self.driver.find_element_by_id(id)
            if id_ele:
                log.info_log(f"Element : {name} found successfully")
                print(f"Element : {name} found successfully")
        except Exception as e:
            log.error_log(f"Fail to find element: {name}")
            print(f'Fail to find element: {name}')
        return id_ele

    def send_web_element_keys(self,wbe,value,name):
        try:
            wbe.send_keys(value)
            log.info_log(f"Succesfully send the key to {name}")
            print(f"Succesfully send the key to {name}")
        except Exception as e:
            log.error_log(f"Fail to send the key to : {name}")
            print(f"Fail to send the key to : {name}")

    def click_on(self, element, name):
        try:
            element.click()
            log.info_log(f"Succesfully Clicked on {name}")
            print(f"Succesfully Clicked on {name}")
        except Exception as e:
            log.error_log(f"Fail to click : {name}")
            print(f"Fail to click : {name}")


if __name__=='__main__':
    pass