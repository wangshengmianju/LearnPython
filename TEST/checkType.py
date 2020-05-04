#这实际上是完成修改类的工作，究竟是怎么实现的呢？__get__函数中的instance究竟传入的是什么东东？它居然知道调用字典来查看属性
#也许描述符Typed本身是一个类，当它被关联的时候就对应了一个描述符对象，而__get__函数中的第二参数object是这个描述符对象的实例，但是新的问题又来了，从python语言的角度，什么是类，什么是实例？(现在代码里面的print已经很完备的输出了变量的信息，就等搞清楚了）

class Typed:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]   #为什么访问字典，是因为如果直接访问name会触发get或者set函数

    def __set__(self, instance, value):
        print('set--->',self,instance,value)
        if not isinstance(value,self.expected_type):
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)

def typeassert(**kwargs):
    def decorate(cls):      #这个语法糖是怎么完成People = decorate(people)的？可以写多重装饰器么？
        print('类的装饰器开始运行啦------>',cls,kwargs)
        for name,expected_type in kwargs.items():
            setattr(cls,name,Typed(name,expected_type))
        return cls
    return decorate
    
@typeassert(name=str,age=int,salary=float) #有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)
class People:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

#有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs
# 2.People=decorate(People)

#print('People-----',People.__dict__)  # 在decorate(People)装饰符的函数中加了数据装饰符属性
p1=People('egon',18,3333.3)
#print(p1)
#print('People.name',People.name)

#print('p1-----',p1.__dict__) # 因为 instance.__dict__[self.name]=value的缘故，p1中也添加了这些实例属性
#print('People-----',People.__dict__)
#print(p1.name) # 因为数据装饰符的优先级大于实例属性，
                # 所有这里的name其实是描述符，然后调用了描述符中的get方法，
                # 返回了实例中的实例属性name
#p1.name = 'das'
#print(p1.name)


