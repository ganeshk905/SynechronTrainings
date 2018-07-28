#map ....you need to pass a function and any collection object like list or tuple, it will basically call the function with all list elements as arguments.
#generates generator object


L=[100,200,300,400]
def disc(P):
    return P-10

r1=map(disc, L)
#print('r1 =', list(r1))
#print('r1 =', list(r1))
for i in r1:
    print('í=', i)


#filter ..depending on return value - true or false , it will add or omit list values..returns generator object


def filt(P):
    return P>100 and P<400
r2=filter(filt,L)
print('r2 =', list(r2))


def filt_servers(s):
    if s.startswith('p'):
        return True
    else:
        return False

M=['pseri', 'tseri', 'dseri', 'pser2']
r3=filter(filt_servers, M)
print('r3 =', list(r3))


#reduce

def red(p,q):
    return p+q
from functools import reduce#import the library
r4=reduce(red, L)
N=['W','E','L']
r5=reduce(red, N)
print(r4)
print(r5)

#lambda functions

r7=map(lambda P:P-10, L)
r8=filter(lambda P:P>100 and P<400, L)
r9=reduce(lambda p,q:p+q, L)

r10=lambda a,b:a+b
r11=r10(10,20)
r12=[lambda a,b:a+b, lambda a,b:a-b]#list of lambda functions ; call by index
r13=r12[0](10,20)

D={'ádd':lambda a,b:a+b, 'sub':lambda a,b:a-b}
r14=D['ádd'] (10,20)
print('r14 = ', r14)
