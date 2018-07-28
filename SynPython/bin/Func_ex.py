#functions

def add1():
    pass

def add2():
    a=10
    b=20
    c=a+b
    print('c=',c)

add2()
add2()
#print('c=', c) NameError: name 'c' is not defined (fn scope variable)

def add3():
    a=10
    b=20
    c=a+b
    #return c
    #return     #return None
    #return a,b,c #returns tuple with a,b,c values : (10, 20, 30)
    return a+b/c

r1 = add3()
print(r1)

#positional args
def add4(a,b):
    return a+b
r2=add4(10,20) #positional args
print(r2)

#positional args with def value
def add5(a, b=10):
    return a+b
r3 = add5(10)
r4 = add5(10,0)
r5 = add5(10, 20)
print(r3,r4,r5) #20 10 30

# *c - tuple/variable arg (like params in c#)
def add6(a,b=10,*c):
    print('tuple c=', c)
    res = a + b
    for i in c:
        res += i
    return res

r6=add6(10) #a=10, b=10, c=()
print(r6) # 20
r7=add6(10,20) #a=10, b=20, c=()
print(r7) #30
r8=add6(10,20,30,40) #a=10, b=20, c=(30,40)
print(r8) #100

# tuple similar to print fn
def add7(*a):
    if(len(a) > 0):
        res = 0
        for x in a:
            res += x
        return res
    else:
        return None

r9=add7()
r10=add7(10)
r11=add7(10,20.5)
print(r9,r10,r11)

#key word only args : like sep and end args in print fn
def add8(a,b=10,*c,d,e=10):
    print('tuple c=', c)
    res = a + b + e + d
    for i in c:
        res += i
    return res

#key word only args : order not matter
r12=add8(10,20,30,40,50,e=60,d=70) #a=10, b=20, c=(30,40,50), d=70, e=60
print(r12)

def add9(a,b,*c):
    print(a,b,c)
x=10
y='Hello'
L=[10,20]
T=('a','b')
D=dict(A=10, B=20)

add9(x,y,L,T,D) #10 Hello ([10, 20], ('a', 'b'), {'A': 10, 'B': 20})

# fn which take only keyword arg... add * as first arg
def add10(*,user,pswd):
    print(user,pswd)
r13 = add10(pswd='Welcome@123', user='admin' )

#fn ** => extra args goes in dict
def add11(a,b=10,*c,d,e,**f):
    print('tuple=',c)
    print('Dict=', f)
    res=a+b+d+e
    for i in c:
        res += i
    for j in f.values():
        res += j
    return res

r14 = add11(10, e=20, d=30) # a=10, b=10, c=(), d=30, e=20, f={}
print(r14)
r15 = add11(10,20,30,40,d=50,e=60,g=70,h=80) # a=10, b=20, c=(30,40), d=50, e=60, f={'g':70, 'h':80}
print(r15)


