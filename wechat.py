# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 09//17//2021//
"""
import pyautogui as pag  # 实现python控制鼠标键盘
import pyperclip  # 实现python调取剪切板
import time
import os
import random


def main():
    for i in range(2):
        pag.moveTo(272, 629, 1)
        pag.click()
        pag.typewrite(message='woliekaile1', interval=0.1)
        pag.moveTo(270, 584, 0.1)
        pag.click()
        pag.scroll(-1)
        pag.moveTo(202, 283, 0.1)
        pag.click()
        pag.moveTo(300, 629, 1)
        pag.click()
        time.sleep(0.2)
        pag.press('enter')


if __name__ == "__main__":
    main()