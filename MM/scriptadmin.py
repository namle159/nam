import multiprocessing
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import random
from random import randint
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class ScriptAdmin (unittest.TestCase):
    def test_admin  (self):
        self.driver = Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mm.ecomyze.asia/admin/')
        self.driver.find_element('id', 'user_login').send_keys('admin')
        self.driver.find_element('id', 'user_pass').send_keys('YNvNgOBHJrm^W!O!YT(2Ws1n')
        self.driver.find_element('id', 'wp-submit').click()
        xem_chi_tiet_don_hang = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(('xpath', '//a[@class="order-view"]')))
        xem_chi_tiet_don_hang.click()         
        time.sleep(2)      
        self.driver.back()                                              
        thay_doi_trang_thai_don_hang = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(('xpath', '//a[@aria-label="Chuẩn bị hàng"]')))
        thay_doi_trang_thai_don_hang.click()
        thay_doi_trang_thai_don_hang = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(('xpath', '//a[@aria-label="Đang xử lý"]')))
        thay_doi_trang_thai_don_hang.click()
        in_hoa_don = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(('xpath', '//a[@alt="PDF Packing Slip"]')))
        in_hoa_don.click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        self.driver.find_element('xpath', "//div[contains(text(), 'Các sản phẩm')]").click()
        xem_san_pham = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(('xpath', '//a[@class="row-title"]')))
        xem_san_pham.click()
        # input("Nhấn Enter để đóng trình duyệt...")

if __name__ == '__main__':
    # unittest.main()
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=unittest.main, args=())
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()
    