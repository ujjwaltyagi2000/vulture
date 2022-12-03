import face_recognition as fr
from deepface import DeepFace as df
import cv2
import os

image = fr.load_image_file(r"testing-dataset\techudyam.jpeg")
height, width = image.shape[0], image.shape[1]

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
copy=image.copy()
pad_copy=image.copy()

path = r"detected-faces"

face_locations = fr.face_locations(image)
print(face_locations)

for i in range(len(face_locations)):

    # x1, y1, x2, y2 = face_locations[i][3]-100, face_locations[i][0]-200, face_locations[i][1]+100, face_locations[i][2]+100
    #Face Coordinates:
    x1, y1, x2, y2 = face_locations[i][3], face_locations[i][0], face_locations[i][1], face_locations[i][2]
    coordinates = [x1, y1, x2, y2]
    print("\nFace Coordinates: ")
    print(coordinates)
    
    face_height = abs(y1-y2)
    face_width = abs(x1-x2)

    print(f"\nWidth = {face_width}")
    print(f"Height = {face_height}")

    #Padded coordinates:
    px1, py1, px2, py2 = x1-(face_width//2), y1-(face_height//2), x2+(face_width//2), y2+(face_height//2)
    # 0 --> top left --> -100 
    # 1 --> top right -->+100
    # 2 --> top right -->-100
    # 3 --> top left --> -100

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

    copy =  cv2.rectangle(copy, (x1, y1), (x2, y2), (255,0,255), 2)

    crop_img = image[y1:y2, x1:x2]

    cv2.imwrite(os.path.join(path , f"face{i+1}.jpeg"), crop_img)

    pad_copy =  cv2.rectangle(pad_copy, (px1, py1), (px2, py2), (255,0,255), 2)

    pad_crop_img = image[py1:py2, px1:px2]

    cv2.imwrite(os.path.join(path , f"pad_face{i+1}.jpeg"), pad_crop_img)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Original", 1200, 900)
# Displaying the image
cv2.imshow("Original", image)


cv2.namedWindow("Faces", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Faces", 1200, 900)
cv2.imshow("Faces", copy)
cv2.waitKey(0)

cv2.namedWindow("Padded Faces", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Padded Faces", 1200, 900)
cv2.imshow("Padded Faces", pad_copy)
cv2.waitKey(0)