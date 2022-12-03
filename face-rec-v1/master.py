from deepface import DeepFace as df
import face_recognition as fr
import cv2
import os

# PATHS:
faces_path = r"detected-faces"
training_img_path = r"training-dataset\ujjwal.jpeg"
testing_img_path = r"testing-dataset\aum.jpeg"

# Image Labels:
training_label = "Training Image"
testing_label = "Testing Image"
matched_face_label = "Matched Face"

# Face extraction from group photo:
def extract_faces(image):

    # image = fr.load_image_file(r"face-rec-v1\testing-dataset\aum.jpeg")
    # extract_faces(image)
    
    height, width = image.shape[0], image.shape[1]

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    copy=image.copy()

    path = r"detected-faces"

    face_locations = fr.face_locations(image)
    print("Face Locations: ")
    print(face_locations)
    print("\n")

    for i in range(len(face_locations)):

        x1, y1, x2, y2 = face_locations[i][3]-150, face_locations[i][0]-250, face_locations[i][1]+150, face_locations[i][2]+150
        # 0 --> top left --> -100 
        # 1 --> top right --> +100
        # 2 --> top right --> -100
        # 3 --> top left --> -100

        new_coordinates = [x1, y1, x2, y2]
        print(f"Coordinates of Face {i+1} bounding box after padding:")
        print(new_coordinates)
        print("\n")
        
        x1 = max(0, x1)
        x1 = min(x1,width)
        x2 = max(0, x2)
        x2 = min(x2,width)
        y1 = max(0, y1)
        y1 = min(y1,height)
        y2 = max(0, y2)
        y2 = min(y2,height)
        
        print(f"Final Coordinates of Face {i+1} bounding box after limiting bounding boxes to image bounds:")
        print(x1, y1, x2, y2)
        print("\n")
        
        copy =  cv2.rectangle(copy, (x1, y1), (x2, y2), (255,0,255), 2)

        crop_img = image[y1:y2, x1:x2]

        cv2.imwrite(os.path.join(path , f"face{i+1}.jpeg"), crop_img)

# showing image:
def disp_img(path, label):

    image = cv2.imread(path)
    cv2.namedWindow(label, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(label, 1000, 750)
    cv2.imshow(label, image)  
    cv2.waitKey(10000)  

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
    
    model_name = 'VGG-Face'

    min_distance = 1

    true_face_index = 0
    
    image = fr.load_image_file(testing_img_path) 
    extract_faces(image)

    files = count_files(faces_path) # multiple images can be loaded from this using an iteration from 1-files

    for i in range(0,files):

        face_path = os.path.join(faces_path , f"face{i+1}.jpeg")

        response = df.verify(img1_path=face_path, img2_path=training_img_path, model_name=model_name, prog_bar = True)
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
cv2.waitKey(10000)  
cv2.destroyAllWindows()