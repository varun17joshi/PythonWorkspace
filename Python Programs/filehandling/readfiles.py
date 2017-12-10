'''
Created on Dec 10, 2017

@author: VarunJoshi
'''
file = open("cars.txt", "r")
content = file.read()
file.close()

file = open("cars.txt", "r")
allcars = file.readlines()
file.close()

print(content)
print('-----------------------------------------------------------------------')
print('Length of each name')

for car in allcars:
    print(len(car))