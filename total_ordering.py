import functools

class Value(object):
    def __init__(self,value):
        self.value=value
    def __repr__(self):
        return f'<{self.__class__.__name__}{self.value}'
    
class Spam(Value):
    def __gt__(self,other):
        return self.value> other.value
    def __ge__(self,other):
        return self.value>= other.value
    def __lt__(self,other):
        return self.value< other.value
    def __le__(self,other):
        return self.value<=other.value
    def __eq__(self,other):
        return self.value == other.value
    
@functools.total_ordering
class Egg(Value):
    def __lt__(self,other):
        return self.value < other.value
    def __eq__(self,other):
        return self.value ==other.value
    
numbers= [4,2,3,4]
spams = [Spam(n) for n in numbers]
eggs =[Egg(n) for n in numbers]

print(spams)
print(eggs)
print(sorted(spams))
print(spams[0].__eq__(eggs[0]))
print(sorted(eggs))