# Задача о сортировке массива

def min_num(x):
    a = x[0]
    for i in x:
        if i < a:
            a = i
    return a

def smalltobig(nums_in):
    nums_out = []
    while nums_in != []:
        n = min_num(nums_in)
        nums_in.remove(n)
        nums_out.append(n)
    return nums_out

print("Введите числа через пробел:")
print(smalltobig(list(map(int, input().split(" ")))))