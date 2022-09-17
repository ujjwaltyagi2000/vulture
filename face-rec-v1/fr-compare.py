import face_recognition

picture_of_me = face_recognition.load_image_file(r"face-rec-v1\testing-dataset\ujjinb.jpeg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file(r"face-rec-v1\testing-dataset\tm.jpeg")

faces = len(face_recognition.face_encodings(unknown_picture))
print(faces)

for face in range(0,faces):
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[face]
    result = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding, tolerance = 0.55)
    print(result)

    if result[0] == True:

        print("It's a picture of me!")
        print(f"I am face number: {face+1}")

    else:

        print("It's not a picture of me!")


# Now we can see the two face encodings are of the same person with `compare_faces`!

# result = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
# print(result)

# if result == True:

#     print("It's a picture of me!")
# else:
#     print("It's not a picture of me!")