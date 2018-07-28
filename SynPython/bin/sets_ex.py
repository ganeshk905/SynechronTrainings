#sets
#Unique
#No key/index
#Mutable
s={10,10,'python', 'python'}
#unordered
print(s) #will print only single occurence


#add
s.add(100)
s.add(100)
print(s)

#Remove
r1=s.remove(100)
r2=s.pop()
print(r1, r2)
del r1

t=s.copy()
s.clear()
print(t,s)

L=[10,10,10,'a','a']
s=set(L)
L=list(s)
print(s,L)
