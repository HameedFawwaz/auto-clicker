import pyautogui
import cv2

while True:

    firstx, firsty = pyautogui.locateCenterOnScreen('hit.png', confidence = 0.9)

    pyautogui.click(firstx, firsty)