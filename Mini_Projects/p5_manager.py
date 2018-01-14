# A quick javascript.p5 Projects generator
# I work a lot with this javascript lib, so i created this tool

# Imports.
# I don't remember whether 'subprocess' is a basic lib or not
# So I wrapped it w/ try-except just in case...
import os
try:
	import subprocess
except:
	print("You need to install 'subprocess' for this to work.\nTry typing 'pip install subprocess' in the command prompt")

# Getting the projects name from user
project_name = input("Project Name : ")

# Stringifying the input
project_name = str(project_name)

# Basic text for the HTML file - links to scripts and an index.js file where the magic happnes
html_text = "<!DOCTYPE html>\n<html>\n\t<head>\n\t<meta charset='utf-8'>\n\t<title>"+project_name+"</title>\n\t<script src='https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.5.16/p5.js'></script>\n\t<script src='https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.5.16/addons/p5.sound.js'></script>\n\t<script src='https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.5.16/addons/p5.dom.js'></script>\n\t<script src='index.js'></script>\n\t<style> body {padding: 0; margin: 0;} </style>\n</head>\n<body></body>\n</html>"

# Basic text for the JS file - where the magic happens
js_text = "\nfunction setup(){\n\tcreateCanvas(600,600);\n}\n\nfunction draw(){\n\n}"

# Creating path
os.makedirs(project_name)
html_path = project_name+"/index.html"
js_path = project_name+"/index.js"

# Creating and writing to the HTML file
html_file = open(html_path, 'w')
html_file.write(html_text)
html_file.close()

# Creating and writing to the JS file
js_file = open(js_path, 'w')
js_file.write(js_text)
js_file.close()

# In case the user wants to immediatly start working on the project
# In Popen -> insert the path to your code editor
open_now = input("Open now? (y/n) : ")
if open_now == 'y':
	subprocess.Popen(['the path to your Code Editor', 
		html_path, js_path])