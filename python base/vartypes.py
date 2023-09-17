# Variables and types

# + - * /
a = 321
b = 12
print(a + b)    # 333
print(a - b)    # 309
print(a * b)    # 3852
print(a / b)    # 26.75

# type
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))


# true false
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False