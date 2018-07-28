#Strings
'''
c-1
c-2
'''
"""
C-1
C-2
"""
a=10
b=a
c='python'
d="PERSON's"
e='''PERSON'S HEIGHT XYZ"'''
f="""PERSON's"""
g='PERSON\'S'
path='C:\training\test.py'
print (path)
path2='C:\\training\\test.py'
path3=r'C:\training\test.py'
print(path, path2, path3, sep='\n')
f='WEL COME'
print (f[0])

#Slicing
print(f[1:6]) #EL CO
print(f[ :4]) #WEL
print (f[4: ])
print (f[ : ])
print (len(f))
print(f[1:6:1])
print(f[1:6:2])
print(f[1:6:3])
print(f[ : : -1])
print(f[6:1:-1])
print(f[6:1:-2])
print(f[-1])
print(f[len(f)-1])
print(f[-4:])

r1=f.startswith('WEL')
r2=f.endswith('COME')
#TRUE, FALSE
print ( r1, r2)
r3=f.isupper()
r4=f.upper()
print ( r3, r4)
r5=f.islower()
r6=f.lower()
print ( r1, r2)
print(r5, r6)

r7=f.istitle()
r8=f.title()
print ( r7, r8)

s1='Hello'
s2='python'
r9=s1+s2
r10=s1*10
print ( r9, r10)
line='-'*40
print(line)

h='abc'
r11=h.isalpha()
i='123'
r12=i.isdigit()
j='abc123'
r13=j.isalnum()
print(r11, r12, r13)
r14=f.split()#split by space
r15=f.split('E')#['W', 'LCOM' , ' ']
print (r14, r15)
k=' wel come '
r16=k.strip()
r17=k.lstrip()
r18=k.rstrip()

print(r16, r17, r18, sep='\n')

l='[wel[come]'
r19=l.strip('[]')
r20=l.lstrip('[')
r21=l.rstrip(']')
print(r19, r20, r21, sep='\n')

x=10
y=20
z=x+y
r22='add of x and y is z'
print (r22)
r23='add of {} and {} is {}'.format(x,y,z)
print(r23)
r24='add of {2} and {1} is {0}'.format(z,y,x)
print(r24)
r25=f.index('E')
r26=f.find('E')
print( r25, r26)

r27=f.index('E', 2)
print( f, r27)

r28=f.count('E')
r29=f.replace('E', 'e')
print(r28, r29)

