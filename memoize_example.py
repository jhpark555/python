import functools

cache =dict()

def memoize(function):
    def safe_has(args):
        '''
        In case of unhashable types use the rear() to be hashable
        '''
        try:
            return hash(args)
        except:
            return repr(args)
    
    @functools.wraps(function)
    def _memoize(*args):
        #If the cache is not available, call the function
        #Note that all args need to be hashable
        #key = function, safe_hash(args)
        key = function, args
        if key not in cache:
            cache[key]=function(*args)
        return cache[key]
    return _memoize

@memoize
def printer(*args):
    print(args)

def main():
    printer('a','b','c')

    #printer(dict(a=1,b=2,c=3))

if __name__=='__main__':
    main()