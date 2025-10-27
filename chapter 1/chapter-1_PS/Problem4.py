# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os
directry_path = '/New folder'

content = os.listdir(directry_path)

# print(content) give result in this formate ['Additional', 'OneNote', 'plot', 'software']

for item in content:
    print(item)       

# give answer in this formate
# Additional
# OneNote
# plot
# software