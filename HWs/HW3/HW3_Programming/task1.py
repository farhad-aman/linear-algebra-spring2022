import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image
plt.rcParams["figure.figsize"] = (12, 8.25)
image = Image.open('part1.jpg')
plt.imshow(image)
data = np.asarray(image)
red = [0 for i in range(256)]
green = [0 for i in range(256)]
blue = [0 for i in range(256)]
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        red[data[i][j][0]] += 1
        green[data[i][j][1]] += 1
        blue[data[i][j][2]] += 1
labels = np.arange(256)
width = 0.5
fig, ax = plt.subplots()
pred = ax.bar(labels, red, width, label='Red', color='red')
ax.set_title('Red')
fig, ax = plt.subplots()
pgreen = ax.bar(labels, green, width, label='Green', color='green')
ax.set_title('Green')
fig, ax = plt.subplots()
pblue = ax.bar(labels, blue, width, label='Blue', color='blue')
ax.set_title('Blue')
