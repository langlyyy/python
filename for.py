
#for iterating_var in sequence:
#    statements(s)

for letter in 'Python':
    print('当前字母：', letter)

fruits = ['banana', 'apple', 'mango']
for fruits in fruits:
        print('水果：', fruits)

D = [(1,2), (3,4), (5,6)]
for x in D:
    print(x)

for ((a,b),c) in (((1,2),3),((4,5),6),((7,8),9)):
    print((a,c),b)