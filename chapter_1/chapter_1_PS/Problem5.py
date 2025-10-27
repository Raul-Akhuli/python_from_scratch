# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

# specify the directory you want to list 
directry_path = '/New folder'

# List all files and directory in one specified path 
content = os.listdir(directry_path)

# print(content) give result in this formate ['Additional', 'OneNote', 'plot', 'software']


# print each file and directroy name
for item in content:
    print(item)       

# give answer in this formate
# Additional
# OneNote
# plot
# software