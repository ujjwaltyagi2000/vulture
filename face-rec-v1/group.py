import face_recognition

picture_of_me = face_recognition.load_image_file(r"face-rec-v1\testing-dataset\ujjinb.jpeg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file(r"face-rec-v1\testing-dataset\techudyam.jpeg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[2]
print(len(face_recognition.face_encodings(unknown_picture)))

# Now we can see the two face encodings are of the same person with `compare_faces`!

result = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
print(result)

if result == True:

    print("It's a picture of me!")
else:
    print("It's not a picture of me!")