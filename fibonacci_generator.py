def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
def main():
    fib=fibonacci()
    for _ in range(10):
        print(next(fib),end=',')

if __name__=='__main__':
    main()