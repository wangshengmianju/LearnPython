# 我们有描述符的工具，还有装饰器的语法，搞清楚@property的实现非常重要
# @property就是预先将属性存取器封装为一个描述符，然后再利用装饰器的语法实现描述符的赋值，总体上是将自定义类里面的方法伪装成一个属性（其实调用的是函数，但是执行的是描述符协议，看起来就像属性的存取）。采用@语法糖的缺点就是：property类的初始化，只能接收到fget的参数，所以property给我们准备了getter、setter、deleter三个函数作为附属的描述符，这三个函数再次调用property类的初始化来吸收自定义的get、set、delete存取器

def newProperty(setMethod=None, delMethod=None):       #这个外包装就是为了完成自定义set方法的导入，没什么必要的情况下直接用property.setter就好了,而且最便捷的方法是不要使用@语法糖，而直接采用property（fget，fset，fdel，doc) 函数的形式。
    def deco(func):
        func = property(func, setMethod, delMethod)
        return func
    return deco

class student():
    def __init__(self, point=60):
        self._score = point
        print('Initialization complete')

    def set_score(self, value):
        print('hello')
        self._score = value

    @newProperty(set_score)
    def score(self):
        print('hi')
        return self._score  #不能假设属性名为score，因为score已经被描述符对象占用了，如果再次使用score，会导致无限循环
    


jack = student(99)
#jack.score = 99
print(jack.score)
print(student.score)