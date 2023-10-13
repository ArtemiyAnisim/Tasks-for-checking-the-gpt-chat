# Задача о вычислении числа Фибоначчи

x = int(input())
a = 0
b = 1

if x == 1:
    c = 0
elif x == 2:
    c = 1
else:
    for i in range(x - 2):
        c = a + b
        a = b
        b = c

print(c)