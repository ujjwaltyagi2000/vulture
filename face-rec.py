from tkinter.filedialog import askopenfilename # We will use this to give user the option to browse the image file
import face_recognition as fr
from tkinter import Tk
import cv2
import os # will help find file directories

# which file to analyse:
Tk().withdraw()

load_image = askopenfilename()

target_image = fr.load_image_file(load_image) # image file to be analyzed
target_encoding = fr.face_encodings(target_image)



# Searches for occurrences of this face:
def encode_faces(folder):
     
     list_people_encoding = []

     for filename in os.listdir(folder):

          known_img = fr.load_image_file(f'{folder}{filename}')
          known_encoding = fr.face_encodings(known_img)[0]

          print(len(fr.face_encodings(known_img)))

          list_people_encoding.append((known_encoding, filename))
          print(list_people_encoding)

     return list_people_encoding

# print(encode_faces())

def find_target_face():

     face_location = fr.face_locations(target_image)

     for person in encode_faces('dataset/'):

          encoded_face = person[0]
          filename = person[1]

          is_target_face = fr.compare_faces(encoded_face, target_encoding, tolerance = 0.55)

          print(f'{is_target_face} {filename}')

          if face_location:

               face_number = 0
               for location in face_location:
                    if is_target_face[face_number]:
                         label = filename
                         create_frame(location, label)

                    face_number += 1

def create_frame(location, label):
     
     top, right, bottom, left = location
     cv2.rectangle(target_image, (left,top), (right,bottom), (255,0,0), 2)
     cv2.rectangle(target_image, (left,bottom+20), (right,bottom), (255,0,0), cv2.FILLED)
     cv2.putText(target_image, label, (left + 3, bottom + 14), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255,255,255), 1)


def render_img():

     rgb_img = cv2.cvtColor(target_image, cv2.COLOR_BGR2RGB)
     cv2.imshow('Face Recognition', rgb_img)
     cv2.waitKey(0)

find_target_face()
render_img()



