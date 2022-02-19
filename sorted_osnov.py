def sorted_osnov():
	import shutil
	import os
	# Часть набора данных для тестирования
	test_data_portion = 0.15
	# Часть набора данных для проверки
	val_data_portion = 0.15
	##############################################################################################
	def create_directory(dir_name,name):
	    if os.path.exists(dir_name):
		shutil.rmtree(dir_name)
	    os.makedirs(dir_name)
	    for i in name:
		os.makedirs(os.path.join(dir_name,i))  
	##############################################################################################
	def copy_images(start_index, end_index, source, dest_dir,t):
	    for i in range(start_index, end_index):
		try:shutil.copy2(os.path.join(source,str(i) + ".jpg"), os.path.join(dest_dir,t))
		except:print("error")
	##############################################################################################
	source_dir_mas = ['/home/keinn/Neron_net/PetImages/Cat','/home/keinn/Neron_net/PetImages/Dog','/home/keinn/Neron_net/download_foto1']  #имена старых директорий(загруженных из интернета)
	mas_name_dir_in_dir = ["cats","dogs","pushkin"]                                                                                        #имена новых папок в директории новой
	mas_end_dir = ['train2','val2','test2']                                                                                                   #именна новых директорий
	###############################################################################################
	#создание директорий                                                                          #                                
	for dirr in mas_end_dir:                                                                      #
	    create_directory(dirr,mas_name_dir_in_dir)                                                #
	############################################################################################### 
	#нахождение минимального кол-во фото в директориях начальных
	mas_min = []
	for i in source_dir_mas:
	    files = os.listdir(path=i)
	    mas_min.append(len(files))
	nb_images = min(mas_min)                                                                      #
	###############################################################################################
	#создание индексов копирования                                                                #
	start_val_data_idx = int(nb_images * (1 - val_data_portion - test_data_portion))              #
	start_test_data_idx = int(nb_images * (1 - test_data_portion))                                #
	print(start_val_data_idx)                                                                     #
	print(start_test_data_idx)                                                                    #
		                                                                                      #
		                                                                                      #
	############################################################################################### 
	#копирование фото в директории и папки находящиеся в них                                      #
	count = 0                                                                                     # 
	for source in source_dir_mas:                                                                 #
	    for dest_dir in mas_end_dir:                                                              #
		copy_images(0, start_val_data_idx,source,dest_dir,mas_name_dir_in_dir[count])         #
	    count = count+1                                                                           # 
	###############################################################################################






















	  
