import os, sys, shutil
import pathlib
from os import path
from os.path import exists, isfile, getmtime, join as pjoin
from shutil import copyfile

#FUNCTIONS
#function to rename a series of files in numerical order
def renameNumerically(passedFiles, maximum):
    i = 0
    x = len(passedFiles) - 1
    while i <= x:
        if maximum <= 1000:
            for file in passedFiles:
                extension = pathlib.Path(file).suffix
                prefix = ""
                newNameNum = sequenceStart + i
                if i < 10:
                    prefix = "00"
                elif i < 100:
                    prefix = "0"
                newNameStr = prefix + str(newNameNum) + extension
                os.rename(file, newNameStr)
                i += 1
        elif maximum <= 10000:
            for file in passedFiles:
                extension = pathlib.Path(file).suffix
                prefix = ""
                newNameNum = sequenceStart + i
                if i < 10:
                    prefix = "000"
                elif i < 100:
                    prefix = "00"
                elif i < 1000:
                    prefix = "0"
                newNameStr = prefix + str(newNameNum) + extension
                os.rename(file, newNameStr)
                i += 1
        else:
            print("error")


print("\t**********************************************")
print("\t***  Welcome to the filename management application  ***")
print("\t**********************************************")
print("You will have several options. But first, please enter a directory you wish to execute in.")

#get directory to be worked in, make sure it's valid, and the user is happy with it
happy = "n"
while happy == "n":
    directory = input("Directory:")
    valid = path.exists(directory)
    if valid:
        os.chdir(directory)
        print("Directory is: " + os.getcwd())
        files = os.listdir(directory)
        print("This directory contains the following files:")
        i = 0
        for file in files:
            print(str(i) + ". " + file + "\n")
            i += 1
        print("Is this the folder you wish to execute in?")
        happy = input("y for yes, n for no: ")
    else:
        print("That is not a valid filepath.")
        happy = "n"

print("What do you wish to do in the directory?")
print("1. Change all file names to a sequential series of numbers, up to 1000 files.")
print("2. Change all file names to a sequential series of numbers, up to 10,000 files.")
print("3. Remove duplicate files.")
print("4. Strip all filenames of certain characters.")
print("5. Delete all files containing a designated string of characters.")

#determine the function the user wishes to execute
actionInput = input("Select 1, 2, 3, 4, or 5: ")

if actionInput == "1" or actionInput == "2":    
    #Change all file names to a sequential series of numbers. 1 means a max of 1000 files. 2 means a max of 10000 files

    #get variables ready
    list_filesToExclude = []
    movementOption = 0 #rename is 1, move is 2
    sequenceStart = 0

    print("Selected: Rename all files in numerical sequence.")

    #get the first number in the sequence. This will correspond to the first file in the working directory. 
    sequenceStartInput = input("Select the first number in the sequence: ")
    if not sequenceStartInput.isnumeric():
        print("Error")
    sequenceStart = int(sequenceStartInput)
    if sequenceStart < 0:
        print("error")

    #get any files, by index, that the user wishes excluded from the operation. Folders will be excluded automatically. 
    print("Are there any files you wish to exclude from this operation? Enter the number of each file, separated by a space. If no files are to be excluded, enter 'n'.")
    filesToExcludeString = input("File numbers: ")
    if filesToExcludeString != "n":
        filesToExclude = filesToExcludeString.split()
        #remove files from list that should be excluded
        for file in files:
            i = files.index(file)
            if str(i) in filesToExclude:
                del files[i]
    for file in files:
        i = files.index(file)
        if os.path.isdir(file):
                del files[i]
    
    #check if the user wants the items in the directory sorted alphabetically, if they aren't already.
    print("Check that the files in this directory are ordered alphabetically, or however you want them.")
    sort = input("Do you want to perform alphabetization on this directory? y or n: ")
    if sort == "y" or sort == "Y":
        files.sort()
    else:
        print("No sort selected.")

    #determine if the user wants the existing files renamed, or if they should be copied to a new location and then the copies renamed
    print("Do you want the files to be renamed? Or do you want copies made with the new names? These will be placed in a new folder within this directory.")
    option = input("Enter 'rename' or 'move': ")
    if option == "rename" or option == "Rename" or option == "RENAME":
        if actionInput == "1":
            renameNumerically(files, 1000)
        elif actionInput == "2":
            renameNumerically(files, 10000)
    elif option == "move" or option == "Move" or option == "MOVE":
        folderName = input("Enter a name for the new folder: ")
        if not folderName:
            print("error")
        else:
            newPath = os.path.join(directory, folderName)
            os.mkdir(newPath)
            #copy files to new directory
            for file in files:
                shutil.copy(file, newPath)
            os.chdir(newPath)
            copiedFiles = os.listdir(os.getcwd())
            if actionInput == "1":
                renameNumerically(copiedFiles, 1000)
            elif actionInput == "2":
                renameNumerically(copiedFiles, 10000)
    else:
        print("error")        

