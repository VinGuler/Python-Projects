# Getting an e-mail list from an EXCEL file { xlsx / xls }

# Importing the lib
try:
	from openpyxl import load_workbook
except:
	print("You need to install 'openpyxl' for this to work.\nTry typing 'pip install openpyxl' in the command prompt")

# Pretty self explanatory
mail_list = []

# This file is where the emails will be written to
mail_file = open("Mails.txt", 'w')

# This file is the original xls/x file
f = load_workbook('your-file-name.xlsx')

# This is the column you'd like to extract the data from
costumers = f['costumers']

# Going through all the rows in the selected column
for i in range(4, 133):
	# Excluding you company mails from the list 
    if "@your-company-name.whatever" in costumers['B'+str(i)].value:
        continue
    else:
    	# Adding each mail, in each row, into the mail_list
        mail_list.append(costumers['B'+str(i)].value)

# How many mails have we collected
total_mails = len(mail_list)

# Here you go through the mail_list (Collected mail addresses) 
# and writing them all to the 'Mails.txt' file
for i in range(total_mails):
	# This if statement if for simplisity...
	# All mails will have a semicolon after them EXCEPT the last one
    if i != len(mail_list)-1:
        mail_file.write(mail_list[i].lower() + "; ")
    else:
        mail_file.write(mail_list[i].lower())

# Writing to 'Mails.txt' the total amount of mail adresses             
mail_file.write("\n\nTotal mails : " + str(total_mails) + "\n")

# Closing the 'Mails.txt' file
mail_file.close()

