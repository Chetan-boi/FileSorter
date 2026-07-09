# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import pathlib
import sys
import shutil

def moveToFolder(file, extension):
   source = "input/" + file
   if (extension == "jpeg" or extension == "jpg"):
       destination = "output/image/"

   else:
    destination = "output/" + extension + "/"

   shutil.move(source, destination)

def identifyFileType(fileName):
    return fileName.split('.')[-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = [f for f in os.listdir("input") if os.path.join("input",f) and not f.startswith(".")]
    for f in file:
        extension = identifyFileType(f)
        moveToFolder(f,extension)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
