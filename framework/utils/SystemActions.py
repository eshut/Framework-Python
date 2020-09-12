from framework.Base.BaseElement import *
import pyautogui
import os
import time
import random
import cv2
import numpy as np
from random import choice
from string import ascii_lowercase, ascii_uppercase
from string import digits
from PIL import Image


FILES = jsonGetter.GetJson.getFile(CONFIG, "Files")


class SysOperations:
    @staticmethod
    def upload(file):
        time.sleep(2)
        path = os.getcwd() + FILES + file
        pyautogui.write(path)
        pyautogui.press('enter')

    @staticmethod
    def generate_string(x):
        string = [choice(ascii_uppercase + ascii_lowercase + ascii_lowercase + digits) for i in range(x)]
        random.shuffle(string)
        string = "".join(string)
        return string

    @staticmethod
    def compare_images(path_1, path_2):
        image1 = Image.open(path_1)
        size = image1.size
        image2 = Image.open(path_2)
        new_image2 = image2.resize(size)
        new_image2.save(path_2)

        img1 = cv2.imread(path_1 ,0)  # same
        img2 = cv2.imread(path_2 ,0)  # same

        try:
            res = cv2.absdiff(img2, img1)
            percentage = (np.count_nonzero(res) * 100) / res.size
        except:
            percentage = 99999
        return percentage