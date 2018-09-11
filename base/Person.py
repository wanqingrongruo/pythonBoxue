
class Person:
    """A general person class"""
    def __init__(self, name, age):  # 类的构造函数, self 表示执行方法的对象本身, 初始化函数的首参... 在Python里，方法的第一个表示对象自身的参数是显式的，它需要明确写在方法的参数列表里
        self.name = name
        self.age = age
    
    
    def wakeup(self, at):
        print("{0} wake up at {1} am".format(self.name, at))

    def __del__(self):
        print(self.name + " is realeaimed")
