

x = 88

def func():
    global x
    x = 99
    return x
#    print(func())

print(x)
print(func())