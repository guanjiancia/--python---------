import os

'''''
  当前是index.py 文件   导入的模块是commons.py 文件
'''

'''class commons():
    def main(self):
        # 利用字符串的形式去对象(模块)中操作(寻找/检查/删除/设置)成员 反射
        imp = input('请输入一个方法:')  # 比如login
        # delattr()  删除内存里面的方法
        # setattr()  #设置内存里面的方法
        if hasattr(self, imp):  # 判断有没有这个方法
            fuc = getattr(self, imp)  # 获得这个方法
            fuc()  # 会调用 commons文件里面的方法
        else:
            print('404')

c = commons()
c.main()
print(hasattr(c,'put'))'''

'''a = {"filename": "aa.avi", "filesize": 148161214}
b = a['filesize']
print(b)'''

# def test1(*args):
#     print(args)
#     cmd_split = args[1]
#     print(cmd_split)
#
# test1(1,2,3,4,5)

import threading,time
import multiprocessing

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run thread is : %s\n" % n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)
    for i in range(12):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print("----all threads done ----")




























