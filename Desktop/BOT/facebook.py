import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from Base.base import Base
from contact.contact_facebook import *
from contact.message import messageFB
class Testcase(unittest.TestCase):
    def testAutoSendmsg(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = Chrome(options=options)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        self.driver.find_element('name','email').send_keys(username)
        self.driver.find_element('name','pass').send_keys(password)
        self.driver.find_element('name','login').click()
        urls= file_mau['URL GROUP/CONTACT LIST/POST SEEDING'][:100]
        for i in contact_list: 
            self.driver.get(i)
            print(i)
            try:
                Base(self.driver).click_element(('xpath','//div[@aria-label="Xem đề xuất"]'))
                time.sleep(1)
            except:
                print('Không bắt được element')
            # try:
            #     Base(self.driver).click_element(('xpath','//div[@class="x78zum5 x1a02dak x139jcc6 xcud41i x9otpla x1ke80iy"]//div[@aria-label="Thêm bạn bè"]'))
            # except:
            #     None
            # Base(self.driver).click_element(('xpath','//span[contains(text(), "Nhắn tin")]'))
            # msg= messageFB(self)
            # Base(self.driver).click_element(('xpath','//div[@aria-label="Đóng đoạn chat"]'))
        input('Nhan Enter de dong trinh duyet...')

if __name__ == '__main__':
    unittest.main()
