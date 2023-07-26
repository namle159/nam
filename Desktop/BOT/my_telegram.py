# import unittest
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import time
# from Base.base import Base
# class Testcase(unittest.TestCase):
#     def testAutoSendmsg(self):
#         options = Options()
#         options.add_argument("--disable-notifications")
#         self.driver = Chrome(options=options)
#         self.driver.get('https://web.telegram.org/k/')
#         cookies = [
#           {
#                 'name': 'useragent',
#                 'value': 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2'
#             },
#             {
#                 'name': '_uafec',
#                 'value': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F114.0.0.0%20Safari%2F537.36'
#             }
#         ]
#         for cookie in cookies:
#             self.driver.add_cookie(cookie)

#         self.driver.get('https://web.telegram.org/k/')
#         self.driver.maximize_window()
#         Base(self.driver).click_element(('xpath','//div[@class="c-ripple"]'))
#         Base(self.driver).send_keys_to_element(('xpath','//div[@inputmode="decimal"]'),'84789114159')
#         Base(self.driver).click_element(('xpath','//button[@class="btn-primary btn-color-primary rp"]'))
#         # danh_sach_nguoi_gui= ['https://www.linkedin.com/in/thien-ho-6b7b9a16a/?fbclid=IwAR1fXtqT3BT6EPlt40a4XMOVC92sXcRGT-7NMktmqLxO8Kn_sAre7HMqE28']
#         # for i in danh_sach_nguoi_gui:
#             # self.driver.get(i)
#         input('Nhấn Enter để đóng trình duyệt...')
# if __name__ == '__main__':
#     unittest.main()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Token của bot Telegram (lấy từ BotFather)
TOKEN = "6297727958:AAG5ZMXpAlFBxLua9O8KHff5SLA-4-rjQkk"

# Hàm xử lý lệnh /get_group_id
def get_group_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    update.message.reply_text(f"ID của nhóm là: {chat_id}")

def main():
    # Tạo đối tượng updater
    updater = Updater(TOKEN, use_context=True)

    # Lấy đối tượng dispatcher để đăng ký các xử lý sự kiện
    dispatcher = updater.dispatcher

    # Đăng ký xử lý lệnh /get_group_id
    dispatcher.add_handler(CommandHandler("get_group_id", get_group_id))

    # Bắt đầu chạy bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()


