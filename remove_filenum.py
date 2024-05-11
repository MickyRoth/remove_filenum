# Remove filenumbers from filenames in cuurent directory

import os

files = []  # list of files
num = 0     # number of changed files

for fsobj in os.listdir():      # get list of files
    if os.path.isfile(fsobj) and fsobj[0].isdigit():   # if it's a numbered file
        files.append(str(fsobj)) 

print('Detected',len(files),'numbered files')

for filename in files:        # for each file
    newfilename = filename
    for i in range(len(filename)):
        if filename[i].isdigit() or filename[i]== ' ': # if the character is a number or a space
            newfilename = newfilename[1:]  # delete the first character
        else: break # if the character is not a number or a space, were done with the file
    try:
        os.rename(filename, newfilename)
        num+=1
    except Exception as e:
        print(e, 'could not rename', filename, 'to', newfilename)
        
print(f'Done! Changed {num} files')
