#main_prog.py import the function from lib folder

import addmodule #defined function in lib
import sys
r1=sys.path
print('r1=', r1)

sys.path.append(r'..\lib') #second way to add path vriable but temporary only till program execution
r2=sys.path
print('r2 =', r2)

print(addmodule.msg)
print(addmodule.add(10,20))

import addmodule as a

print(a.msg)
print(a.add(10,20))

from addmodule import msg,add
print(msg)
print(add(10,20))

from addmodule import *
print(msg)
print(add(10,20))

from addmodule import msg as m
print(m)

#inside folder structures

import project.net.addmodule

print(project.net.addmodule.msg)
print(project.net.addmodule.add(10,20))

import project.net.addmodule as a
print(a.msg)
print(a.add(10,20))


from project.net.addmodule import *
print(msg)
print(add(30,40))

from project.net.addmodule import msg as m
print(m)

from project.net.addmodule import msg,add
print(msg)
print(add(40,50))







