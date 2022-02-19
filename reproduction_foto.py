from os import listdir
import os
import cv2
mass = listdir("/home/keinn/Neron_net/download_foto2")
print(mass)
d = len(mass)
for i in mass:
	srt = "/home/keinn/Neron_net/download_foto2/"+str(d)+".png"
	image = cv2.imread("/home/keinn/Neron_net/download_foto2/"+i)
	flip_image = cv2.flip(image,1)
	cv2.imwrite(srt,flip_image)
	d=d+1