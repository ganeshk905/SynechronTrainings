#Conditional statement

a=10

if a==10:
    print('a',a)

if a>=10 and a<100:
        print('a is greater')

if a<10:
    print('a is lesser')


b=10

if b==10:
   print('b is equal')
elif b<10:
   print('b is lesser') 
elif b<10:
   print('b is greater')



c=100

if c==10:
    print('c eq')
elif c>10:
    print('c gt')
else:
    print('b is greater')


S='Python'

if S=='Python':
   print('s eq')

if 'th' in S:
   print('th found')

if 'xy' not in S:
   print('XY not found')


L1=[10,'Python']
L2=[10,'Python']
L3=L2

if L1==L2:
    print('contents are equal')

if L3 is L2:
    print('L3 and L2 are refering the same objects')


if 10 in L1:
    print('10 found')

if 'th' in L1[1]:
    print('th found')


D={'A':10,'B':20}

if 'A' in D:
    print('key-A-found')

if 'A' in D.keys():
    print('key-A-found')


if 20 in D.values():
    print('20 found')

