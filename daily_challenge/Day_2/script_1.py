#!/usr/bin/env python

import os

#===============================
# Current Working Directory
#===============================

cwd=os.getcwd()

print("Current working directory:",cwd)
print()

#=======================================================================================

#=========================================
# Changing the current working directory
#=========================================

def change_dir():

    print("Current working directory:")
    print(os.getcwd())
    print()

change_dir()
os.chdir("../")
change_dir()

#====================================================================================

#===============================
# Creating directory
#===============================


directory_name = "scripts"
parent_directory= os.getcwd()
new_path=os.path.join(parent_directory, directory_name)


print("Let's create a new directory named:", directory_name)

os.mkdir(new_path)

print("Directory created:")

print(os.getcwd())