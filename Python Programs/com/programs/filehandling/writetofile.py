'''
Created on Dec 10, 2017

@author: VarunJoshi
'''
file = open("numbers.txt", "w")
for i in range(0,50):
        file.write(str(i) + "\n")
file.close()