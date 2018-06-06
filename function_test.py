"""magician_name = ['1','2','3','4']
magicians = []
def make_great(old_names,new_names):
    while old_names:
        f_magicians = old_names.pop()
        f_magicians = 'the great' + f_magicians
        new_names.append(f_magicians)
def show_magician(names):
    for name in names:
        print(name)
make_great(magician_name[:],magicians)
show_magician(magician_name)
show_magician(magicians)"""
'''def make_sandwich(*burdening):
    print('\n这个三明治需要的配料有：')
    for burdenings in burdening:
        print('-'+ burdenings)
make_sandwich()
make_sandwich()'''
'''def build_profile(first,last,**user_info):
    profile_dict = {}
    profile_dict['first'] = first
    profile_dict['last'] = last
    for key,value in user_info.items():
        profile_dict[key] = value
    return profile_dict
profiles = build_profile('1','2',s='4',m='5',a='6')
print(profiles)'''
'''def car_profile(facturer,size,**user_info):
    profile_dict = {}
    profile_dict['facturer'] = facturer
    profile_dict['size'] = size
    for key,value in user_info.items():
        profile_dict[key] = value
    return profile_dict
car = car_profile('subaru', 'outback', color='blue',tow_package=True)
print(car)'''
#在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实
#例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
#添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
#添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就
#餐人数。
'''class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_resaurant(self):
        print(self.restaurant_name, ':' ,self.cuisine_type)
    def open_resaurant(self):
        print('营业中：')
    def served(self):
        print("现在有",str(self.number_served),"人在就餐")
    def in_number_served(self,number):
        while self.number_served <= number:
            print(restaurant.served())
            self.number_served += 1
restaurant = Restaurant('A','B')
restaurant.describe_resaurant()
restaurant.open_resaurant()
restaurant.number_served = 2
restaurant.in_number_served(10)
restaurant.served()'''
#创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。在类User 中定义一个名
#为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。
#创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
'''class User():
    def __init__(self,first_name,last_name,):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0
    def describle_user(self):
        print("first_name:",self.first_name,"last_name:",self.last_name)
    def greet_user(self):
        print("hello",self.first_name," ",self.last_name)
    def in_login_attemps(self):
        self.login_attemps += 1
        print('login_attemps:',self.login_attemps)
    def reset_login_attemps(self):
        self.login_attemps = 0
        print(self.login_attemps)
f_user = User('A','B')
f_user.describle_user()
f_user.greet_user()
f_user.in_login_attemps()
f_user.in_login_attemps()
f_user.reset_login_attemps()'''
#在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。编写一个名为increment_login_attempts() 的方法，
#它将属性login_attempts 的值加1。再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。
#根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。打印属性login_attempts 的值，确认它被正确地递增；然后，调用方
#法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。


#冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant 类。这两个版
#本的Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋
#的方法。创建一个IceCreamStand 实例，并调用这个方法。
'''class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_resaurant(self):
        print(self.restaurant_name, ':' ,self.cuisine_type)
    def open_resaurant(self):
        print('营业中：')
    def served(self):
        print("现在有",str(self.number_served),"人在就餐")
    def in_number_served(self,number):
        while self.number_served <= number:
            print(self.number_served)
            self.number_served += 1
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours = ['1','2','3']
    def iccreams(self):
        for i in self.flavours:
            print(i)
ice_name = IceCreamStand('1','2')
ice_name.iccreams()
ice_name.describe_resaurant()'''
#管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。添加一个名为privileges 的属性，用
#于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。编写一个名为show_privileges() 的方法，它
#显示管理员的权限。创建一个Admin 实例，并调用这个方法。
'''class User():
    def __init__(self,first_name,last_name,):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0
    def describle_user(self):
        print("first_name:",self.first_name,"last_name:",self.last_name)
    def greet_user(self):
        print("hello",self.first_name," ",self.last_name)
    def in_login_attemps(self):
        self.login_attemps += 1
        print('login_attemps:',self.login_attemps)
    def reset_login_attemps(self):
        self.login_attemps = 0
        print(self.login_attemps)
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = ['1','2','3']
    def show_privileges(self):
            print(self.privileges)
admin = Admin('1','2')
admin.show_privileges()'''
"""with open('pi_digits.txt') as file_09:
    contents = file_09.read()
print(contents)"""
#在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，其中每一行都以“In Python you can”打头。将这个文件命名为
#learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。编写一个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个
#文件；第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在with 代码块外打印它们。
'''filename = 'learning_python.txt'
with open(filename) as file_09:
    lines = file_09.read()
print(lines)'''
'''filename = 'learning_python.txt'
with open(filename) as file_09:
    lines = file_09.readlines()
    for line in lines:
        f_line = line.replace('Python', 'C')
        print(f_line.rstrip())'''
#提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引
#发TypeError 异常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获TypeError 异常，并打印一
#条友好的错误消息。对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
'''if __name__ == '__main__':
    while True:
        try:
            first_number = input("输入：")
            if first_number == 'q':
                break;
            second_number = input("输入：")
            if second_number == 'q':
                break;
            f_sum = int(first_number) + int(second_number)
        except ValueError:
            print("只可以输入数字")
        else:
            print(f_sum)'''
#编写一个程序，提示用户输入他喜欢的数字，并使用json.dump() 将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打印
#消息“I know your favorite number! It's _____.”。
import json
'''def fdump(route,l_number):
    with open(route,'w') as file_09:
        json.dump(str(l_number),file_09)
def fload(route):
    with open(route) as file_09:
        num = json.load(file_09)
        print("I know your favorite number! It's "+num)
filename = 'username.json'
l_number = input("your favourite number is: ")
fdump(filename,l_number)
fload(filename)'''
#将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
#运行这个程序两次，看看它是否像预期的那样工作。
import json
def fdump(route):
    l_number = input('your favourite number is ')
    with open(route,'w') as file_09:
        json.dump(str(l_number),file_09)
def fload(route):
    with open(route) as file_09:
        num = json.load(file_09)
    if num:
        print("I know your favorite number! It's "+num)
    else:
        fdump(route)
if __name__ == '__main__':
    route = 'username.json'
    fdump(route)
    fload(route)

































































