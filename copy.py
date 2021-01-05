f1=open("mahi.txt","r")
f2=open("copy.txt","w")
f3=open("new.txt","a")

res=f1.read().upper()
f2.write(res)
f3.write(res)
f1.close()
f2.close()
f3.close()

