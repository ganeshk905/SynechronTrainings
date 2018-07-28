F1=open(r'c:\training\log\out1.txt', 'w')#F1 is file object
x=10
x=str(x)+'\n'
s='python\n'
F1.write(x)
F1.write(s)
F1.flush()#only flush the contents from buffer to file


L=[x,s]
F1.writelines(L)
F1.close()#flush and close the object


F2=open(r'C:\training\log\out1.txt', 'r') #read-only mode (default), if file not present..will throw error
r1=F2.read()#read all the file contents in single string#r1='10\npython\n10\npython\n'
print('r1 =', r1)
F2.seek(0)#sek(0) means first chracter in file
r2=F2.read()#seek pointer initially at beginning, after 1st read, it is at the end of file..reset it
print('r2 =', r2)
F2.seek(0)

r3=F2.readline()#Storing only 1 line
r4=F2.readline()
print('r3 =', r3)
print('r4 =', r4)

F2.seek(0)

r5=F2.readlines()
print('r5 =', r5)

F2.seek(0)

while True:
    line=F2.readline()
    if line=='':
        print('Reached End of File')
        break
    else:
        print ('Line =', line)


F2.seek(0)
for line in F2:
    print ('line =' , line)
F3=open(r'C:\training\log\out2.txt','w')
print(x,s,100,200,file=F3,flush=True)
F4=open(r'C:\training\log\out3.csv', 'w')
print(10,20,30,sep=',',file=F4,flush=False)
F3.close()
F4.close()


