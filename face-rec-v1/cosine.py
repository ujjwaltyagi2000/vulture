from PIL import Image
import numpy as np
from scipy import spatial


# open images

img1 = Image.open(r"deepface\dataset\img3.jpg")
img2 = Image.open(r"face-rec-v1\detected-faces\face3.jpeg")

# make sure images have same dimensions, use .resize to scale image 2 to match image 1 dimensions
# i am also reducing the shape by half just to save some processing power

img1_reshape = img1.resize((round(img1.size[0]*0.5), round(img1.size[1]*0.5)))
img2_reshape = img2.resize((round(img1.size[0]*0.5), round(img1.size[1]*0.5)))

# convert the images to (R,G,B) arrays

img_array1 = np.array(img1_reshape)
img_array2 = np.array(img2_reshape)

# flatten the arrays so they are 1 dimensional vectors

img_array1 = img_array1.flatten()
img_array2 = img_array2.flatten()

# divide the arrays by 255, the maximum RGB value to make sure every value is on a 0-1 scale

img_array1 = img_array1/255
img_array2 = img_array2/255

similarity = -1 * (spatial.distance.cosine(img_array1, img_array2) - 1)
print(similarity)