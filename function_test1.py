'''def field(recond,label):
	for(fname,fvalue) in recond:
		if fname == label:
			print(fvalue)
bob = [['name','Bob Smith'],['age',42],['pay',10000]]
sue = [['name','Sue Jones'],['age',45],['pay',20000]]
field(bob,'name')'''

'''bob = {'pay':30000,'job':'dev','age':42,'name':'Bob'}
sue = {'job':'hdw','pay':40000,'age':45,'name':'Sue'}
people = [bob,sue]
for person in people:
print(person['name'],person['pay'],sep= ',')'''


'''class Dog():
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("%s is eating ..." %self.name)
d = Dog('oo')
choice = input('>>').strip()
if hasattr(d,choice):
    func = getattr(d,choice)
    func()'''

'''import os
def child():
    print('Hello',os.getpgid())
    os._exit(0)
def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('hello',os.getpgid(),newpid)
        if input() == 'q':
            break
parent()'''


























