import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('./images/input.jpg')
#calcHist(image,channel,mask,histogramSize,Range)
histogram = cv2.calcHist([image],[0],None,[256],[0,256])

#ravel() flatens our image array from 2 to 1
plt.hist(image.reveal(),256,[0,256])
plt.show()

#viewing separate bgr channels
color = ('b','g','r')

#separate color and plot each in the histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2,color = col)
    plt.xlim([0,256])

plt.show()