elif actionInput == "3":
    #Remove duplicate files
    #Inform user of what will happen, and confirm their desire to proceed
    print("Selected: Remove duplicate files. ")
    print("Any files with '(1)', '(2)', etc (up to '(9)') or 'copy' in the name will be deleted. Is this ok?")
    confirm = input("y/n: ")
    if confirm == "y" or confirm == "yes":
        #check each filename, and if the name contains one of the strings that are typically added to duplicate files in the same directory, the duplicate file is deleted. 
        for file in files:            
            print(pathlib.Path(file).stem)
            if "(1)" in pathlib.Path(file).stem:
                os.remove(file)
            elif "(2)" in pathlib.Path(file).stem:
                os.remove(file)
            elif "(3)" in pathlib.Path(file).stem:
                os.remove(file)
            elif "(4)" in pathlib.Path(file).stem:
                os.remove(file)
            elif "(5)" in pathlib.Path(file).stem:
                os.remove(file)
            elif "(6)" in pathlib.Path(file).stem:
                os.remove(file)
            elif "(7)" in pathlib.Path(file).stem:
                os.remove(file)
            elif "(8)" in pathlib.Path(file).stem:
                os.remove(file)
            elif "(9)" in pathlib.Path(file).stem:
                os.remove(file)
            elif "copy" in pathlib.Path(file).stem:
                os.remove(file)
            elif "COPY" in pathlib.Path(file).stem:
                os.remove(file)
            elif "Copy" in pathlib.Path(file).stem:
                os.remove(file)
        print("Operation complete.")
    else:
        print("cancelling action")

elif actionInput == "4":
    #Strip all filenames of certain characters
    #get variables ready
    stringToStrip = ""
    list_filesToExclude = []
    trimOrWhole = 0
    print("Selected: Strip filenames of designated characters or strings.")
    print("What characters or strings should be stripped from the filenames?")
    stringToStrip = input("The whole text block to strip: ")

    for file in files:
        currentName = pathlib.Path(file).stem
        newName = currentName.strip(stringToStrip)
        os.rename(file, newName)

elif actionInput == "5":
    #delete all files containing a certain character string
    stringToDelete = input("Enter filter string: ")
    print("This operation will delete all files whose names contain the string " + stringToDelete + ". Is this ok?")
    confirm = input("y/n? ")
    if confirm == "y" or confirm == "yes" or confirm == "YES" or confirm == "Yes":
        for file in files:
            if stringToDelete in pathlib.Path(file).stem:
                os.remove(file)
    else:
        print("Cancelling...")
    print("Deletion complete. Are there more strings you wish to filter out?")
    more = input("y/n? ")
    while more == "y":
        diff = input("Are these files in a different directory?")
        if diff == "y" or diff == "yes" or diff == "YES" or diff == "Yes":
            newDir = input("Enter new directory: ")
            os.chdir(newDir)
            print("Now working in: " + os.getcwd())
            files = os.listdir(os.getcwd())
        stringToDelete = input("Enter filter string: ")
        print("This operation will delete all files whose names contain the string " + stringToDelete + ". Is this ok?")
        confirm = input("y/n? ")
        if confirm == "y" or confirm == "yes" or confirm == "YES" or confirm == "Yes":
            for file in files:
                if stringToDelete in pathlib.Path(file).stem:
                    os.remove(file)
        else:
            print("Cancelling...")
        print("Deletion complete. Are there more strings you wish to filter out?")
        more = input("y/n? ")

else:
    print("Bad input")





