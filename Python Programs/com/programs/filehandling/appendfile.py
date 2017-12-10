'''
Created on Dec 10, 2017

@author: VarunJoshi
'''
# file = open('numbers.txt', 'a')
# for i in range(51,100):
#     file.write(str(i)+'\n')
# file.close()

with open("numbers.txt","a+") as file:
    file.write('1'+'\n')