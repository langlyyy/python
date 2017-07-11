


def my_abs(x):
    if x < 0:
        return(-(x))
    else:
        return(x)

def power(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s

p = power(3,5)
print(p)

a = my_abs(-10)
print(a)


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

sd = calc(1, 2, 3, 9)
print(sd)

def person(name,age, **kw):
    return(name, age, 'other:', kw)


#name = input("输入你的名字：")
#age = int(input("输入你的年龄："))
#aihao = input("输入你的爱好：")

#print(person(name, age, sfs=aihao))


def func(a, b, c=0, *args, **kw):
    print('a =', a, 'b = ', b, 'c = ', c, 'args =', args, 'kw =', kw)

func(1,3,'s','df','dfs',ss=4)



