import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from Base.base import Base
from contact.contact_linkedin import *
from contact.message import messageLinkedin
class Testcase(unittest.TestCase):
    def testAutoSendmsg(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = Chrome(options=options)
        self.driver.maximize_window()
# Đăng nhập cách 1:
        try:
            self.driver.get('https://www.linkedin.com/')
            Base(self.driver).send_keys_to_element(('name','session_key'),username)
            
        except:
            self.driver.get('https://www.linkedin.com/')
            Base(self.driver).send_keys_to_element(('name','session_key'),username)
        Base(self.driver).send_keys_to_element(('name','session_password'),password)
        Base(self.driver).click_element(('xpath','//button[@type="submit"]'))
# Đăng nhập cách 2:
        # self.driver.get('https://www.linkedin.com/')

    #     cookies= [{'name': 'lang', 'value': 'v=2&lang=en-us'},
    # {'name': 'bcookie', 'value': 'v=2&2dfc056d-e528-448f-8ba8-431b2db3c0cf'},
    # {'name': 'bscookie', 'value': 'v=1&202307191237341b18f356-2548-42ab-8220-17a686702835AQGoiBa1QnQ8DVAVPVj9ezb_SSc9iXBj'},
    # {'name': 'JSESSIONID', 'value': 'ajax:7146788679260160815'},
    # {'name': 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg', 'value': '1'},
    # {'name': 'aam_uuid', 'value': '48752029502764003903891862024755059401'},
    # {'name': 'liap', 'value': 'true'},
    # {'name': 'li_at', 'value': 'AQEDAUUbiXQB6OQSAAABiW4pSqQAAAGJkjXOpE4AGj0Pvv4uKxp8IonSbAu_wr4iozUU_fpqxUvUkL9geYqfmNPF06Go597du3EJ1_s-pOw5Bl6L1Nv1131jCvNALdNXOc8Xcc57gKBsswuC5RO8S8yI'},
    # {'name': 'timezone', 'value': 'Asia/Bangkok'},
    # {'name': 'li_theme', 'value': 'light'},
    # {'name': 'li_theme_set', 'value': 'app'},
    # {'name': '_gcl_au', 'value': '1.1.56862246.1689770350'},
    # {'name': 'li_sugr', 'value': 'e22f7978-301f-4e59-82fd-e79ec7823810'},
    # {'name': '_guid', 'value': '062ee05b-af07-4b1d-bcbd-86f25d6003c0'},
    # {'name': 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg', 'value': '-637568504%7CMCIDTS%7C19558%7CMCMID%7C48568820437863441413948958513680181506%7CMCAAMLH-1690375149%7C3%7CMCAAMB-1690375149%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689777549s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C161955901'},
    # {'name': 'UserMatchHistory', 'value': 'AQIW2Jde7OjVoAAAAYluKVR9QdhC3VUYpe__-j9ihfVztIjwhtHy0qpiE9uAxpQF7ZyFL805ZdR8584go2rtbU1N7hChigFyb_4Ax-THJ14wkplwgtXRBC1OF7TxAi-6hxcsaSpM0eC7wyyT2qqkVfgxW7NN58lyywLQrQdzcKmMEN_tzU4LF28feT5jJhZTSLqgz2yvW6u3lYVPSHyMYY0MYQjbOSg9LG-T7S5NH2VPq0G1RZbaQ32CvSQjcfiKSm-4V94gBd2acojXu2OY-tkCx7dN2DC0O3-qH8CPOhKzUeFAzJ1t9idK6hGyMlcmrH-PYQbI55c4n7-tN39vulXH074766g'},
    # {'name': 'AnalyticsSyncHistory', 'value': 'AQJ0Cj5G6wm46QAAAYluKVR9vqC_C_2N-goocv_NiiU2UN93zZOooUxsHpxTKOdQ65MrZuJ0Kf9SkVXjYuyt3g'},
    # {'name': 'lms_ads', 'value': 'AQGCsiyV1a7PXgAAAYluKVW6FL4DW-V6wOBtmIoeI6qQWQA0VWLLKAKk6L_2PNSV0Os8YYS6vw_uY4xbSWwaK1bX-LrtZuKI'},
    # {'name': 'lms_analytics', 'value': 'AQGCsiyV1a7PXgAAAYluKVW6FL4DW-V6wOBtmIoeI6qQWQA0VWLLKAKk6L_2PNSV0Os8YYS6vw_uY4xbSWwaK1bX-LrtZuKI'},
    # {'name': 'ln_or', 'value': 'eyI0MzQ2MTM3IjoiZCJ9'},
    # {'name': 'lidc', 'value': '"b=TB64:s=T:r=T:a=T:p=T:g=3170:u=1:x=1:i=1689770434:t=1689856747:v=2:sig=AQH5bHKAb4FxbzFMrS_V6zyv6R9APJNs"'},
    # {'name': 'sdsc', 'value': '34%3A1%2C1689770436247%7EJAPP%2C0%7EJBSK%2C-15165jvt3Wru%2F1BBVGTxw9dtuT%2BzTKz4%3D'},
    # {'name': 'useragent', 'value': 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2'},
    # {'name': '_uafec', 'value': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F114.0.0.0%20Safari%2F537.36'}
    #     ]
    #     for cookie in cookies:
    #         self.driver.add_cookie(cookie)
    #     self.driver.get('https://www.linkedin.com/')
    #     try:
    #         Base(self.driver).click_element(('id','reload-button'))
    #     except:
    #         None
        urls= file_mau['URL'][:60]
        for i in urls:
            self.driver.get(i)
            print(i)
            try:
                Base(self.driver).click_element(('xpath','(//button[@aria-label="More actions"])[2]'))
            except:
                print('Không bắt được element')
            # try:
            #     # try:
            #         try:    
            #             Base(self.driver).click_element(('xpath','//button[@class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view pvs-profile-actions__action"]//li-icon[@type="connect"]'))
            #         except:
            #             Base(self.driver).click_element(('xpath','(//button[@aria-label="More actions"])[2]'))
            #             Base(self.driver).click_element(('xpath','(//div[@class="artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view full-width display-flex align-items-center"]//li-icon[@type="connect"])[2]'))
            #         Base(self.driver).click_element(('xpath','//button[@aria-label="Add a note"]'))
            #         msg= messageLinkedin(self)
            #         Base(self.driver).send_keys_to_element(('name','message'),msg)
            #         time.sleep(2)
            #         Base(self.driver).click_element(('xpath','//button[@aria-label="Send now"]'))
            #         time.sleep(3)
                # except:
                #     Base(self.driver).click_element(('xpath','//div[@class="entry-point pvs-profile-actions__action"]'))
                #     msg= messageLinkedin(self)
                #     Base(self.driver).send_keys_to_element(('xpath','//div[@role="textbox"]'),msg)
                #     Base(self.driver).click_element(('xpath','//button[@type="submit"]'))
                #     time.sleep(2)
                #     Base(self.driver).click_element(('xpath','//button[@class="msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]'))
            # except:
            #     None
        input('Nhấn Enter để đóng trình duyệt...')

if __name__ == '__main__':
    unittest.main()
