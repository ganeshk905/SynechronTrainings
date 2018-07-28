a=10
b=0
try:
    r=a/b
except:
    print('Some Error')


c=10
d=0
try:
    r=c/d
except ZeroDivisionError:
    print('ZDE')
except NameError:
    print('NE')


#program termination as except block is not there
''''try:
    #r=c/d
finally:
    print('Finally block')#you can close all teh connections there'''

#try, finally
#try, except
#try, except,finally

#Raise exceptions

e=10
f=0
try:
   if f==0:
       raise ZeroDivisionError
   r=e/f
except ZeroDivisionError:
    print('ZDE')


try:
    assert f>0, 'f is zero' #if condition is false, it will print "F is zero, if true..it will "go to next step
    r=e/f
except AssertionError as a:
    print('AE =', a)


#except:
#except(NameError):
#except(ZeroDivisionError, NameError):
#except(LookupError) # super class..will be able to accept sub-class exceptions

#For all exception class, we have super class - Exception
'''BaseClass Exception -->root
Exception .....>Super classmethod
  ---LookupError
      ----KeyError
      ----IndexError'''


try:
    r=e/f
except Exception as e:
    print(type(e))

#If you do not have an exception defined, you can create it and extend it from Exception

class MyError(Exception):
    def __init__(self, m):
        print('My Error is ', m)
    def help(self):
        print('help msg')
        
try:
    if f==0:
        raise MyError('f is zero')
except MyError as b:
    print(b.help())