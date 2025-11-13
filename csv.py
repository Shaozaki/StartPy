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

# Metode Sobel
sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
plt.figure(figsize=(18, 19))
plt.subplot(221)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")
plt.subplot(222)
plt.imshow(sobelxy, cmap="gray")
plt.title("Sobel X Y")
plt.axis("off")
plt.subplot(223)
plt.imshow(sobelx, cmap="gray")
plt.title("Sobel X")
plt.axis("off")
plt.subplot(224)
plt.imshow(sobely, cmap="gray")
plt.title("Sobel Y")
plt.axis("off")
(-0.5, 959.5, 639.5, -0.5)
print("Deteksi tepi metode sobel")
# plt.savefig("hasil_deteksi.png")
# print("Menampilkan hasil di jendela baru...")
# plt.show()
