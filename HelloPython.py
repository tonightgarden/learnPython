#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(100 + 1000)
print('hello tg')
print('hello tg',  'name is', 'tg', 'age = ' , 26)
#name = input()
#print('input name is ',name)

a = 1000
if a >100:
    print('a > 100')
else:
    print('a <= 100')
	
print(0xff00)
print("I‘am fine")
print('I"am ok')
print('\nI\'am \"ok\"')
print(r'hijn]'r'"''\n',r'\\\\n')
print('''line1
line2
line3''')
print(r'''line1
line2
line3''')
print(3>2)
print(not(3>2 and 2>3))

a =100
print('a = ',a)
a = 'abc'
print('a = ',a)
print(10/3)
print(10//3)
print(ord('A'),'\n')
print(chr(67),'\n')
print('\u4e2d\u6587')
print('中文'.encode('utf-8'))
print('中文'.encode('utf-8').decode('utf-8'))

print(len('你好adf'))
print(len('你好adf'.encode('utf-8')))
print('hello, my name is %s and  I\'am %d years old\n' %('lilei',22))

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])



height = 1.75
weight = 80.5

#weight = int(input('输入体重 ： '))
bmi = weight/(height*height)
if bmi>32:
    print('严重肥胖')
elif bmi>=28:
    print('肥胖')
elif bmi>=25:
    print('过重')
elif bmi>=18.5:
    print('正常')
else:
    print('过轻')
	

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(name)
	
number = (213,23,34)
for num in number:
    print(num)    

	
dis = {'tg':34,(1,2,3):23}
print(dis['tg'])
print(dis[(1,2,3)])
	


