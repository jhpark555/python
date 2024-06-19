import functools

class Property(object):
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel

    def __get__(self,instance,cls):
        if instance is None:
            return self
        elif self.fget:
            return self.fget(instance)
    
    def __set__(self,instance,value):
        #print('@',instance)
        self.fset(instance,value)
    
    def __delete__(self,instance):
        self.fdel(instance)

    def getter(self,fget):
        return Property(fget,self.fset,self.fdel)
    
    def setter(self,fset):
        return Property(self.fget,fset,self.fdel)
    
    def deleter(self,fdel):
        return Property(self.fget,self.fset,fdel)
    
class Sandwich:
    def __init__(self):
        self.registry={}

    def __getattr__(self,key):
        print('Getting %r' %key)
        return self.registry.get(key,'Undefined')
    
    def __setattr__(self,key,value):
        if key=='registry':
            object.__setattr__(self,key,value)
        else:
            print('Setting %r to %r' %(key,value))
            self.registry[key]=value

    def __delattr__(self,key):
        print('Deleting %r' % key)
        del self.registry[key]


    @Property
    def eggs(self):
        return self._eggs
    
    @eggs.setter
    def eggs(self,value):
        print('setter')
        self._eggs=value
    @eggs.deleter
    def eggs(self):
        del self._eggs

sandwich= Sandwich()
sandwich.eggs= 5
print(sandwich.eggs)

print(sandwich.a)
sandwich.a=1
print(sandwich.a)
del sandwich.a