# Imports.
# You need to install openpyxl lib for this script to work
from openpyxl import load_workbook
import os

"""
IMPORTANT NOTE
Notice I do 2 loops, 1 is to create the directories, 
and the second is to organize the files in them.

Also -> I have not fully tested it yet...

Also2 -> this was made for a very specific file tree...
"""

# Root directory for all the folders
root = "C:\\path\\to\\the\\files\\you\\want\\to\\sort"

# Loading the xlsx file 
file = load_workbook(filename='index.xlsx')
# Picking the sheet to work on
worksheet = file['files'] 

# The orgnizing funciton
def organize(row, root_folder):
        # Variables for the xlsx sheet
        # this_row -> Counter for the current row (in the xlsx sheet)
        this_row = row
        # writing current root_folder in the 1s column (also 1st row of the root_folder)
        worksheet['A'+str(this_row)] = root_folder
        # Root path for this root_folder
        path = root + "\\" + str(root_folder)
        # Getting the names of all the files in this folder
        files = os.listdir(path)

        # Creating directories based on the files in this folder
        # See create_dirs(fs) function
        create_dirs(files, path)
        
        # After all the directories are created,
        # Go over all the files
        for f in files:
                # For each file, check that it's not one of these files: 
                if f == "file_to_ignore" or f == "file_to_ignore_2":  
                        # If it is, go to the next file in the list
                        continue
                # Get the shortened version of the files' name
                shortened_name = get_short(f)
                # Get the part of the name before "." <- exculiding the files' type
                f_name = f.split(".")[0]
                # Write the files' name in the xlsx sheet
                # See write_to_sheet(r, f) function
                # Also incremet row counter, to go to the next row in the xlsx
                worksheet['B'+str(this_row)] = f_name
                this_row += 1

                # Path to the current location of the file - needed for os.rename()
                old_path = path + "\\" + f

                # Try moving the file into it's new folder created in create_dirs(f, cp) function 
                try:
                        # New path is: current_folder_path\file_name\file_name.type
                        new_path = path + "\\" + shortened_name + "\\" + f
                        # Move the file from the old location to the new location
                        os.rename(old_path, new_path)
                # You might get this exception, if so, it means the file already exists in the new folder
                # So simply continue to the next file in the files list
                except(FileExistsError):
                        continue
        # Checking to see this worked -> printind the directories in this folder
        print(os.listdir(path))
        # Return the next row -> Needed for the final loop
        # This way I know where to start writing the next root_folder into the xlsx file
        return this_row + 1

# Creating the folders for the files
# Recieves a files list
def create_dirs(files, current_path):
        # Current path of the files, getting it from the organize(r, y) functino
        path = current_path

        # Getting the unique names for all the files
        unique_names = get_unique_names(files)
        
        # For every file in the list
        for name in unique_names:            

                # New path for the new folder created with the files' name
                new_path = path + "\\" + name
                # Printing the new_path to see it worked properly 
                print(new_path)
                # Try crating the new directory (folder)
                try:
                        os.mkdir(new_path)
                # Might get this if the folder already exists, 
                # simply continue to the next file
                except(FileExistsError):
                        continue

# Getting the unique file names from the files list
def get_unique_names(files):     
        # Unique names for the files
        # If a shortened name apears twice or more on the short_names list,
        # it will appear only once on the unique_names list
        unique_names = []

        # All the files' shortened names
        short_names = get_short_names(files)
        
        # Creating the unique_names list
        for f_name in short_names:

                # Adding first file name to unique_names
                if len(unique_names) == 0:
                        unique_names.append(f_name)
                # If there are any names in the unique_names list
                else:
                        # If the files' short name is the same as the last name in the unique_names,
                        # Go to the next word in the short_names list
                        if f_name == unique_names[len(unique_names)-1]:
                                continue
                        # If the short names is not on the unique_names list, add it
                        else:
                                unique_names.append(f_name)

        return unique_names

# Returns a list of the short names of a recieved files list
def get_short_names(files):
        # All the files shortened names
        short_names = []

        # Creating the short_names list
        for f in files:
                # For each file, check that it's not one of the files you don't want: 
                if f == "file_to_ignore" or f == "file_to_ignore_2": 
                        # If it is, go to the next file in the list
                        continue   
                # Getting only the short version of the file name
                short_name = get_short(f)
                # Adding the shortened name to the short_names list
                short_names.append(short_name)
        # Return the short_names list
        return short_names

# Getting the short version of a recieved file name
def get_short(file):
        # Getting only the string that appears before the "."
        f_name = file.split(".")[0]
        # Getting only the 1st part of the string before " -" or "-" char
        if " -" in f_name:
                s_name = f_name.split(" -")[0]
        else:
                s_name = f_name.split("-")[0]
        return s_name

# Calling the organize function for all the folders
# folder names are numbers (like "1", "2", "3")
current_row = 0
for folder in range (2009, 2011):
        # Put the first folder on the second row in the xlsx file
        if current_row == 0:
                current_row = organize(2, folder)
        # Then use the current_row variable as the starting row for the next folder
        else:
                organize(current_row, folder)

# Saving the changes in the xlsx file
file.save("index.xlsx")
