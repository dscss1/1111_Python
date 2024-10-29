import random


def first():
    print("Hello")
    return 10


def printLine(count, symbol):
    print(symbol*count)


def summ(var1, var2=0, var3=0, var4=0):
    result = var1 + var2 + var3 + var4
    return result


# printLine()
# a = first()
# print(a)
#
# printLine()
#
# b = summ(10, 20, 30, 40)
# #c = summ(10, 20, 30)
# #d = summ(10, 20)
# print(b)
# print(c)
# print(d)
#
# printLine()


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


# a = [1,2,4,7,8,7,5,3,4,6]
# count = 0
# for i in a:
#     if isEven(i):
#         print(i, end=' ')
#         count += 1
#
# print()
# print(count)


def orel_reshka():
    n = random.randint(0,1)
    if n == 1:
        print("Орел")
        return 1
    else:
        print("Решка")
        return 0

count = 0
for i in range(10):
    if orel_reshka() == 1:
        count += 1
printLine(5, '#=')
print(count)