import cv2
import numpy as np
import pyautogui
import time


template = cv2.imread('2019-07-02_06-55_1.png', cv2.IMREAD_GRAYSCALE)
#field = cv2.imread("field.JPG", cv2.IMREAD_GRAYSCALE)
fish = cv2.imread("fish_big.JPG", cv2.IMREAD_GRAYSCALE)


def find_fishing(): #ищет поплавок миниигры-рыбалки
    screen_width, screen_height = pyautogui.size()
    bottom_half_y = screen_height // 2
    region = (100, 300, screen_width - 100, bottom_half_y)


    while "BIBA":
        screenshot = pyautogui.screenshot(region=region)

        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        loc = np.where(res >= threshold)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            print("sleep")
            time.sleep(4)
        if len(loc[0]) == 0:
            continue
        for pt in zip(*loc[::-1]):
            x = pt[0]
            #print("x=", x)
            if 700<=x<=1000:
                return x
            else:
                break

def fishing_planet(x): #прохождение мини-игры рыбалки
    if 650<=x<=840:
        pyautogui.mouseDown(button="left")
    else:
        pyautogui.mouseUp(button="left")
        pyautogui.mouseDown(button='left')
        time.sleep(0.1)
        pyautogui.mouseUp(button="left")


def find_spot(): #найти рыбное место и закинуть туда удочку
    screen_width, screen_height = pyautogui.size()
    bottom_half_y = screen_height // 2
    region = (100, 300, screen_width - 100, bottom_half_y)

    




while "Я сосу бибу":
    x = find_fishing()
    fishing_planet(x)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        print("sleep")
        time.sleep(4)