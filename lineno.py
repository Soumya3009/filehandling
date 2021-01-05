line=0
word=0
char=0

f=open("mahi.txt","rb")
print(f.tell())
f.seek(-20,2)
print(f.tell())
for elem in f:
    line+=1
    word+=len(elem.split())
    char+=len(elem)
    #f.seek(-20,1)
    #print(f.tell())
    #print(f.readline())
    #print(elem)
f.close()

print(f"Line:{line} word:{word} Character:{char}")

