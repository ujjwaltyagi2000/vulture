from deepface import DeepFace
from deepface.detectors import FaceDetector
from retinaface import RetinaFace
import matplotlib.pyplot as plt
import cv2
import pandas as pd


# FIND NUMBER OF FACES IN AN IMAGE

# img_path = r"face-rec-v1\testing-dataset\aum.jpeg"

# detector_name = "retinaface"

# img = cv2.imread(img_path)

# detector = FaceDetector.build_model(detector_name) #set opencv, ssd, dlib, mtcnn or retinaface

# objects = FaceDetector.detect_faces(detector, detector_name, img)

# print("there are ",len(objects)," faces")

# for obj in objects:

#     cv2.imshow('Image', obj)
#     cv2.waitKey(2000)

df = DeepFace.find(img_path = r"face-rec-v1\training-dataset\ujjwal.jpeg", db_path = r"face-rec-v1\testing-dataset/")
print(df.head())