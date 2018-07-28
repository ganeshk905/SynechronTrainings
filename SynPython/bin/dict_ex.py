#Dictionary
D={'course':'python', 'dur':5, 'loc':['pune', 'blr']}
E=dict(course='python', dur=5, loc=['pune', 'blr'])
print(D,E)


print(D['course'])

#add,update
D['course']=['java','python']
print(D)
print(D['loc'][1])

#remove
r1=D.pop('course')
r2=D.popitem()#key value pair
print(r1,r2)
del E['dur']
print(E)
del D
D=E.copy()
E.clear()
print(D, E)

k=D.keys()
v=D.values()
i=D.items()
print(k, v, i)

