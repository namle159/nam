import multiprocessing
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
class ScriptKho (unittest.TestCase):
    def test_kho(self):  
        service = Service(executable_path='path/to/chromedriver')
        self.driver = WebDriver(service=service)
        self.driver.maximize_window()
        self.driver.get('https://mm.ecomyze.asia/')
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Đăng nhập')]").click()
        self.driver.find_element(By.ID, 'username').send_keys('mmanphu')
        self.driver.find_element(By.ID, 'password').send_keys('6B55blhp#a$mXz5zOknS0(Iy')
        self.driver.find_element(By.NAME, 'login').click()
        time.sleep(2)
        xem_chi_tiet_don_hang = self.driver.find_element(By.XPATH, '//td[@class="dokan-order-id"]//a[@target="_blank"]')
        xem_chi_tiet_don_hang.click()
        time.sleep(2)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        in_don_hang = self.driver.find_element(By.XPATH, '//a[@data-tip="In đơn hàng"]')
        in_don_hang.click()
        time.sleep(2)
        self.driver.switch_to.window(handles[0])
        sua_don_hang = self.driver.find_element(By.XPATH, '(//a[@data-original-title="Sửa đơn hàng"])[1]')
        sua_don_hang.click()
        self.driver.find_element(By.XPATH, '(//a[@data-original-title="Đang xử lý"])[1]').click()
if __name__ == '__main__':
    jobs = []
    for i in range(1):
        p = multiprocessing.Process(target=unittest.main, args=())
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()
    # suite = unittest.TestSuite()
    # for i in range(2):
    #     suite.addTest(script_kho('test_kho'))
    # unittest.TextTestRunner(verbosity=2).run(suite)

    
        
        