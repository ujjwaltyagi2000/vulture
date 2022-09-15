import face_recognition as fr
import cv2

image = fr.load_image_file(r"face-rec-v1\testing-dataset\aum.jpeg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
copy=image.copy()

face_locations = fr.face_locations(image)
print(face_locations)

for i in range(len(face_locations)):

    x1, y1, x2, y2 = face_locations[i][3]-50, face_locations[i][0]-200, face_locations[i][1]+50, face_locations[i][2]+50
    copy =  cv2.rectangle(copy, (x1, y1), (x2, y2), (255,0,255), 2)
# 0 --> top left --> -100 
# 1 --> top right -->+100
# 2 --> top right -->-100
# 3 --> top left --> -100
cv2.imshow("Original", image)
cv2.imshow("Faces", copy)
new_coordinates = [x1, y1, x2, y2]
print(f"New coordinates = {new_coordinates}")
crop_img = image[y1:y2, x1:x2]
cv2.imshow("cropped", crop_img)

cv2.waitKey(0)