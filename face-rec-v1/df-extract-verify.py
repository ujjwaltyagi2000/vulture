from retinaface import RetinaFace as rf
from deepface import DeepFace as df
import matplotlib.pyplot as plt
import cv2
import os

def show_face(image):

    # plt.imshow(image)
    # plt.show()
    cv2.imshow('Face',rgb_face)
    cv2.waitKey(2000)

img_1_path = r"face-rec-v1\testing-dataset\ujjinb.jpeg"
img_2_path = r"face-rec-v1\training-dataset\ujjwal.jpeg"
path = r"D:\Projects\Python\vulture\face-rec-v1\detected-faces"

faces = rf.extract_faces(img_path = img_1_path, align = True)
# new_faces = rf.extract_faces(img_path = img_2_path, align = False)

model_name = 'Facenet'

# response = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name, detector_backend="skip")
# print(response)
# If model name isn't passed, VGG-Face is set as the default model
# Multiple stages of verification are taking place in the back-end of this verify() function
face_num=1

for face in faces:
    
    rgb_face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
    show_face(rgb_face)

    face_path = os.path.join(path , f"face{face_num}.jpeg")
    
    cv2.imwrite(face_path, rgb_face)

    response = df.verify(img1_path=face_path, img2_path=img_2_path, model_name=model_name, detector_backend="skip")
    print(response)
    
    face_num+=1
    
    # response = df.verify(img1_path=face_path, img2_path=img_2_path, model_name=model_name, detector_backend="skip")
    # print(response)
    # print(type(response))


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
# known_image = fr.load_image_file(r"face-rec-v1\testing-dataset\aum.jpeg")
# unknown_image = fr.load_image_file(r"face-rec-v1\testing-dataset\ujjwal.jpeg")

# known_encoding = fr.face_encodings(known_image)[0]
# unknown_encoding = fr.face_encodings(unknown_image)[0]

# results = fr.compare_faces([known_encoding], unknown_encoding)
# print(results)

