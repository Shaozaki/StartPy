import cv2
import numpy as np
import requests
from matplotlib import pyplot as plt

url = "https://cdn.pixabay.com/photo/2018/09/05/19/03/fantasy-3656849_1280.jpg"

r = requests.get(url)
with open("test.jpg", "wb") as f:
    f.write(r.content)
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(gray, (3, 3), 0)
