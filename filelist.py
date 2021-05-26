
import os
path = os.getcwd()+'\\Videos';
list = []
for e in os.walk(path):
    list = e[0]
print(list)
