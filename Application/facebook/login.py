from libAuto.common.selenium_base import CommonUtil
from time import sleep


class Login(CommonUtil):
    USER_NAME_TEXT_FIELD_ID = 'email'
    PASSWORD_TEXT_FIELD_XPATH = '//input[@id="pass"]'
    LOGIN_BUTTON_XPATH = '//input[@value="Log In" and @type="submit"]'
    LOGOUT_MENU_XPATH = 'logoutMenu'
    LOGOUT_BUTTON_XPATH = ''

    def __init__(self,username, password):
        CommonUtil.__init__(self)
        self.username = username
        self.password = password

    def launch(self,url):
        self.driver.get(url)

    def login(self):
        # identify login element & enter text
        un = self.get_element_by_id(self.USER_NAME_TEXT_FIELD_ID, "UserName")
        self.send_web_element_keys(un,self.username,"UserName")
        sleep(2)
        # identify password & enter text
        pw = self.get_element_by_xpath(self.PASSWORD_TEXT_FIELD_XPATH,"Password")
        self.send_web_element_keys(pw,self.password,"Password")
        sleep(2)
        # identify login button & click
        log_in = self.get_element_by_xpath(self.LOGIN_BUTTON_XPATH,"LogIn Button")
        self.click_on(log_in,"LogIn Button")

    def logout(self):
        pass


if __name__=='__main__':
    obj = Login('9966406753','suryarebal')
    obj.launch('https://www.facebook.com/')
    obj.login()
