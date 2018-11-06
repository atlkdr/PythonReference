from time import sleep
from threading import *

class A(Thread):
    def __init__(self,id,rate):
        self.rate = rate
        self.id=id
        Thread.__init__(self)
    def run(self):
        for i in range(1,10):
            print("Hello:",self.id)
            sleep(self.rate)

a=A('id1',1)
b=A('id2',2)

a.start()
b.start()

a.join()
b.join()
