from math import *
with open('C:/Users/User/Downloads/matA.csv') as f1: 
    A = [] 
    for line in f1: 
        row = line.strip().split(',') 
        A.append([float(x) for x in row])
with open('C:/Users/User/Downloads/matb.csv') as f2: 
    b = [] 
    for line in f2: 
        row = line.strip().split(',') 
        for x in row:
            b.append(float(x))
def func(c1, c2):
    x1 = 1
    x2 = -1
    t = 0
    h = 0.001
    while t < 10:
        u = c1 * x1 + c2 * x2

        # метод эйлера

        dx1 = A[0][0] * x1 + A[0][1] * x2 + b[0] * u # из условия понимаем что A 2 x 2
        dx2 = A[1][0] * x1 + A[1][1] * x2 + b[1] * u
        x1 = x1 + h * dx1
        x2 = x2 + h * dx2
        t = t + h
    value = (x1 ** 2 + x2 ** 2) / 2
    return value
c_values = []
step = 2 / 24
for i in range(25): 
    c_values.append(-1 + i * step)
with open('C:/Users/User/Downloads/result52.csv', 'w') as f:
    f.write('c1,c2,f\n')
    for c1 in c_values: 
        for c2 in c_values:
            value = func(c1, c2)
            f.write(str(c1) + ',' + str(c2) + ',' + str(value) + '\n')
