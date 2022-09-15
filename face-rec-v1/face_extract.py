from deepface import DeepFace
from retinaface import RetinaFace
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import os

img_1_path = r"face-rec-v1\testing-dataset\aum.jpeg"
img_2_path = r"face-rec-v1\testing-dataset\sb.jpeg"
img_3_path = r"face.jpeg"

path = r"face-rec-v1\detected-faces"

faces = RetinaFace.extract_faces(img_path = img_1_path, align = False)

model_name = 'VGG-Face'

# response = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name, detector_backend='retinaface')
# print(response)
# If model name isn't passed, VGG-Face is set as the default model
# Multiple stages of verification are taking place in the back-end of this verify() function
face_num=1

for face in faces:
    rgb_face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
    
    cv2.imwrite(os.path.join(path , f"face{face_num}.jpeg"), rgb_face)
    # cv2.imwrite(f"face-rec-v1\testing-dataset\face{face_num}.jpeg",rgb_face)
    cv2.imshow('Face',rgb_face)
    cv2.waitKey(2000)
    face_num+=1

# for index in range(1,face_num):
# img_path = r"face1.jpeg"
# response = DeepFace.verify(img1_path=img_path, img2_path=img_2_path, model_name=model_name)
# print(response)
#     response2 = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name, detector_backend='retinaface')
#     print(response2)
# response2 = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name, detector_backend='retinaface')
# print(response2)