import sys
import os

if len(sys.argv) == 1:
    print("What's going on here buddy?\nYou need to give me a name...\nplease")
    exit() 

if len(sys.argv) >2:
    print("Woah there cowbow!\nThis is UNIX!\nLet's avoid spaces in directory names, shall we?\nDon't try to be smart by putting the whole thing in quotes either!")
    exit()

if ' ' in maindir:
    print("Okay, look smart guy/gal/non-binary pal.\nThis is UNIX.\nYou REALLY shouldn't be putting spaces in your directory names!!!\nBE BETTER!")
    exit()
 
current_path = os.path.abspath(os.getcwd())

maindir = sys.argv[1]

newpath = os.path.join(current_path, maindir) 

subdirs = ["VCFs","GFFs","misc","data"]

print("Making directory and subdirectories for: {0}".format(maindir))

for i in subdirs:
    if not os.path.exists(os.path.join(newpath,i)):
        os.makedirs(os.path.join(newpath,i))
    else:
        print("{0}/{1} already exists.".format(maindir,i))
        
###
