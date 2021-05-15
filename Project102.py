import os

OrignalFileName = input("enter file path with file name: ")
NewFileName = input('enter the file path with new file name: ')

os.rename(OrignalFileName,NewFileName)

print("File renamed successfully, Please go and check whether it the name is Changed")