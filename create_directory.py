import sys
import os


current_path = os.path.abspath(os.getcwd())

if len(sys.argv) == 1:
    print("What's going on here buddy? You need to give me a name... cancelling script")
    exit() 

if len(sys.argv) >2:
    print("Woah there cowbow! This is UNIX! Let's avoid spaces in directory names, shall we? Don't try to be smart by putting the whole thing in quotes either!")
    exit()


print("making directory and subdirectories for: {0}".format(sys.argv[1]))
newpath = os.path.join(current_path, sys.argv[1]) 
vcfs = os.path.join(newpath,"VCFs")
gffs = os.path.join(newpath,"GFFs")
misc = os.path.join(newpath,"misc")
DATA = os.path.join(newpath,"data")

if not os.path.exists(vcfs):
    os.makedirs(vcfs)
if not os.path.exists(gffs):
    os.makedirs(gffs)
if not os.path.exists(misc):
    os.makedirs(misc)
if not os.path.exists(DATA):
    os.makedirs(DATA)
