import os
from PIL import Image
import matplotlib.pyplot as plt

datapath = "./dataset/cats_and_dogs_filtered/"
for image_type in ["train/", "validation/"]:
	for image_class in ["cats/", "dogs/"]:
		for file in os.listdir(datapath + image_type + image_class):
			with Image.open(datapath + image_type + image_class + file) as img:
				width, height = img.size
				plt.scatter(width, height)

		plt.title(image_type + image_class + " images width and height")
		plt.xlabel("width")
		plt.ylabel("height")
		plt.show()
