# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from Base.base import Base
from contact.message import *
from contact.contact_zalo import *
class Testcase(unittest.TestCase):
    def testAutoSendmsg(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = Chrome(options=options)
        self.driver.get('https://chat.zalo.me/')
        cookies = [
            {"name": "_zlang", "value": "vn"},
            {"name": "__zi", "value": "3000.SSZzejyD6jKgdB6gqHOQm2lJi_xFM1JOQ8-Xz84K5z0XnwFqX1GJb275fB2C4nELBC2Zlp8.1"},
            {"name": "_ga", "value": "GA1.2.1571600609.1690364716"},
            {"name": "_gid", "value": "GA1.2.1196855595.1690364716"},
            {"name": "__zi-legacy", "value": "3000.SSZzejyD6jKgdB6gqHOQm2lJi_xFM1JOQ8-Xz84K5z0XnwFqX1GJb275fB2C4nELBC2Zlp8.1"},
            {"name": "app.event.zalo.me", "value": "6738453721370915594"},
            {"name": "_ga", "value": "GA1.3.1571600609.1690364716"},
            {"name": "_gid", "value": "GA1.3.1196855595.1690364716"},
            {"name": "zpsid", "value": "mKDC.384418145.9.Pw3ZKeZfrQFfA3orXEdLe_sQfv2mtU6IiDZXbld-yC2WkLzXYOKXO-pfrQC"},
            {"name": "zpw_sek", "value": "Okwm.384418145.a0.xjpCIOcWrFReOJtWgA3KzlA2iPshclQUv-MkiiRYcBlGcUo0qVYEkU6FuhJkdUdKzD73q-g8X7nBeRa2ISGrtG"},
            {"name": "_gat", "value": "1"},
            {"name": "useragent", "value": "TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2"},
            {"name": "_uafec", "value": "Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F114.0.0.0%20Safari%2F537.36"},
            {"name": "z_uuid", "value": "a76c0e3d-0d6c-4ac2-86a7-cb382e14cbcd-8d3fec2581d3961f3037851d5cc0039c"},
        ]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://chat.zalo.me/')
        self.driver.maximize_window()
        # Base(self.driver).click_element(('xpath','//a[contains(text(),"Với mật khẩu")]'))
        # Base(self.driver).send_keys_to_element(('xpath','//input[@placeholder="Mật khẩu"]'),'Hello123')
        # Base(self.driver).click_element(('xpath','//a[contains(text(),"Đăng nhập với mật khẩu")]'))

        # sdt= ['0368525951','0356818998']
        # '0368525951'
        # urls= file_mau['Business Phone'][6:6]
        # for i in urls:
        #     Base(self.driver).click_element(('xpath','//div[@data-translate-title="STR_CONTACT_ADD_FRIEND"]'))

        #     try:
        #         Base(self.driver).send_keys_to_element(('xpath','//input[@placeholder="Số điện thoại "]'),i)
        #         Base(self.driver).click_element(('xpath','//div[@data-translate-inner="STR_SEARCH"]'))
        #         Base(self.driver).click_element(('xpath','//div[@data-id="btn_UserProfile_SendMsg"]'))
        #         print(i)
        #     except:
        #         Base(self.driver).click_element(('xpath','//div[@data-translate-inner="STR_CANCEL"]'))
        #         print('Không tìm được thông tin')
        #     try:
        #         messageZalo(self)
        #         ten_nguoi_nhan= Base(self.driver).getElement(('xpath','//div-b18[@class="header-title flx flx-al-c flex-1"]'))
        #         ten_nguoi_nhan_text = ten_nguoi_nhan.text
        #         print(f'Đã gửi tin nhắn cho {ten_nguoi_nhan_text}')
        #     except:
        #         print('Không gửi được tin nhắn')
        input('Nhấn Enter để đóng trình duyệt...')

if __name__ == '__main__':
    unittest.main()
