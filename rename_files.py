'''
rename files batch
'''
import os
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir(r"C:\Users\KMaughan\Desktop\prank\prank")
	print(file_list)
	saved_path = os.getcwd()
	print ("Current working director is {}".format(saved_path))
	os.chdir(r"C:\Users\KMaughan\Desktop\prank\prank")
	remove = "0123456789"
	table=str.maketrans("","",remove)
	#(2) for each file, rename filename
	for file_name in file_list:
		file_name_bytes = str.encode(file_name)
		os.rename(file_name_bytes, file_name_bytes.translate(None, b"0123456789"))
	#os.chdir(saved_path)
		
	
	
rename_files()