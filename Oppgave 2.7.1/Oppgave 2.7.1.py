import numpy

rang = int(input('input how many number you wanna sort: '))
value = [0]*rang
tmp = 0
print('Input',rang, 'numbers')
for i in range(rang) :
    value[i] = float(input('input value no: ' + str(i + 1) + ' '))
    
for i in range(rang) :
    for j in range(rang - i - 1):
        m = i + j + 1
        if value[i] < value[m]:
            a = value[i]
            value[i] = value[m]
            value[m] = a

for a in value:
    print(a)