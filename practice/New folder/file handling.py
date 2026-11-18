# file handling(#for open and reading file)
f=open("rushda.txt","r")
print(f.read())
#now opening file using path
f=open(r"D:\rushda\python\practice\New folder\rushda.txt")
print(f.read())
#using with (so that it automatically closes file)
with open ("rushda.txt")as f:
    #print(f.read())
    print(f.read(8))# now with read:
#if not using with then close file
#READLINE: reads only first line
f=open("rushda.txt")
print(f.readline())
print(f.readline())#it read two line
f.close()
#

