N = input('第一个整数：')
A = list(input('第二行整数：'))
min1 = int(min(A))
max1 = int(max(A))
d1 = (max1 - min1)/(N - 1)
B = [0]*N
for i in A:
    j = (i -min1)/di
    B[j] = 1
    if sum(B)==N:
        print('True')
    else:
        print('False')
