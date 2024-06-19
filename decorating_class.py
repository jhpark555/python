import functools

def singleton(cls):
    instances =dict()
    @functools.wraps(cls)
    def _singleton(*args,**kwargs):
        if cls not in instances:
            #print('@')
            instances[cls]= cls(*args,**kwargs)
        return instances[cls]
    return _singleton

@singleton
class SomeSingleton(object):
    def __init__(self):
        print('Executing init')

a=SomeSingleton()
b=SomeSingleton()
print(a is b)
a.x=123
print(b.x)