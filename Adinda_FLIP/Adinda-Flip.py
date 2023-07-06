import cv2

load = cv2.imread('adinda.jpg', 1)
flip = cv2.flip(load, 0)
flip1 = cv2.flip(load, 1)
flip2 = cv2.flip(load, 2)

cv2.imshow('Putar Gambar 0', flip)
cv2.imshow('Putar Gambar 1', flip1)
cv2.imshow('Putar Gambar 2', flip2)

cv2.waitkey(0)
cv2.destroyAllWindows()
