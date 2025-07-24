import cv2
import numpy as np
img=cv2.imread("D:\\Img processing\\img300.jpg")
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
sigma=0.5
k=2*int(3*sigma)+1
ax=np.arange(-k//2+1,k//2+1)
xx,yy=np.meshgrid(ax,ax)
kernel=np.exp(-(xx**2+yy**2)/(2.*sigma**2))
kernel=kernel/(2*np.pi*sigma**2)
kernel/=kernel.sum()
pad=kernel.shape[0]//2
padded=np.pad(gray, pad, mode='reflect')
H,W=gray.shape
gaus=np.zeros((H, W), dtype=np.float64)
for i in range(H):
    for j in range(W):
        patch=padded[i:i+kernel.shape[0],j:j+kernel.shape[1]]
        gaus[i,j]=np.sum(patch * kernel)
gaus=np.clip(gaus, 0, 255).astype(np.uint8)
cv2.imshow("gaussian manual", gaus)
gaus_cv=cv2.GaussianBlur(gray, (k, k), sigma)
cv2.imshow("gaussian built in", gaus_cv)
cv2.waitKey(0)