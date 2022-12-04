from deepface import DeepFace as df
import face_recognition as fr
from tkinter import filedialog
import cv2
import os

# paths:
faces_path = r"detected-faces"
training_img_path = r"training-dataset\anshuman.jpg"
testing_img_path = r"testing-dataset\p7.jpg"

# models and metrics:
models = ['VGG-Face', 'Facenet', 'OpenFace', 'DeepFace', 'DeepID', 'Dlib', 'ArcFace']
metrics = ['cosine', 'euclidean', 'euclidean_l2']

# image Labels:
training_label = "Training Image"
testing_label = "Testing Image"
matched_face_label = "Matched Face"

# face extraction from group photo:
def extract_faces(image):
    
    height, width = image.shape[0], image.shape[1]

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    copy=image.copy()

    path = r"detected-faces"

    face_locations = fr.face_locations(image)
    print("Face Locations: ")
    print(face_locations)
    print("\n")

    for i in range(len(face_locations)):

        # x1, y1, x2, y2 = face_locations[i][3]-100, face_locations[i][0]-200, face_locations[i][1]+100, face_locations[i][2]+100

        # face Coordinates:
        x1, y1, x2, y2 = face_locations[i][3], face_locations[i][0], face_locations[i][1], face_locations[i][2]
        coordinates = [x1, y1, x2, y2]
        print("\nFace Coordinates: ")
        print(coordinates)
        
        face_height = abs(y1-y2)
        face_width = abs(x1-x2)

        # print(f"\nWidth = {face_width}")
        # print(f"Height = {face_height}")

        # padded coordinates:
        px1, py1, px2, py2 = x1-(face_width//2), y1-(face_height//2), x2+(face_width//2), y2+(face_height//2)
        # x1 --> -50% 
        # y1 --> -50%
        # x2 --> +50%
        # y2 --> +50%

        # restrictions for bounding box coordinates so they stay within image bounds:
        px1 = max(0, px1)
        px1 = min(px1,width)
        px2 = max(0, px2)
        px2 = min(px2,width)
        py1 = max(0, py1)
        py1 = min(py1,height)
        py2 = max(0, py2)
        py2 = min(py2,height)

        new_coordinates = [px1, py1, px2, py2]
        print("\nPadded Face Coordinates: ")
        print(new_coordinates)

        pface_height = abs(py1-py2)
        pface_width = abs(px1-px2)

        print(f"\nPadded Width = {pface_width}")
        print(f"Padded Height = {pface_height}")
        # x1 = max(0, x1)
        # x1 = min(x1,width)
        # x2 = max(0, x2)
        # x2 = min(x2,width)
        # y1 = max(0, y1)
        # y1 = min(y1,height)
        # y2 = max(0, y2)
        # y2 = min(y2,height)

        copy =  cv2.rectangle(copy, (px1, py1), (px2, py2), (255,0,255), 2)

        crop_img = image[py1:py2, px1:px2]

        cv2.imwrite(os.path.join(path , f"face{i+1}.jpeg"), crop_img)

# showing image:
def disp_img(path, label):

    image = cv2.imread(path)
    cv2.namedWindow(label, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(label, 1000, 750)
    cv2.imshow(label, image)  
    cv2.waitKey(2000)  

# counting images in a directory:
def count_files(directory):

    count = 0
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            count += 1

    return count

# verification using face_recognition:
def fr_verify():
    pass

# verification using DeepFace
def df_verify():
    
    model = models[0]

    metric = metrics[0]

    min_distance = 1

    true_face_index = 0
    
    image = fr.load_image_file(testing_img_path) 
    extract_faces(image)

    files = count_files(faces_path) # multiple images can be loaded from this using an iteration from 1-files

    for i in range(0,files):

        face_path = os.path.join(faces_path , f"face{i+1}.jpeg")

        response = df.verify(img1_path=face_path, img2_path=training_img_path, model_name=model, distance_metric=metric, prog_bar = True, enforce_detection=False)
        print(response)
        
        if response['verified'] == True and min_distance>response['distance']:

            min_distance = response['distance']

            true_face_index = i

    return true_face_index      
    
print("\n\nVulture Initiating........\n")

face_index = df_verify()

disp_img(training_img_path, training_label)
disp_img(testing_img_path, testing_label)

matched_face_path = os.path.join(faces_path , f"face{face_index+1}.jpeg")
face_img = cv2.imread(matched_face_path)
fm_height, fm_width = face_img.shape[0], face_img.shape[1]
cv2.namedWindow(matched_face_label, cv2.WINDOW_NORMAL)
cv2.resizeWindow(matched_face_label, fm_width, fm_height)
cv2.imshow(matched_face_label, face_img)  
cv2.waitKey(2000)  
cv2.destroyAllWindows()