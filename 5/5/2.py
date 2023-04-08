# primer matrix 
# n =3
# A =[]
# for i in range(n):
#     A.append([9]*n)
# for i in range(n):
#     for j in range(n):
#         print(A[i][j]," ")
#     print()

# 11/1
# В данной действительной квадратной матрице порядка п найти сумму 
# элементов строки, в которой расположен элемент с наименьшим 
# значением. Предполагается, что такой элемент единственный.
# m= [
#     [5,7,9],
#     [4,8,2],
#     [7,9,1]
# ]
# n = [min(i) for i in m]
# print(sum(m[n.index(min(n))]))


# 11/2
#  Среди столбцов заданной целочисленной матрицы, содержащих 
# только такие элементы, которые по модулю не больше 10, найти столбец 
# с минимальным произведением элементов и поменять местами с 
# соседним.

#5/2
# Упорядочить по возрастанию элементы каждой строки матрицы 
# размером n х m.

# from random import randint
 
# n = 0
# m = 50
# a = [[randint(n,m) for _ in range(m)] for _ in range(n)]
# for i in a:
#     print(*sorted(i))

m =int (input('katar sany:'))
n = int (input('zholdar sany:'))
a=[]
for i in range(m):
    b = []
    for j in range(n):
        print('element engiz[',i,',',j,'] element')
        b.append(int(input()))
    a.append(b)
print('vash massiv:')
for i in range(m):
    for j in range(n):
        print(a[i][j],end= ' ')
    print()

for i in range(m):
    for j in range(n):
        if a[i][j]>a[i+1][i+1]:
            print(a[i][j],end= ' ')
    print()