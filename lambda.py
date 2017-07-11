from python import time

start = time.clock()
print(start)

#fib = lambda n,x=0,y=1:x if not n else fib(n-1,y,x+y)
fib = lambda n:1 if n<=3 else fib(n-1)+fib(n-2)
print(fib(20))

end = time.clock()
print("read: %f s" % (end - start))

def dt(s1,s2):
    return [x for x in s1 if x in s2]
s1 = 'PythoN'
s2 = 'python'

print(dt(s1,s2))

