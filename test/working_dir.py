import os

dirpath = os.getcwd()
print("current path: " + dirpath)
dirname = os.path.basename(dirpath)
print("current dir: " + dirname)

os.chdir("..")
dirpath = os.getcwd()
print("now current path is: " + dirpath)

os.chdir("input")
dirpath = os.getcwd()
print("now current path is: " + dirpath)
