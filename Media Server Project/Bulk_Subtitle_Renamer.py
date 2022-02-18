import os
import re

folders = [] #Enter the names of sub directories containing subtitles to be renamed

#The function takes in the string containing the sub string or character to be replaced, the old character and the replacement as new and the nth occurence in the string
#It then splits the string in 2 at the location of the character or sub string to be replaced and does so by subtracting 1 from the nth occurence to give the index
#The old value is replaced with the new value only once as indicated by the 1 on line 13 and the split string is then rejoined as newString which is returned
def replacechar(string, old, new, n):
    where = [m.start() for m in re.finditer(old, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(old, new, 1)
    newString = before + after
    return newString

#Iterate through each directory name in the folders list
for folder in folders:

    directory = " mainDirectoryLocation  " + folder
    #Iterate through each file present in the current sub directory of the iteration in the main for loop
    for filename in os.listdir(directory): 
        #If the file name ends with srt, indicating that it is a subtitle file, the following should happen
        if filename.endswith(".srt"): 
            #Assign the path of file to be renamed to old_name
            old_name = r"mainDirectoryLocation" + folder + "/" + filename
            n = filename.count('oldChar') #Assign the number of occurences of the character to be changed to n,the number can be reduced if you do not wish to change only the last occurence of the character in the string
            n_filename = replacechar(filename, "oldChar", "newChar", n)  #Assign the return value to n_filename
            #Assign the new path of renamed file to new_name
            new_name = r"mainDirectoryLocation" + folder + "/" + n_filename

            if os.path.isfile(new_name): #If there already exuxts a file in the directory with the same name we are alerted
                print("The file already exists")
            else:
                # Else, Rename the file
                os.rename(old_name, new_name)
            continue      

        else:
            continue #Continue if the file does not end in extension srt