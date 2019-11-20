"""
The driver manager responsible to return driver object depending for different browsers.

The browsers supported

Chrome
Firefox
*Opera
*ie
*edge

"""

from selenium import webdriver


class DriverManager(object):

    def get_chrome_driver(self):
        # relative path or create absolute path dynamically
        self.driver=None
        try:
            self.driver = webdriver.Chrome(executable_path='../../dependencies/drivers/Chrome/chromedriver.exe')
        except Exception as e:
            print(e)
        return self.driver

    def get_firefox_driver(self):
        pass

    def get_ie_driver(self):
        pass

    def get_opera_driver(self):
        pass


if __name__=="__main__":
    cls = DriverManager()
    cls.get_chrome_driver()