#Tuples
T=(10,12.5,'python',['a','b'],(10,20))
print(T)
print(T[1])
print(T[1:])
#T[0]=100#Error
#Error T[3]=200
T[3].append(200)
print(T)
i=T.index(12.5)
c=T.count('python')
print(i,c)
x=10
r1=type(x)
s='Hello'
r2=type(s)
r3=type(T)
print(r1)

L=list(T)
L.append(100)
T=tuple(L)
print(T)

s='Wel come'
L=list(s)
print(L)
s=','.join(L)
print(s)

