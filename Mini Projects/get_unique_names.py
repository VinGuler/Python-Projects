# Imports
import os

### Notice this only works for Alphabeticly ordered file lists ###
### This is part of the order_files.py file, I just find this to be useful on it's own ###

# Root directory
root = "C:\\path\\to\\the\\files\\you\\want\\to\\sort"

# All the files in the Root directory
files = os.listdir(root)

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
        # Retrun the unique_names list
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

# Getting a short version of a recieved file name
def get_short(file):
        # Getting only the string that appears before the "." -> removing files' type
        f_name = file.split(".")[0]
        # Getting only the 1st part of the string before " -" or "-" char
        # You can choose how you want to to split the name
        if " -" in f_name:
                s_name = f_name.split(" -")[0]
        else:
                s_name = f_name.split("-")[0]
        return s_name

# Showing the unique_names  
def show_unique(unique_names):             
        print("_____unique_____")
        print("Unique names: " + str(len(unique_names)))
        for i in range(0, len(unique_names)):
                print(unique_names[i])        
