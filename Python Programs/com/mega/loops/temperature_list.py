'''
Created on Dec 10, 2017

@author: VarunJoshi
'''
temperatures=[10,-20,-289,100,-273.15]

def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
for t in temperatures:
    print(c_to_f(t))
    
response=''
while response != "y":
    response = input("please enter Y or y to exit").lower()
    if response == "y":
        exit
    else:
        print("Sorry !! Try Again!!")