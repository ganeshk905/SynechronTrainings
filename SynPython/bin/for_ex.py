#For loop

S='python'

for a in S:
    print('a=',a)

L=[10,20]
b=100
for b in L:
    print('b=',b)

print('Now b=',b)


D={'A':10,'B':20}

for K in D:
    print('K=',K)
    print('V=',D[K])

for K in D.keys():
    print('K=',K)


L1=[10,20,30]
L2=['a','b']

r1=zip(L1,L2)
print('r1=',list(r1))

for i,j in zip(L1,L2):
    print(i,j)


comp=['sap','syn','IBM']

for C in comp:
    if C=='syn':
        print('Found')
        break
else:
    print('Not Found')
