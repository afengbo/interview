# 单例模式：确保一个类只有一个实例
# 比如,某个服务器的配置信息存在在一个文件中,客户端通过AppConfig类来读取配置文件的信息.
# 如果程序的运行的过程中,很多地方都会用到配置文件信息,则就需要创建很多的AppConfig实例,这样就导致内存中有很多AppConfig对象的实例,造成资源的浪费.
# 其实这个时候AppConfig我们希望它只有一份,就可以使用单例模式.
#####################
#  1. 装饰器实现


import threading


def single_model(cls):
    instances = {}

    def single(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return single


@single_model
class A:
    a = 6

    def __init__(self):
        print("AAAAAAAAAAA")


# a1 = A()
# a2 = A()
# print(a1.a, id(a1))
# print(a2.a, id(a2))


####################
#  2. 反射、__new__实现
#  注意：这种方法在python2中不好使，因为继承方式的原因(super)


class Singleton(object):
    _instance_lock = threading.Lock()

    # def __init__(self, *args, **kwargs):
    #     pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Singleton._instance_lock:
                # if not hasattr(cls, '_instance'):
                Singleton._instance = super().__new__(cls)

            return Singleton._instance
        return getattr(cls, '_instance')


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)
