import cv2
import numpy as np
import face_recognition as fr

# The library face_recognition supports only the BGR format of images. 
# While printing the output image we should convert it into RGB using OpenCV.

# img_bgr = fr.load_image_file('face-rec-v2/dataset/au.jpeg')
# img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

img_ujji=fr.load_image_file('face-rec-v2/dataset/tk.jpg')
img_ujji_rgb = cv2.cvtColor(img_ujji,cv2.COLOR_BGR2RGB)
# new_res = cv2.resize(img_ujji_rgb, (600, 450))

#--------- Detecting Face -------
face = fr.face_locations(img_ujji_rgb)[0]
copy = img_ujji_rgb.copy()

# ------ Drawing bounding boxes around Faces------------------------
cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
cv2.imshow('copy', copy)
cv2.imshow('ujji',img_ujji_rgb)
cv2.waitKey(0)

# #------to find the face location
# face = fr.face_locations(img_ujji)[0]

# #--Converting image into encodings
# train_encode = fr.face_encodings(img_ujji)[0]

# #----- lets test an image
# test = fr.load_image_file('face-rec-v2/dataset/y.jpg')
# test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
# test_encode = fr.face_encodings(test)[0]
# print(fr.compare_faces([train_encode],test_encode))
# cv2.rectangle(img_ujji, (face[3], face[0]),(face[1], face[2]), (255,0,255), 1)
# cv2.imshow('img_ujji', img_ujji)
# cv2.waitKey(0)