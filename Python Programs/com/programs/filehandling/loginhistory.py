'''
Created on Dec 10, 2017

@author: VarunJoshi
'''
import datetime

def create_login(fileobj):
    password = ''
    failed=0
    while password != "varun173":
        if failed < 6:
            password = input("enter the password")
            if password == "varun":
                print("Password is correct.\n")
                fileobj.write("Login Successful at "+str(datetime.datetime.now())+"\n")
                break
            else:
                failed+=1
                if(failed >= 3 and failed!=6):
                    print("You have "+str(6-failed)+'attempt left')
                fileobj.write("Unsuccessful login attempt at"+str(datetime.datetime.now())+'\n')
        else:
            print("Your account is locked")
            break
    fileobj.write("Total number of failed attempt "+str(failed))

# open the file 
fileobj = open("demo.txt",'a+')
#call the login function
create_login(fileobj)
