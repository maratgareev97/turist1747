def main():
	import shutil
	import os	
	data_dir = '/home/keinn/Neron_net/PetImages/Cat'
	source_dir2 = '/home/keinn/Neron_net/PetImages/Dog'
	#data_dir = '/home/keinn/Neron_net/p2/Cat'
	#source_dir2 = '/home/keinn/Neron_net/p2/Dog'
	# Каталог с данными для обучения
	train_dir = 'train'
	# Каталог с данными для проверки
	val_dir = 'val'
	# Каталог с данными для тестирования
	test_dir = 'test'
	# Часть набора данных для тестирования
	test_data_portion = 0.15
	# Часть набора данных для проверки
	val_data_portion = 0.15
	# Количество элементов данных в одном классе
	nb_images = 12500 #12500
	############################################
	def create_directory(dir_name):
	    if os.path.exists(dir_name):
		shutil.rmtree(dir_name)
	    os.makedirs(dir_name)
	    os.makedirs(os.path.join(dir_name, "cats"))
	    os.makedirs(os.path.join(dir_name, "dogs"))    
	def copy_images(start_index, end_index, source_dir1,source_dir2, dest_dir,t):
	    for i in range(start_index, end_index):
		try:
	    	    if(t=='cat'):
	    	        print("cat")
	    	        shutil.copy2(os.path.join(source_dir1,str(i) + ".jpg"), os.path.join(dest_dir, "cats"))
	    	    if(t=='dog'):
	    	        print('dog')
	    	        shutil.copy2(os.path.join(source_dir2,str(i) + ".jpg"), os.path.join(dest_dir, "dogs"))
		except:print("error")
	#################################
	start_val_data_idx = int(nb_images * (1 - val_data_portion - test_data_portion))
	start_test_data_idx = int(nb_images * (1 - test_data_portion))
	print(start_val_data_idx)
	print(start_test_data_idx) 
	#########################################################
	mas_name_dir_in_dir = ['cats',"dogs"]


	##############################################################################################
	create_directory(train_dir,)                                                                  #
	create_directory(val_dir)                                                                    #  
	create_directory(test_dir)                                                                   #  
	copy_images(0, start_val_data_idx, data_dir,source_dir2, train_dir,'cat')                    #
	copy_images(0, start_val_data_idx, data_dir,source_dir2, train_dir,'dog')                    #
	copy_images(start_val_data_idx, start_test_data_idx, data_dir,source_dir2, val_dir,'cat')    #
	copy_images(start_val_data_idx, start_test_data_idx, data_dir,source_dir2, val_dir,'dog')    #
	copy_images(start_test_data_idx, nb_images, data_dir,source_dir2, test_dir,'cat')            #  
	copy_images(start_test_data_idx, nb_images, data_dir,source_dir2, test_dir,'dog')            #  
	##############################################################################################






















  
