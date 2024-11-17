import os
import time

import pyautogui
import pygetwindow
import keyboard
from pygetwindow import Win32Window

import config

def get_window(wname:str):
    w = pygetwindow.getWindowsWithTitle(wname)
    while len(w) < 1:
        w = pygetwindow.getWindowsWithTitle(wname)
    return w[0]

def tail(file):
    file.seek(0, 2)
    while True:
        lines = file.readline()
        if not lines:
            time.sleep(0.1)
            continue
        yield lines



def open_fever():
    os.system(f"\"{config.fever_launcher_path}\"")
    fwindow = get_window('发烧游戏')
    time.sleep(3.5)
    return fwindow

def open_nel(fever_window: Win32Window):
    fever_window.activate()
    pyautogui.click(fever_window.left + fever_window.width - 250, fever_window.top + fever_window.height - 150)
    fwindow = pygetwindow.getWindowsWithTitle('《我的世界》-启动器')
    while len(fwindow) < 1 or fwindow[0].width < 500 or fwindow[0].height < 500:
        fwindow = pygetwindow.getWindowsWithTitle('《我的世界》-启动器')
    time.sleep(0.7)
    adwindow = pygetwindow.getWindowsWithTitle("通告")
    if len(adwindow) > 0: adwindow[0].close()
    return fwindow[0]

def open_game_window(nel_window: Win32Window):
    nel_window.activate()
    time.sleep(0.2)
    pyautogui.click(nel_window.left + 25, nel_window.bottom - 40)
    return get_window('《我的世界》-开始游戏')

def open_id_select_menu(game_prestart_window: Win32Window):
    game_prestart_window.activate()
    pyautogui.moveTo(game_prestart_window.left + 150, game_prestart_window.top + 190)
    time.sleep(0.2)
    pyautogui.click()
    return get_window('《我的世界》-角色选择')

def select_id_and_start(id_select_window: Win32Window):
    id_select_window.activate()
    time.sleep(0.2)
    pyautogui.click(id_select_window.midtop.x, id_select_window.midtop.y + 200)
    time.sleep(0.1)
    pyautogui.click(id_select_window.right - 50, id_select_window.bottom - 30) # ?

def send_chat(msg:str, bjd_window:Win32Window):
    keyboard.send('t')
    time.sleep(0.05)
    keyboard.write(msg)
    keyboard.send('enter')

def get_bjd_window():
    return get_window("布吉岛")

qd_sent = False
def send_qd(bjd_window: Win32Window):
    global qd_sent
    if qd_sent: return
    bjd_window.restore()
    bjd_window.activate()
    send_chat("/qd", bjd_window)
    qd_sent = True
    time.sleep(0.5)
    pyautogui.click(bjd_window.center.x, bjd_window.center.y - 100)
    time.sleep(0.1)
    keyboard.send("esc")

vip_send = False
def send_vip(bjd_window: Win32Window):
    global vip_send
    if vip_send: return
    bjd_window.restore()
    bjd_window.activate()
    keyboard.send("x")
    time.sleep(0.1)
    pyautogui.rightClick()
    time.sleep(0.5)
    pyautogui.click(bjd_window.center.x - 100, bjd_window.center.y - 140)
    time.sleep(0.5)
    pyautogui.click(bjd_window.center.x - 100, bjd_window.center.y - 140)
    vip_send = True

if __name__ == '__main__':
    select_id_and_start(open_id_select_menu(open_game_window(open_nel(open_fever()))))
    while True:
        log_lines = tail(config.log_file)
        for log_line in log_lines:
            print(log_line)
            if log_line == "": continue
            if log_line.__contains__("Connecting to"):
                print("connecting!!!!")
            if log_line.__contains__("player CIT-"):
                print("connected, send qd")
                w = get_bjd_window()
                send_qd(w)
                time.sleep(0.5)
                send_vip(w)