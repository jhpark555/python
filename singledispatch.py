import functools

@functools.singledispatch
def show_type(argument):
    print(f'argument:{argument}')

@show_type.register(int)
def show_int(argument):
    print(f'int argument:{argument}')

@show_type.register
def show_float(argument:float):
    print(f'float argument:{argument}')


show_type('abc')
show_type(123)
show_type(1.23)

registry =dict()

def register(function):
    type_ = next(iter(function.__annotations__.values()))
    registry[type_]=function

    @functools.wraps(function)
    def _register(argument):
        new_function =registry.get(type(argument),function)
        return new_function(argument)
    
    return _register


@register
def show_type1(argument:any):
    print(f'argument1:{argument}')

@register
def show_int1(argument: int):
    print(f'int argument1: {argument}')

show_type1('abc')    
show_type1(123)


import json

@functools.singledispatch
def write_as_json(file,data):
    json.dump(data,file)

@write_as_json.register(str)
@write_as_json.register(bytes)
def write_as_json_filename(file,data):
    with open(file,'w') as fh:
        write_as_json(fh,data)

data = dict(a=1,b=2,c=3)

write_as_json('test1.json',data)
write_as_json(b'test2.json','w')
with open('test3.json','w') as fh:
    write_as_json(fh,data)

#print(write_as_json.registry.keys())