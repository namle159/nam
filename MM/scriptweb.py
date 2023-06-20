import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
from random import randint
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import data
class ScriptWeb (unittest.TestCase):
    def test_web(self):
        self.driver = Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mm.ecomyze.asia/')
        self.driver.find_element(By.XPATH, '(//a[@class="product-image image-loaded"])[1]').click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, '//div[@class="col-lg-4 col-md-4 col-xs-12 mm-infor-detail show-desktop"]//a[@class="button add_to_cart_button ajax_add_to_cart product_type_simple"]').click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, '//div[@class="table-visiable-dk"]//a[@title="Xem Giỏ hàng"]').click()
        # # time.sleep(2)
        # xem_gio_hang = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='oc-mini-cart-menu']//a[contains(text(), 'Xem giỏ hàng')]")))
        # xem_gio_hang.click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//a[contains(text(), '	Tiến hành Thanh toán')]").click()
        # thay_doi_dia_chi = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, '//div[@class="top-bar-left col-md-8"]//span[@class="change"]')))
        # thay_doi_dia_chi.click()
        # time.sleep(2)
        # chon_tp = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element(By.ID, 'select-city')))
        # Select(chon_tp).select_by_index(2)
        # chon_quan = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element('id', 'select-district')))
        # time.sleep(5)
        # Select(chon_quan).select_by_index(randint(1,15))
        # chon_phuong = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.driver.find_element('id', 'select-ward')))
        # time.sleep(5)
        # Select(chon_phuong).select_by_index(randint(1,10))
        # self.driver.find_element(By.NAME, 'address').send_keys(str(random.randint(0, 100)))
        # self.driver.find_element(By.XPATH, "(//button[contains(text(), 'Lưu')])[1]").click()
        # try:
        #     btn_giu_nguyen = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Không, giữ nguyên')]")))
        #     btn_giu_nguyen.click()
        # except:
        #     None
        # time.sleep(5)
        # name = random.choice(data.name_list)
        # self.driver.find_element(By.NAME, 'billing_last_name').send_keys(name)
        # gmail = random.choice(data.email_list)
        # self.driver.find_element(By.NAME, 'billing_email').send_keys(gmail)
        # self.driver.find_element(By.NAME, 'billing_phone').send_keys(f'01234567+ {randint(10,99)}')
        # self.driver.find_element(By.NAME, 'woocommerce_checkout_place_order').click()
        # ma_don_hang = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//li[@class="order"]//strong')))
        # ma_don_hang_ = ma_don_hang.text
        # self.driver.find_element(By.XPATH, "//div[@class='mm-wishlist mm-flex']//a[contains(text(), 'Theo dõi Đơn')]").click()
        # self.driver.find_element(By.ID, 'orderid').send_keys(ma_don_hang_)
        # self.driver.find_element(By.ID, 'order_email').send_keys(gmail)
        # self.driver.find_element(By.NAME, 'track').click()
        input("Nhấn Enter để đóng trình duyệt...")

if __name__ == '__main__':
    unittest.main()
    
