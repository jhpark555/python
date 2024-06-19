def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')
        
b1=dict(api=1, author='Douglas Hofstadter',type='book',title='Godel, Escher, Bach')
print(get_creators(b1))

from collections import OrderedDict
b2= OrderedDict(api=2, type='book', title='Python in a nutshell',
                authors='Martelli Ravenscroft Holden'.split())
print(get_creators(b2))

print(get_creators({'type':'book','api':1,'author':'Philip park'}))



from collections.abc import Sequence, Callable

def until(
limit: int,
filter_func: Callable[[int], bool],
v: int
) -> list[int]:
    if v == limit:
        return []
    elif filter_func(v):
        return [v] + until(limit, filter_func, v + 1)
    else:
        return until(limit, filter_func, v + 1)
    
