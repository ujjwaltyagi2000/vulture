from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2

# FACE VERIFICATION:
img_1_path = r"face-rec-v1\testing-dataset\tm.jpeg"
img_2_path = r"face-rec-v1\testing-dataset\ujjwal.jpeg"

model_name = 'VGG-Face' #Models: Facenet, VGG-Face, ArcFace

response = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name, tolerance = 0.5)
print(response)

# faces = DeepFace.detectFaces(img_1_path)







