import numpy as np
import cv2
def distance(one,two):
    return np.sqrt(np.sum(np.power((one-two),2)))

img=cv2.imread("3.jpg")
width=img.shape[1]
height=img.shape[0]
myimg=np.zeros([height,width,3],np.uint8) #创建大小一样的画布
black=np.array([0,0,0])
white=np.array([255,255,255])
grey=np.array([125,125,125])
for y in range(0,height-1):
    for x in range(0, width - 1):
        current=img[y,x,:]
        right = img[y, x+1, :]
        down = img[y+1, x, :]
        if distance(current,right)>10 and distance(current,down)>10:
            myimg[y,x,:]=black
        elif distance(current,right)<=10 and distance(current,down)<=10:
            myimg[y,x,:]=white
        else:
            myimg[y,x,:]=grey
cv2.imwrite("3.jpg",myimg)