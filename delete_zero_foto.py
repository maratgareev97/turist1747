def delete_zero_foto():
	from os import listdir
	import os
	import cv2
	mass = listdir("/home/keinn/Neron_net/download_foto1")
	print(mass)
	d = len(mass)
	for i in mass:
		srt = "/home/keinn/Neron_net/download_foto1/"+str(d)+".png"
		image = cv2.imread("/home/keinn/Neron_net/download_foto1/15.png")
		L_im1 = len(image)
		L_im2 = len(image[1])
		print(L_im1,L_im2)



		'''
		mas = []
		for i in range(L_im1):
			x = image[i]
			summ = 0
			for j in range(L_im2):
				y = x[j]
				summ = summ+y
			summ = summ/L_im2
			mas.append(summ)
		print(mas)	
		break
		d=d+1
