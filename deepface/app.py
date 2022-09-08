from deepface import DeepFace
import cv2

img_1_path = r"deepface\my-face-data\training-dataset/ujjwal.jpeg"
img_2_path = r"deepface\my-face-data\testing-dataset/y.jpg"

img1 = cv2.imread(img_1_path)
img2 = cv2.imread(img_2_path)

window_name = 'image'

cv2.imshow(window_name, img1)
cv2.imshow(window_name, img2)
cv2.waitKey(0)

model_name = 'VGG-Face'

response = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name)

print(response)

df = DeepFace.find(img_path = img_1_path, db_path = r"deepface\my-face-data\testing-dataset/")
print(df.head())





