# import threading
# import time

'''class MyThread(threading.Thread):
    def __init__(self,num):
        super(MyThread,self).__init__()
        self.num = num

    def run(self):
        print('runing on numer',self.num)
        time.sleep(2)

t1 = MyThread(1)
t2 = MyThread(2)
t1.start()
t1.join()
t2.start()'''

'''def run(n):
    global num
    num += 1
    print('task',n)
    time.sleep(2)
    print('wall')
num = 0
start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=('done %s' %i,))
    t.setDaemon(t)
    t.start()
    t_objs.append(t)

#for t in t_objs:
#   t.join()

print('task finished -------',threading.current_thread(),threading.active_count())
print('cost:',time.time()-start_time)
print('num:',num)'''

#
# def run(n):
#     lock.acquire()
#     time.sleep(1)
#     print('run the thread: %s' % n)
#     lock.release()
#
#
# if __name__ == '__main__':
#     lock = threading.BoundedSemaphore(5)
#     for i in range(10):
#         t = threading.Thread(target=run,args=(i,))
#         t.start()
# while threading.active_count() != 1:
#     pass
# else:
#     print('------all thread done------')

# import multiprocessing
# import time
# import threading
#
# def run(n):
#     time.sleep(2)
#     print('run %s' % n)
#
# if __name__ == '__main__':
#     for i in range(10):
#         process = multiprocessing.Process(target=run,args=('bob %s' % i,))
#         process.start()


from multiprocessing import Pipe,Process

# def get(coon):
#     coon.send('hello')
#     print(coon.recv())
# if __name__ == '__main__':
#     Parent_coon,Child_coon = Pipe()
#     p = Process(target=get,args=(Parent_coon,))
#     p.start()
#     print(Child_coon.recv())
#     Child_coon.send('im ok')

__author__ = "Alex Li"

import time
import queue
from greenlet import greenlet



# def consumer(name):
#     print("--->starting eating baozi...")
#     while True:
#         new_baozi = yield
#         print("[%s] is eating baozi %s" % (name, new_baozi))
#         # time.sleep(1)
#
#
# def producer():
#     r = con.__next__()
#     r = con2.__next__()
#     n = 0
#     while n < 5:
#         n += 1
#         con.send(n)
#         con2.send(n)
#         time.sleep(1)
#         print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
#
#
# if __name__ == '__main__':
#     con = consumer("c1")
#     con2 = consumer("c2")
#     p = producer()





