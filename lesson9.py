from threading import Thread
from time import sleep

def count(name):
    print('Starting thread ' + name)
    for i in range(10, 0, -1):
        sleep(1)
        print(name + ': ' + str(i))
    print('Stopping thread ' + name)

t1 = Thread(target=count, args=('t1' ,))
t2 = Thread(target=count, args=('t2' ,))
t1.start()
t2.start()
t1.join()
t2.join()