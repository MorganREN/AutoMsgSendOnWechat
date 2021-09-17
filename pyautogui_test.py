# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 09//17//2021//
"""
import pyautogui as pag

# 获取当前鼠标光标的位置
currentMouseX, currentMouseY = pag.position()
print(currentMouseX, currentMouseY)

# 获取当前屏幕的分辨率
# screenWidth, screenHeight = pag.size()
#
# # 2秒钟鼠标移动坐标为42，46位置，线性移动
# pag.moveTo(x=42, y=46, duration=2, tween=pag.linear)
#
# # 1秒鼠标移到屏幕中央
# # pag.moveTo(screenWidth/2, screenHeight/2, duration=1)
#
# # 鼠标左击一次
# pag.click()
