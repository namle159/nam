import pywinauto.findwindows as findwindows
from pywinauto import Application
import time
import pywinauto.mouse
from pywinauto import keyboard
from contact.contact_zalo import *
import pyautogui
try:
    zalo_path= r"C:\Users\johnlee\AppData\Local\Programs\Zalo\Zalo.exe"
    app= Application().start(zalo_path)
    zalo_window= None
    for hwnd in findwindows.find_windows():
        window= app.window(handle=hwnd)
        if window.window_text() == 'Zalo':
            zalo_window = window
            break

    if zalo_window:
        zalo_window.maximize()
        time.sleep(2)
        # urls= file_mau['Business Phone'][6:6]
        urls= ['0368525951','096643924','0356818998']
        for i in urls:
            pywinauto.mouse.click('left',(237,70))
            time.sleep(0.1)
            keyboard.send_keys('{VK_CONTROL down}a{VK_CONTROL up}')
            keyboard.send_keys(i, pause=0.01, with_spaces=True)
            time.sleep(0.001)
            pywinauto.mouse.click('left',(131,247))
            time.sleep(0.001)
            pywinauto.mouse.click('left',(237,70))
            pywinauto.mouse.click('left',(647,995))
            keyboard.send_keys('{VK_CONTROL down}a{VK_CONTROL up}')
            keyboard.send_keys('Em chào anh/chị',pause=0.001, with_spaces=True)
            pyautogui.keyDown('shift')
            pyautogui.press('enter')
            pyautogui.keyUp('shift')
            keyboard.send_keys('Em xin kết nối và chia sẻ báo cáo Social Listening chủ đề "Đêm Nhạc BLACKPINK BORNPINK - Người Việt Ủng Hộ Hay Phản Đối Nhiều Hơn?".',pause=0.001, with_spaces=True)
            pyautogui.keyDown('shift')
            pyautogui.press('enter')
            pyautogui.keyUp('shift')
            keyboard.send_keys('Báo cáo dài 17 trang, hơn 86 biểu đồ từ tổng quan đến chuyên sâu, cung cấp góc nhìn toàn diện về sự kiện này.',pause=0.001, with_spaces=True)
            pyautogui.keyDown('shift')
            pyautogui.press('enter')
            pyautogui.keyUp('shift')
            keyboard.send_keys('Anh/Chị xem báo cáo miễn phí ở đây ạ: https://slyze.co/c2JdjgA',pause=0.001, with_spaces=True)
            keyboard.send_keys('{ENTER}', pause=0.1, with_spaces=True)


    else:
        print('abc')
except:
    print('xyz')