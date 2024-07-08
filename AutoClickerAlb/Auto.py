import cv2
import numpy as np
import pyautogui
import time

# Загрузка изображения объекта (шаблона)
template = cv2.imread('2019-07-02_06-55_1.png', cv2.IMREAD_GRAYSCALE)
field = cv2.imread("field.JPG", cv2.IMREAD_GRAYSCALE)
prev_center=None
screen_width, screen_height = pyautogui.size()
bottom_half_y = screen_height//2
region = (100, 300, screen_width-100, bottom_half_y)
#print(screen_width//2)


while True:
    # Захватываем изображение с экрана
    screenshot = pyautogui.screenshot(region=region)

    # Преобразуем изображение в массив numpy и конвертируем его в формат BGR для OpenCV
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Преобразуем кадр в оттенки серого
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Поиск объекта на кадре с использованием метода шаблонного сопоставления
    res = cv2.matchTemplate(gray_frame, field, cv2.TM_CCOEFF_NORMED)

    # Установка порогового значения для обнаружения объекта
    threshold = 0.7
    loc = np.where(res >= threshold)
    if len(loc[0]>0):
        field_x, field_y=loc[::-1]

        field_width, field_height = field.shape[::-1]


        field_area = np.array(pyautogui.screenshot(region=(835, 222, 1129, 259)))
        gray_field_area=cv2.cvtColor(field_area, cv2.COLOR_BGR2GRAY)

        res_object = cv2.matchTemplate(gray_field_area, template, cv2.TM_CCOEFF_NORMED)
        threshold_object = 0.6
        loc_object=np.where(res_object>=threshold_object)
        for pt in zip(*loc_object):


    # Отображаем кадр
    #cv2.imshow('Object Detection', frame)

    #pyautogui.mouseUp(button='left')
    # Если пользователь нажимает клавишу 'q', выходим из цикла
    if cv2.waitKey(1) & 0xFF == ord('q'):
        time.sleep(4)

# Закрываем все окна OpenCV
cv2.destroyAllWindows()