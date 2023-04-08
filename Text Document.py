
#1   esep
# a= input("Аты жонынызды енгызыныз  ")
# b= input("жасыныз  ")
# c=input("мекен-жайыныз  ")
# print(a)
# print(b)
# print(c)
#2esep

# import math
# x= int(input("ainymaly engiz:"))

# t= int(input("ainymaly engiz:"))
# z =((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
# print("z = {0:.2f}".format(z))
#3 esep
# a1=input("1: ")
# a2=input("2: ")
# a3=input("3: ")
# if a1<=a2 and a1<=a3:
#     min=a1
# elif a2<=a3:
#     min=a2
# else: min=a3
# print(min)
#3/1 esep 
# for num in map(float, input("3 sandy probel arkyly engiz").split()):
#     if 1 < num < 6:
#         print(f" {num} sany osy aralykta zhatyr (1, 6)")



#4 esep

# by= int(input("bagasy "))
# for i in range (1,11):
#     print(i,"kg stoit ",i*by,"tg")
#4/1 esep
# a=int(input("sandar:\n" ))
# sum=0
# n=0
# while a!=0:
#     sum+=a
#     n+=1
#     a=int(input())

# print("summa:",sum)
# print("sandar sany: ",n)






#Функцанальное программирование lab 2 


# 1. Екі бүтін А және В саны берілген (А ≤ B бар). А-дан В-ға дейінгі барлық сандарды басып шығарыңыз. 

# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно. 

# a=int(input("a = "))
# b=int(input("b = "))

# for i in range (a,b+1):
#     print (i)

# 2. А және В екі бүтін сандар берілген.
#  А<B болса, өсу ретімен немесе басқаша жағдайда кему ретімен А-дан В-ға дейінгі барлық сандарды басып шығарыңыз. 

# a=int(input("a = "))
# b=int(input("b = "))
# if a<b:
#     for i in range (a,b+1):
#         print(i)
# else:
#     for i in range(a, b-1, -1):
#         print(i)

# 3. Екі бүтін А және В саны берілген, A>B.
#  А-дан В-ға дейінгі барлық тақ сандарды кему ретімен басып шығарыңыз. Бұл тапсырмада if операторынсыз орындай аласыз. 
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i, end=' ')

# 4.Үстел ойыны үшін 1-ден N-ге дейінгі сандары бар карталар пайдаланылады.Бір карта жоғалады.
#  Қалған карталардың сандарын білу арқылы оны табыңыз. 
# N саны берілген, содан кейін N − 1 қалған карталардың саны (1-ден N-ге дейінгі әртүрлі сандар).
#  Бағдарлама жоғалған картаның нөмірін көрсетуі керек. 
# def missing_card(N, cards):
#     return sum(range(1, N + 1)) - sum(cards)

# N = int(input("Карталар санын енгізіңіз: "))
# cards = [int(input("Карта нөмірін енгізіңіз: ")) for i in range(N - 1)]
# print("Жетіспейтін карта: ", missing_card(N,cards))







# sum1=0
# sum2=0
# n = int(input("n = "))
# for j in range(int(input("j = "))):
#     sum2 += j
# for i in range(1, n + 1):
#     sum1 += i
# print(sum1-sum2)




# import math
# def s3(a):
#     return a*a*math.sqrt(3)/4.0
# def s6(a):
#     return 

# def GCD(a, b):
#     while b:
#         a, b = b, a % b
#         return a
# a, b, c, d = map(int, input().split())
# x = a * d
# y = b * c
# t = GCD(x, y)
# print(x // t, '/', y // t, sep='')







# n = int(input("n = "))

# for i in range(1,n+1):

#    if n % i == 0:

#        print(i,end=" ")

# def sumD(n): 
#  sumD = 0
#  while n!= 0:
#     sumD += n % 10
#     n = n // 10
#  return sumD 

# print (sumD(int(input()))) 


# def QWERT(a,b,c,d):
#     return a/b+c/d
#     return QWERT




# 11 bariant 2 esep
# from random import randint as rd
# def arrmax(arr) :
#     amax = arr[0][0]
#     n = len(arr)
#     for i in range(n) :
#         if max(arr[i]) > amax :
#             amax = max(arr[i])
#     return amax
    
# def arrprint(a, b) :
#     for i in a :
#         print(*i)
#     print()
#     for i in b :
#         print(*i)
#     print()
 
# print('введите для первой матрицы количество строк : ')
# na = int(input())
# print('количество элементов в строке : ')
# ma = int(input())
# print('введите для второй матрицы количество строк : ')
# nb = int(input())
# print('количество элементов в строке : ')
# mb = int(input())
 
