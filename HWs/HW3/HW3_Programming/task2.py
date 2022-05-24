import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image
plt.rcParams["figure.figsize"] = (12, 8.25)
image = Image.open('part2.jpg')
plt.imshow(image)
data = np.asarray(image)
shear = np.full((data.shape[0], data.shape[1] + (2 * data.shape[0]), 3), 255, dtype='uint8')
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        grayscale = (int(data[i][j][0]) + int(data[i][j][1]) + int(data[i][j][2])) / 3
        shear[i][2*i + j] = (grayscale, grayscale, grayscale)
image2 = Image.fromarray(shear)
plt.imshow(image2)
answer = np.full((data.shape[0], data.shape[1] + (2 * data.shape[0]), 3), 255, dtype='uint8')
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        answer[i][j + (2 * int(data.shape[0]))] = data[i][j]
for i in range(shear.shape[0]):
    for j in range(shear.shape[1]):
        answer[i][j] += shear[i][j]
image3 = Image.fromarray(answer)
plt.imshow(image3)
