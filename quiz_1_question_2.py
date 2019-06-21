
import os
from os import listdir

path = "/Users/ersi/Desktop/CSC599/"

for i in range(3):
	f = open("file_" + str(i) + ".txt","w+")
	f.close()

for i in range(3):
	f = open("file_" + str(i) + ".bak" , "w+")
	f.close()

for i in range(3):
	f = open("file_" + str(i) + ".py" , "w+")
	f.close()

for file in listdir(path):
	if file.endswith(".bak"):
		os.remove(path + file)

for file in listdir(path):
	if file.endswith(".txt"):
		os.rename(file,"new_"+file)

for file in listdir(path):
	if file.endswith(".py"):
		if len(open(path + file).readlines()) < 10:
			os.rename(file, "short_" + file)
		else:
			os.rename(file, "long_" + file)