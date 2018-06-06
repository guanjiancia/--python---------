#
# import threading
# import time
#
# event = threading.Event()
#
# def lighter():
#     count = 0
#     event.set()
#     while True:
#         if count > 4 and count < 10:
#             event.clear()
#             print('\033[41;1mred light is on...\033[0m')
#         elif count > 10:
#             event.set()
#             count = 0
#         else:
#             print('\033[42;1mgreen light is on...\033[0m')
#         time.sleep(1)
#         count += 1
#
# def car(name):
#     while True:
#         if event.is_set():
#             print('[%s] runing...' % name)
#             time.sleep(1)
#         else:
#             print('[%s] sees red light , waiting...' % name)
#             event.wait()
#
# l = threading.Thread(target=lighter)
# l.start()
# car = threading.Thread(target=car,args=('Tesla',))
# car.start()

import threading,time

event = threading.Event()
def light():
    count = 0
    event.set()
    while True:
        if count > 5 and count < 10:
            event.clear()
            print(" \033[41;1mred light is on ...\033[0m")
        elif count > 10:
            event.set()
            count = 0
        else:
            print(" \033[42;1mgreen light is on ...\033[0m")
        time.sleep(1)
        count += 1

def car(n):
    while True:
        if event.is_set():
            print("%s runing ..." % n)
            time.sleep(1)
        else:
            print("%s see red light,waiting..." % n)
            event.wait()

t = threading.Thread(target=light)
t.start()
c = threading.Thread(target=car,args=("Tesla",))
c.start()





































