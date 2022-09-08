from deepface import DeepFace
import matplotlib.pyplot as plt

img_1_path = r"D:\Projects\Python\vulture\deepface\dataset/img1.jpg"
img_2_path = r"D:\Projects\Python\vulture\deepface\dataset/img2.jpg"

model_name = 'Facenet'

response = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name)
# If model name isn't passed, VGG-Face is set as the default model
# Multiple stages of verification are taking place in the back-end of this verify() function

print(response)

# Let's see what those stages are and how it works:
img1 = DeepFace.detectFace(img_1_path)
img2 = DeepFace.detectFace(img_2_path)





