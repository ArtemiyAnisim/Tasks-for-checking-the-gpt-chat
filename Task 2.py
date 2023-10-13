# Задача о поиске наибольшего элемента в массиве:

print('Введите числа через пробел:')
nums = list(map(int, input().split(' ')))
a = nums[0]

for i in nums:
    if i > a:
        a = i

print(a)