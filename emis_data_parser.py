import os
import json


# Variables
dataFolder = "C://Users//User//git//exa-data-eng-assessment//data"

fileList = os.listdir(dataFolder) # fileList is list of file names in the folder
print("files found:", len(fileList))


for fileName in fileList:
    fileHandle = open(dataFolder+"//"+fileName, "r")
    for line in fileHandle:
        print(line)
    fileHandle.close()
    cont = input("nextFile?")
    if (cont != "no"):
        continue
    else:
        break
    
