import cv2
import numpy as np
img=cv2.imread("D:\Img processing\img300.jpg")
#cv2.imshow(img)
b,g,r=cv2.split(img)
#cv2.imshow("blue",b)
#cv2.imshow("green",g)
#cv2.imshow("red",r)
h,w=img.shape[:2]
gray=np.zeros((h,w),np.uint8)
for i in range(h):
    for j in range(w):
        gray[i,j]=int(0.299*r[i,j]+0.587*g[i,j]+0.114*b[i,j])
cv2.imshow("gray",gray)
gx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]],dtype=np.float64)
gy=np.array([[-1,-2,-1],[0,0,0],[1,2,1]],dtype=np.float64)
sobel=np.zeros((h,w),np.uint8)
for i in range(1,h-1):
    for j in range(1,w-1):
        temp=gray[i-1:i+2,j-1:j+2]
        gx_val=np.sum(gx*temp)
        gy_val=np.sum(gy*temp)
        sobel[i,j]=np.sqrt(gx_val**2+gy_val**2)
sobel=np.clip(sobel,0,255).astype(np.uint8)
cv2.imshow("sobel manual",sobel)
sx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
sy=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
sobel_cv=np.sqrt(sx**2+sy**2)
sobel_cv=np.clip(sobel_cv,0,255).astype(np.uint8)
cv2.imshow("sobel built in",sobel_cv)
cv2.waitKey(0)