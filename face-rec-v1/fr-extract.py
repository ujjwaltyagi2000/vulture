import face_recognition as fr
from deepface import DeepFace as df
import cv2
import os

image = fr.load_image_file(r"face-rec-v1\testing-dataset\aum.jpeg")
height, width, channels= image.shape

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
copy=image.copy()

path = r"face-rec-v1\detected-faces"

face_locations = fr.face_locations(image)
print(face_locations)

for i in range(len(face_locations)):

    x1, y1, x2, y2 = face_locations[i][3]-100, face_locations[i][0]-100, face_locations[i][1]+100, face_locations[i][2]+100
    # 0 --> top left --> -100 
    # 1 --> top right -->+100
    # 2 --> top right -->-100
    # 3 --> top left --> -100

    new_coordinates = [x1, y1, x2, y2]

    print(new_coordinates)
    
    x1 = max(0, x1)
    x1 = min(x1,width)
    x2 = max(0, x2)
    x2 = min(x2,width)
    y1 = max(0, y1)
    y1 = min(y1,height)
    y2 = max(0, y2)
    y2 = min(y2,height)
    
    print(x1, y1, x2, y2)
    
    copy =  cv2.rectangle(copy, (x1, y1), (x2, y2), (255,0,255), 2)

    crop_img = image[y1:y2, x1:x2]
    # new_coordinates = [x1, y1, x2, y2]
    # print(new_coordinates)

    cv2.imshow("Crop", crop_img)
    cv2.waitKey(0)

    
    # cv2.imwrite(os.path.join(path , f"chehra{i}.jpeg"), crop_img)


cv2.imshow("Original", image)
cv2.imshow("Faces", copy)
# new_coordinates = [x1, y1, x2, y2]
# print(f"New coordinates = {new_coordinates}")
# crop_img = image[y1:y2, x1:x2]
# cv2.imwrite()

cv2.waitKey(0)