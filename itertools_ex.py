import itertools

def islice(iterable, start, stop=None, step=1):
    
    if stop is None and step ==1 and start is not None:
        start, stop= 0, start
        
        iterator = iter(iterable)
        #print(len(iterable))
        for _ in range(start):
            print('#',_)
            next(iterator)
            
        for i, item in enumerate(iterator, start):
            if i>= stop:
                return
            if i% step:
                print('@')
                continue
            yield item
            
print(list(itertools.islice(range(1000),10)))
print(list(itertools.islice(range(1000),900,920,2)))
print(list(itertools.islice(range(1000), 900, 910)))