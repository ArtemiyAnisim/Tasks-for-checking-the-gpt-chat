# Задача на хэш-таблицы

x = [] # Массив на вход (ввести строки туда)

a = {}
b = 0
ans = ''

for i in x:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
    if a[i] > b:
        b = a[i]
        ans = i

print(ans)