import sys
import os

if os.path.isfile("/home/soumya/python/prac/new.txt"):
    print("Found")
    f1=open("new.txt","r")
    f1.seek(9,0)
    print(f1.tell())
    print(f1.readline())
    print(f1.tell())
   # for elem in f1:
       # elem=elem.rstrip("\n")
    #    print(elem)
    f1.close()

else:
    print("Not found")
    sys.exit(0)

