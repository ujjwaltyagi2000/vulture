# from retinaface import RetinaFace as rf
from deepface import DeepFace as df
import matplotlib.pyplot as plt
import face_recognition as fr
import cv2
import os

# PATHS:
faces_path = r"face-rec-v1\detected-faces"
training_img_path = r"face-rec-v1\training-dataset\ujjwal.jpeg"

# Face extraction from group photo:
def extract_faces(image):

    # image = fr.load_image_file(r"face-rec-v1\testing-dataset\aum.jpeg")
    # extract_faces(image)
    
    height, width = image.shape[0], image.shape[1]

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    copy=image.copy()

    path = r"face-rec-v1\detected-faces"

    face_locations = fr.face_locations(image)
    print(face_locations)

    for i in range(len(face_locations)):

        x1, y1, x2, y2 = face_locations[i][3]-150, face_locations[i][0]-250, face_locations[i][1]+150, face_locations[i][2]+150
        # 0 --> top left --> -100 
        # 1 --> top right --> +100
        # 2 --> top right --> -100
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

        cv2.imwrite(os.path.join(path , f"chehra{i+1}.jpeg"), crop_img)

# showing image:
def show_face(image):

    cv2.imshow('Face',image)
    cv2.waitKey(2000)

# counting images in a directory:
def count_files(directory):

    count = 0
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            count += 1

    print(count)
    return count

# verification using face_recognition:
def fr_verify():
    pass

# verification using DeepFace
def df_verify():
    
    model_name = 'VGG-Face'
    
    # files = count_files(path) --> multiple images can be loaded like this using an iteration from 1-files
    
    image = fr.load_image_file(r"face-rec-v1\testing-dataset\aum.jpeg") 
    extract_faces(image)

    files = count_files(faces_path) # multiple images can be loaded from this using an iteration from 1-files

    for i in range(0,files):

        face_path = os.path.join(faces_path , f"chehra{i+1}.jpeg")

        response = df.verify(img1_path=face_path, img2_path=training_img_path, model_name=model_name)
        print(response)
    
print("Vulture Initiating........")
df_verify()


