import cv2
image_file = './data/lena.jpg'
img = cv2.imread(image_file) # cv2.IMREAD_COLOR
img2 = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
print(img.shape, img2.shape)
cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

cv2.waitKey(0)      #이 두가지 작업 해줘야 꼭 창이 뜸
cv2.destroyAllwindows()     #이 두가지 작업 해줘야 꼭 창이 뜸
