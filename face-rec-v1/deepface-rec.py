from deepface import DeepFace

# FACE VERIFICATION:
img_1_path = r"detected-faces\pad_face7.jpeg"
img_2_path = r"testing-dataset\ujjwal.jpeg"

model_name = 'VGG-Face' #Models: Facenet, VGG-Face, ArcFace

response = DeepFace.verify(img1_path=img_1_path, img2_path=img_2_path, model_name=model_name, prog_bar=True)
print(response)
# faces = DeepFace.detectFaces(img_1_path)







