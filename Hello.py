import cv2
import numpy as np

count = 1
imgMain = cv2.imread('/home/omar/Desktop/Omar/ImageProcceing/HW1/ImagesForHW/Fig%d.tif'%(count))
cv2.imshow('sample',imgMain)
cv2.imwrite('sample.tif',imgMain)


while (count<100) :
    count = count + 1
    imgTemp = cv2.imread('/home/omar/Desktop/Omar/ImageProcceing/HW1/ImagesForHW/Fig%d.tif'%(count))
    imgMain=cv2.addWeighted(imgMain,.9,imgTemp,0.1,1)
    print(count)

cv2.imshow('addWighted',imgMain)
cv2.imwrite('addWighted.tif',imgMain)

imgMain=cv2.fastNlMeansDenoisingColored(imgMain,None,5,5,7,21)
cv2.imshow('afterDenoise',imgMain)
cv2.imwrite('afterDenoise.tif',imgMain)
cv2.waitKey()
print ('GoodBy')