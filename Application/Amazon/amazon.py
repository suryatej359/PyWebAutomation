from libAuto.common.selenium_base import CommonUtil


class AmazonAutomation(CommonUtil):

    def launch(self,url):
        self.initialize_driver()
        self.driver.get(url)

    def signIn(self,xpath,name):
        acctList = self.get_element_by_xpath(xpath,name)
        self.click_on(acctList,name)


if __name__=='__main__':
    amz = AmazonAutomation()
    amz.launch('https://www.amazon.in')
    amz.signIn('//a[@id="nav-link-accountList"]',"AccountList")