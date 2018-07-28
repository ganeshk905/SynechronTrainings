def add():
    x=10
    y=20
    print(x+y)
def sub():
    x=10
    y=20
    print(x-y)
add()
sub()
from threading import Thread, Lock
class MyThread(Thread):
    def __init__(self, f): #compulsarily defined
        self.func=f#self.func=add
        super().__init__()
    def run(self): #it should always be run function and should be compulsarily defined
        print('start')
        mylock.acquire() #locking so that only 1 thread exceutes at one time
        self.func()#add
        mylock.release() #releasing the lock now
        print('End')
mylock=Lock()
t1=MyThread(add)
t2=MyThread(sub)
#t1.start() #will call init and run
#t1.join()#Thread objects will run simulatneously so if you want to first complete t1.start() and then start t2.start(), then use t1.join(), else both threads will be executed simultaneoulsy.
#t2.start()

import queue
q=queue.Queue(4)#depending on priority, you can store, first in first out ..this queue can hold 4 threads
q.put(t1)
q.put(t2)
r1=q.empty()
r2=q.full()
r3=q.qsize()
print(r1,r2,r3)

while not q.empty():
    t=q.get()
    t.start()#it will start t1 and immediately execute the thread for t2








