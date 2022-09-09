import os

name = os.path.isfile("testmain.py")

file = open(name+".html","w")

file.write("this is my first file")

file.close()
