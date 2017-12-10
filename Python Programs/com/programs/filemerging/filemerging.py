'''
Created on Dec 10, 2017

@author: VarunJoshi
'''


import time
import datetime
import glob2
import random
import string
import os
from com.programs.filehandling import loginhistory

def getfilename():
    now = datetime.datetime.now()
    file_name = now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"
    return file_name


def create_file():
    """create file and write time for 5 times after every 2 seconds"""
    with open("./"+getfilename(),"w+") as file :
        for each in range(5):
            file.write("Hello, the time is " + str(datetime.datetime.now())+"\n")
            time.sleep(2)

def merge_files(filenames):
    """read files and write its content to new file"""
    with open("./"+ getfilename(), "w") as filetowrite:
        filetowrite.write(str(datetime.datetime.now())+"\n")
        for eachfile in filenames:
            with open(eachfile,"r") as filetoread:
                filetowrite.write(filetoread.read()+"\n")
        filetowrite.write(str(datetime.datetime.now()))


def delete_text_files(filenames):
    """delete the text files and clear the directory"""
    for txtfile in filenames:
        os.remove(txtfile)



#delete all text files and clear the directory
filenames = glob2.glob("./*.txt")
delete_text_files(filenames)

#create files
for i in range(1,4):
    print('Creating file number '+str(i))
    create_file()#create file
filenames = glob2.glob("./*.txt")
  
#merge file
merge_files(filenames)
  
#End of program
print('========END=======')