# a = [[rd(1,50) for i in range(ma)] for j in range(na)]
# b = [[rd(51,100) for i in range(mb)] for j in range(nb)]
 
# arrprint(a,b)
 
# amax = arrmax(a)
# bmax = arrmax(b)
 
# for i in range(len(a)) :
#     for j in range(len(a[i])) :
#         a[i][j] = bmax if a[i][j] == amax else a[i][j]
# for i in range(len(b)) :
#     for j in range(len(b[i])) :
#         b[i][j] = amax if b[i][j] == bmax else b[i][j]
    
# arrprint(a,b)



#Анализ данных

# 11 nuska 1 - esep

# n = int(input("n = "))
# for i in range(n,2*n-1):
#     print(i,"+ 2 = ",i+2)
 
# 11-nuska 2 - esep
# def swapMaxValue(a,b):
#     max1 = [0,0]
#     max2 = [0,0]
    
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             if(a[i][j] > a[max1[0]][max1[1]]):
#                 max1[0] = i
#                 max1[1] = j
#             if(b[i][j] > b[max2[0]][max2[1]]):
#                 max2[0] = i
#                 max2[1] = j
#     t = a[max1[0]][max1[1]]
#     a[max1[0]][max1[1]] = b[max2[0]][max2[1]]
#     b[max2[0]][max2[1]] = t
# def prin(a):
#     for i in a:
#         print()
#         for j in i:
#             print(j,end=" ")
#     print("")

        
# a = [[1,2,3],[6,9,8],[0,8,7]]
# b = [[0,2,5],[6,10,8],[0,8,7]]
# prin(a)
# prin(b)

# swapMaxValue(a,b)
# prin(a)
# prin(b) 


# 5 nuska 1 - esep
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def subtract_fractions(A, B, C, D):
#     numerator = A * D - B * C
#     denominator = B * D
#     ekeui = gcd(abs(numerator), denominator)
#     return numerator // ekeui, denominator // ekeui

# A = 3
# B = 4
# C = 1
# D = 2
# result = subtract_fractions(A, B, C, D)
# print(f"The result of  {A}/{B} from {C}/{D} is {result[0]}/{result[1]}")



# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# a, b, c, d = map(int, input().split())
# x = a * d
# y = b * c
# t = gcd(x, y)
# print(x // t, '/', y // t, sep='')



#

# 5 nuska 2 - esep
def bolu(n):
    return " ".join(str(i) for i in range(1, n+1) if n % i == 0)

print(bolu(50))



# #hello 

# n = int(input())

# for i in range(1,n+1):

#    if n % i == 0:

#     print(i,end=" ")
# 9 есеп Определить, сколько раз в тексте встречается заданное слово.

# string = str(input('Введите строку, в которой будем искать: \n'))
# search = str(input('Введите что искать: \n'))
# count = 0
# for i in range(len(string)):
#    if string[i: i + len(search)] == search:
#        count += 1
# print(count)


# import pandas as pd 

# values = (1,2,10,'python','date science')
# ds =pd.Series(date=values)
# print(type(ds))
# print(ds)


# import pandas as pd
# # Create a DataFramedata = {'city': ['Almaty', 'Nur-Sultan', 'Shymkent'],
#         'population': [1800000, 1700000, 700000]}df = pd.DataFrame(data)
# # Add a new column
# # df['area'] = [1000, 800, 600]
# # Delete a column# df = df.drop('area', axis=1)
# # Rename a column
# # df = df.rename(columns={'population': 'pop'})
# print(df)


## massivter mat
# 5/2
# Упорядочить по возрастанию элементы каждой строки матрицы 
# размером n х m.

# massive = [
# [1,5,6,9,],
# [7,5,9,4],
# [7,5,3,1],
# [8,9,7,9],
# ]
# print(massive)


# N = 3
# M = 4

# A = [
# [1, 2, 3, 4],
# [5, 6, 7, 8],
# [9,10,11,12]]

# for i in range(N):
#     tmp = A[i][0]
#     A[i][0] = A[i][M-1]
#     A[i][M-1] = tmp

# for i in range(N):
#     for j in range(M):
#         print("\n " % A[i][j], end='')
# print()



# import pandas as pd
# import numpy as np
# numb = pd.Series(data = np.linspace(0, 20, 15))
# print (numb)



# numbers = []  # создаем пустой список для хранения чисел

# # запрашиваем числа у пользователя и добавляем их в список
# while True:
#     num = int(input("Введите целое число (0 для завершения ввода): "))
#     if num == 0:
#         break  # если пользователь ввел ноль, то прерываем цикл
#     numbers.append(num)

# # сортируем список и выводим содержимое на экран
# numbers.sort()
# for num in numbers:
#     print(num)










































