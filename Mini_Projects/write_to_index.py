from openpyxl import load_workbook
import os

# Root directory for all the folders
root = "C:\\Users\\webmaster\\Desktop\\Masters"

# Loading the xlsx file 
file = load_workbook(filename='index.xlsx')
# Picking the sheet to work on
worksheet = file['files']

def write_to_index(r, root_folder):
	# Current row counter
	row = r

	# writing current year in the 1s column (also 1st row of the year)
	worksheet['A'+str(row)] = root_folder

	# Root path for this folder
	path = root + "\\" + str(root_folder)
	# Getting the names of all the files in this folder
	files = os.listdir(path)

	for i in range(0, len(files)):
		f = files[i]
		# For each file, check that it's not one of these files: 
		if f == ".DS_Store" or f == "Thumbs.db" : 
			# If it is, go to the next file in the list
			continue 

		# Getting the names of all the files in this folder
		f_name = f.split(".")[0]

		# Write the files' name in the xlsx sheet
		# Also incremet row counter, to go to the next row in the xlsx
		worksheet['B'+str(row)] = f_name
		row += 1

	# Returning the row at which the function finished, and addind 1 for space 
	return row+1

# Setting the current_row to the starting value (2 in this case)
current_row = 2
# Going through all the file, 
# writing them in their right places in the index.xslx file
for i in range (2009, 2018):
	current_row = write_to_index(current_row, i)

# Saving the changes in the xlsx file
file.save("index.xlsx")