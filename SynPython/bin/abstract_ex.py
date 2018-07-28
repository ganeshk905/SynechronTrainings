from abc import ABC, abstractmethod
class MyClass(ABC):#Your class is subclass of ABC-->Abstarct base class
    @abstractmethod#decorator
    def message(self):
        pass
#a=MyClass()

class myclass2(MyClass):
    def message(self):
        print('Hello')
b=myclass2()
b.message()

#abstractmethod, abstractclassmethod
#All methods can be abstract or few
#Create subclass , implement all abstarct methods
#         ELSE
#   subclass will also become abstract class
#You can add abstract method in sub-class too
#Abstract class will not have objects


#decorator function

def my_dec(f):
  def some(a,b):
    print('Start of Result')
    f(a,b)
    print('End of Function')
  return some

@my_dec #here add will be passed as an argument to my_Dec, reason to have decorator functions is to avoid writing common print statements or common logic
def add(x,y):
    print(x+y)
@my_dec
def sub(x,y):
    print(x-y)

add(10,20)
sub(12,20)



#-------------------------------
L=[1,2,3,4]
def squares(M):
    res=[]
    for i in M:
        res.append(i*i)
    return res
r1=squares(L)
for k in r1:
    print('k =', k)
#--------------------------------

#Equivalent generator functions..generator object doesnt store data permanently..it retrieves for once and it is cleared

def sqr(M):
    for i in M:
        yield i*i#while working with generator object, we need to use yield
r2=sqr(L)
for l in r2:
    print('l =', l)
print('r1 =', r1, 'r2 =', list(r2))



import re
import urllib.request
s='10abc30xyz20'
sp=s.split('x')
print(sp)
sp=re.split('[a-z]+',s)
print(sp)

page=urllib.request.urlopen(r'https://www.google.com')
data=page.read()
print(data)
print(type(data))
#data=data.decode()
result=re.findall('http[s]?://[a-zA-Z0-9.]+', str(data))
result2=re.findall('[a-z]+', s)
print('result =', result)
print('result2 =', result2)