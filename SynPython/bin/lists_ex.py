#LIST
L=[10,12.5,'python',['a','b']]
m=list()
print (L)
print(L[0])
print(L[2][2])
print(L[1:])

#add
L.append(100)
print(L)
L.insert(2, 200)
print(L)
L1=[10,20]
L2=['a', 'b']
L3=L1+L2
print(L3)
L1.extend(L2)
print(L1)

#update
L[0]=300
print(L)
#Error as string is immutable L[3][2]='x'#Error
print(L)

#remove
r1=L.pop()#remove item from end
print(L)
r2=L.pop(1)
print(L)
r3=L.remove('python')#removes but doesnt return anything hence "None"
print(r3)
del r1
del L[0]
del m
print(L)

L4=[20,10]
L5=['b','a', 'z']
r4=L4.count(20)
r5=L4.index(10)
print (r4, r5)
L4.sort()#it cannot sort for lists having numbers and alphabets
L5.sort(reverse=True)
print(L4, L5)

L6=L5.copy()#Shallow copy
print(L6)
L6.clear()
print(L6)#response is [] as it is cleared andn ot deleted
import copy
L7=copy.copy(L5)
L8=copy.deepcopy(L5)#deep copy
print (L7, L8)

L1=[10,20,['a','b']]
L2=copy.copy(L1)
L1.append(30)
L1[2].append('c')
L3=copy.deepcopy(L1)
L1[2].append('d')
print(L1, L3)



