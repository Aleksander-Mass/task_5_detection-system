# -*- coding: utf-8 -*-
"""30_11_23_task_5_cats.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PZipPap8_5ovFCNnQMHR2knMfWet7D4z
"""

import cv2
import matplotlib
#matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

img = cv2.imread("cats.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

xml_data = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
detecting = xml_data.detectMultiScale(img_gray, minSize=(30, 30))
detect = len(detecting)
if detect != 0:
    for (a, b, widht, height) in detecting:
        cv2.rectangle(img_color, (a, b), (a+height, b+widht), (0, 255, 0), 5)
plt.subplot()
plt.imshow(img_color)
plt.show()