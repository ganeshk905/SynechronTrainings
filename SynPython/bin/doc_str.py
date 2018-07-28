#Documentation

#multiline comment by '''  '''
'''
C-1
C-2
'''

#C-3

"""
C-4
C-5
"""

def f():
    '''
    C-6
    C-7
    '''

    """
    C-8
    C-9
    """

print(dir(__builtins__))
#print(__cached__)
print(__name__)
print(__file__)
print(__doc__)
print(__loader__)


#Run in IDLE..python shell
'''
Then in shell
1. type...import doc_str....
2. then..dir(doc_str)... o/p is all the fn/variables,builtins used in file
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'f']

3. then...help(doc_str)=> o/p is all the cooments in file

Help on module doc_str:

NAME
    doc_str

DESCRIPTION
    C-1
    C-2

FUNCTIONS
    f()
        C-6
        C-7

FILE
    c:\bhushan\python\bin\doc_str.py

4. help(doc_str.f) =>
Help on function f in module doc_str:

f()
    C-6
    C-7
'''
