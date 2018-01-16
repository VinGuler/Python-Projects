# Imports
import os

"""
IMPORTANT NOTE
Notice I do 2 loops, 1 is to create the directories, 
and the second is to organize the files in them.
"""
# Root directory for all the folders
root = "C:\\path\\to\\the\\files\\you\\want\\to\\sort"
""" 
The orgnizing funciton
@params : folder_name(str) -> The folder to organize the files in
"""
def organize(folder_name):
    # Root path for this year
    path = root + "\\" + str(folder_name)
    # Getting the names of all the files in this folder
    files = os.listdir(path)
    # After all the directories are created,
    # Go over all the files
    for f in files:
        # For each file, check that it's not one of these files: 
        if f == "file_to_ignore_1" or f == "file_to_ignore_2" : 
            # If it is, go to the next file in the list
            continue
        # Path to the current location of the file - needed for os.rename()
        old_path = path + "\\" + f
        # Get the part of the name before "." <- exculiding the files' type
        f_name = f.split(".")[0].split("-")[0].rstrip()
        # New path for the new folder created with the files' name
        new_dir = path + "\\" + f_name
        # Printing the new_path to see it worked properly 
        print(new_dir)
        # Try crating the new directory (folder)
        try:
            os.mkdir(new_dir)
        # Might get this if the folder already exists, 
        # simply continue to the next file
        except(FileExistsError):
            pass
        # Try moving the file into it's new folder created in create_dirs(f, cp) function 
        try:
            # New path is: current_folder_path\file_name\file_name.type
            new_path = new_dir + "\\" + f
            # Move the file from the old location to the new location
            os.rename(old_path, new_path)
        # You might get this exception, if so, it means the file already exists in the new folder
        # So simply continue to the next file in the files list
        except(FileExistsError):
            continue

    # Checking to see this worked -> printind the directories in this folder
    print(os.listdir(path))

# Calling the organize function for all the folders
for folder in range(2009, 2018):
    organize(folder)
