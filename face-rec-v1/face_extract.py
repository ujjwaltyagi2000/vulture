from deepface import DeepFace
from retinaface import RetinaFace
import face_recognition as fr
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import os

img_1_path = r"face-rec-v1\testing-dataset\aum.jpeg"
img_2_path = r"face-rec-v1\testing-dataset\ujjwal_nobeard.jpeg"
img_3_path = r"face.jpeg"

path = r"face-rec-v1\detected-faces"

faces = RetinaFace.extract_faces(img_path = img_1_path, align = False)
new_faces = RetinaFace.extract_faces(img_path = img_2_path, align = False)

model_name = 'Facenet'

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

new_face_num=1

for new_face in new_faces:
    
    new_rgb_face=cv2.cvtColor(new_face,cv2.COLOR_BGR2RGB)
    
    cv2.imwrite(os.path.join(path , f"new_face{new_face_num}.jpeg"), new_rgb_face)
    # cv2.imwrite(f"face-rec-v1\testing-dataset\face{face_num}.jpeg",rgb_face)
    cv2.imshow('Face',new_rgb_face)
    cv2.waitKey(2000)
    new_face_num+=1

# for index in range(1,face_num):
# img_path = r"face1.jpeg"
# response = DeepFace.verify(img1_path=img_path, img2_path=img_2_path, model_name=model_name)
# print(response)
#     response2 = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name, detector_backend='retinaface')
#     print(response2)
# response2 = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name, detector_backend='retinaface')
# print(response2)
# response = DeepFace.verify(img1_path=r"face-rec-v1\detected-faces\face4.jpeg", img2_path=r"face-rec-v1\detected-faces\new_face1.jpeg", model_name=model_name)
# print(response)
# known_image = fr.load_image_file(r"face-rec-v1\detected-faces\face1.jpeg")
# unknown_image = fr.load_image_file(r"face-rec-v1\detected-faces\new_face1.jpeg")
known_image = fr.load_image_file(r"face-rec-v1\testing-dataset\aum.jpeg")
unknown_image = fr.load_image_file(r"face-rec-v1\testing-dataset\ujjwal.jpeg")

known_encoding = fr.face_encodings(known_image)[0]
unknown_encoding = fr.face_encodings(unknown_image)[0]

results = fr.compare_faces([known_encoding], unknown_encoding)
print(results)