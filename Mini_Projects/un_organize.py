# Imports
import os

# Root directory for all the folders
root = "C:\\path\\to\\the\\files\\you\\want\\to\\sort"

def un_organize(main_folder):

	# Root path for this year
	path = root + "\\" + str(main_folder)
	# Getting the names of all the files in this folder
	files = os.listdir(path)
	# Folders list
	folders = []

	# Adding folders to the folders list
	for name in files:
		# For each file, check that it's not one of these files: 
		if name == "file_to_ignore_1" or name == "file_to_ignore_2" : 
			# If it is, go to the next file in the list
			continue
		folders.append(name)

	# For every folder in the folders list
	for folder in folders:
		# This folders path
		folder_path = path + "\\" + str(folder)
		# Getting all the files in the folder
		files_in_folder = os.listdir(folder_path)
		# For every file in the the current folder
		for file in files_in_folder:
			if file == "file_to_ignore_1" or file == "file_to_ignore_2" : 
				# If it is, go to the next file in the list
				continue
			# Path to the current location of the file
			old_path = folder_path + "\\" + file
			# Try moving the file out of the current folder
			try:
				# New path is: master_folder\file_name
				new_path = path + "\\" + file
				# Move the file from the old location to the new location
				os.rename(old_path, new_path)
			# You might get this exception, if so, it means the file already exists in the new folder
			# So simply continue to the next file in the files list
			except(FileExistsError):
				continue
		# Removing the empty folder when done
		os.rmdir(folder_path)

# Calling the organize function for all the folders
for folder in range(2009, 2018):
    un_organize(folder)