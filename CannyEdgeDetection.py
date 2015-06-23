import cv2
import numpy as np
from matplotlib import pyplot as plt

try:
	image = sys.argv[1]
except Exception, e:
	image = 'lena.jpg'


img = cv2.imread(image,0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()