n = int(input('введите количество элементов последовательности:'))
x=1
s=0
print(x)
for i in range(n) :
    s+=x
    x/=-2
    print(x)
print('сумма ряда:',s )