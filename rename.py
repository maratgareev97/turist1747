def Rename()
	from os import listdir
	import os
	mass = listdir("/home/keinn/Neron_net/download_foto1")
	print(mass)
	srr = "/home/keinn/Neron_net/download_foto1/qww"
	d =0
	for i in mass:
		strr = srr+str(d)+'.png'
		srt = "/home/keinn/Neron_net/download_foto1/"+i
		print('old| ',srt,'new |',strr)
		d = d+1
		os.rename(srt,strr )
	d = 0
	print("^^^^^^^^^^^^^^^zero^^^^^^^^^^^^^^^")
	mass = listdir("/home/keinn/Neron_net/download_foto1")
	for i in mass:
		strr = "/home/keinn/Neron_net/download_foto1/"+str(d)+'.png'
		srt = "/home/keinn/Neron_net/download_foto1/"+i
		print('old| ',srt,'new |',strr)
		d = d+1
		os.rename(srt,strr )
		
