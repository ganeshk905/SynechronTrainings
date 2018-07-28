#classes is collection of methods and variables#Multiple object
#Inheritance..existing the existing method for child class
#Operator overloading..
class Account1: #class variable (b_name)  and instance variable (uname) - we use it with an instance; class function and instance function
    #instance object and class object#class object will be created when class is created
    b_name='ICICI' #class variable #static
    def adduser(self, u): #adduser(a, u1) once you call as a.adduser(u1)
        self.uname=u
    def viewuser(self):
        return self.uname
    def __init__(self): #init is constructor
        print('Account logic here')
    def viewrules(): #no self hence you can directly call with classname.method name..if self..then you have create object and then call
        return 'Some Rules'

a=Account1()#calls init at this point
b=Account1()#calls init at this point
a.adduser('u1')
b.adduser('u2')
print(a.viewuser())
print(b.viewuser())
print(Account1.b_name)
print(Account1.viewrules())

class Account2(Account1):
    #b_name='HDFC'
    def addaadhar(self, a):
        self.aadhar=a
    def viewaadhar(self):
        return self.aadhar
    def __init__(self):
        print('CA logic')
        super().__init__()#to call parent class init
        #Account1.__init__(self) another way of calling

c=Account2()
c.adduser('U3')
c.addaadhar('A1')
print(c.viewuser())
print(Account1.b_name)
Account1.viewrules()
print(c.viewaadhar())

class RBI:
    def RBIrules(self):
        return 'RBI rules'

class Account3(Account2, RBI):#multiple inheritance ..search will happen from left to right classes
    def message(self):
        return 'Inside Account3'

d=Account3()
d.adduser('U4')
d.addaadhar('A4')
print(d.viewuser())
print(d.viewaadhar())
print(Account3.b_name)
print(Account3.viewrules())
print(d.RBIrules())

class govt:
    def RBIrules(self):
        return 'govt rules'

class Account4(Account2, RBI):
    def __init__(self):
        self.grules=govt()

e=Account4()
e.adduser('U5')
e.addaadhar('A5')
print(e.viewuser())
print(e.viewaadhar())
print(Account3.b_name)
print(Account3.viewrules())
print(e.RBIrules())
print(e.grules.RBIrules())

class Account5:
    def __init__(self, n):
        self.name=n
    def __add__(self, other):
        return 'Hello ' + self.name + ' and ' + other.name
X=Account5('abc')
Y=Account5('XYZ')
Z=X+Y
print('Z= ', Z)




