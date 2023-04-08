import pandas as pd
# Create a
data = {'city': ['Almaty', 'Nur-Sultan', 'Shymkent'],
'population': [1800000, 1700000, 700000]}
df = pd.DataFrame(data)
# Add a new colum
df['area'] = [1000, 800, 600]
# Delete a column 
df = df.drop('area', axis=1)
# Rename a column
df = df.rename(columns={'population': 'pop'})
print(df)
# import pandas as pd
# df = pd.read_csv('fish.csv')
# head - вывод первых N строк таблицы
# handle = open(4)
# df.head(3)
# df.tail(5)
# print(df.tail(5),df.head(3))
# df = pd.DataFrame([[200, 150], [5000.5, 1500.1]],
#                   index=['python', 'sql'],
#                   columns=['students', 'price'])
# df.iloc[1]
# print(df.iloc[1])





# import pandas as pd
# iloc primer
# df = pd.DataFrame([[200, 150], [5000.5, 1500.1]],
#                   index=['python', 'sql'],
#                   columns=['students', 'price'])
# df.iloc[1]
# print(df.iloc[1])

#В метод read_csv() 
# df = pd.read_csv('fish.csv')
# head - вывод первых N строк таблицы
# df.head(3)
# print(df.head(3))
# df.tail(5)
# print(df.tail(5))





# data = {'col1': [100.0, 5.0, 10.5],        
#         'col2': [200.0, 4.0, 11.4],
        # 'col3': [300.0, 3.0, 12.3]}
# df = pd.DataFrame(data, index=['a', 'b', 'c'])
# result_one = df.loc['a']
# result_two = df.loc[:, 'col2']
# result_three = df.iloc[:, :2]
# result_four = df.iloc[-1:]
# print(df)
# print("result_one:")
# print(result_one)
# print("result_two:")
# print(result_two)
# print("result_three:")
# print(result_three)
# print("result_four:")
# print(result_four)


# import numpy as np
# import pandas as pd
# # L1
# # 1esep_6lab

# # создание ряда со случайными целыми числами от 1 до 10
# ser = pd.Series(np.random.randint(1, 10, 35))

# # изменение формы ряда в матрицу 7x5
# matrix = ser.values.reshape(7, 5)

# # создание DataFrame из матрицы
# df = pd.DataFrame(matrix)

# # вывод результата
# print(df)

# import pandas as pd
# # Input
# ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
# # Solution 1
# from dateutil.parser import parse
# # Parse the date
# ser_ts = ser.map(lambda x: parse(x))
# # Construct date string with date as 4
# ser_datestr = ser_ts.dt.year.astype('str') + '-' + ser_ts.dt.month.astype('str') + '-' + '04'
# # Format it.
# [parse(i).strftime('%Y-%m-%d') for i in ser_datestr]
# # Solution 2
# ser.map(lambda x: parse('04 ' + x))
# print(ser.map)
# 2esep

# # создание рядов ser1 и ser2
# ser1 = pd.Series(range(5))
# ser2 = pd.Series(list('abcde'))

# # объединение рядов вертикально в DataFrame
# df_vertical = pd.concat([ser1, ser2], axis=0)

# # вывод результата
# print(df_vertical)

# # horizont

# # создание рядов ser1 и ser2
# ser1 = pd.Series(range(5))
# ser2 = pd.Series(list('abcde'))

# # объединение рядов горизонтально в DataFrame
# df_horizontal = pd.concat([ser1, ser2], axis=1)

# # вывод результата
# print(df_horizontal)

# L2
# 1esep

# создание ряда со случайными целыми числами от 1 до 10
# ser = pd.Series(np.random.randint(1, 10, 7))
#
# # нахождение позиций чисел, кратных 3
# positions = ser.loc[ser % 3 == 0].index
#
# # вывод результата
# print(positions)

# 2esep

# from sklearn.metrics import mean_squared_error
#
# # создание рядов truth и pred
# truth = pd.Series(range(10))
# pred = pd.Series(range(10)) + np.random.random(10)
#
# # вычисление MSE между truth и pred
# mse = mean_squared_error(truth, pred)
#
# # вывод результата
# print(mse)

# 3esep

# создание рядов p и q
# p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
#
# # вычисление евклидова расстояния между p и q
# distance = np.linalg.norm(p.values - q.values)
#
# # вывод результата
# print(distance)

# 4esep

# создание исходного DataFrame
# df = pd.DataFrame(np.arange(25).reshape(5, -1))
#
# # замена местами первой и второй строки
# df.iloc[[1, 0]] = df.iloc[[0, 1]].values
#
# # вывод результата
# print(df)

# 5esep

# создание исходного DataFrame
# df = pd.DataFrame(np.arange(25).reshape(5, -1))
#
# # переворот всех строк
# df = df.iloc[::-1]
#
# # вывод результата
# print(df)


# 6esep

# создание исходного Series
# ser = pd.Series(['how', 'to', 'kick', 'ass?'])
#
# # изменение первого символа каждого слова на заглавный
# ser = ser.str.title()
#
# # вывод результата
# print(ser)


# L3

# 1esep

# создание исходного Series
# L = pd.Series(range(15))
#
# # создание DataFrame со строками в виде шагов из L
# df = pd.DataFrame({'Step_1': L})
# for i in range(2, 6):
#     df[f'Step_{i}'] = L.shift(i-1)
#
# # удаление строк с пропущенными значениями
# df.dropna(inplace=True)
#
# # вывод результата
# print(df)

# 2esep

# создание DataFrame
# df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
# 
# # выбор положительных элементов
# df_pos = df[df > 0]
#
# # удаление отрицательных элементов
# df_pos.dropna(axis=0, how='all', inplace=True)
# df_pos.dropna(axis=1, how='all', inplace=True)
#
# # определение максимально возможного квадрата
# n_rows, n_cols = df_pos.shape
# n = min(n_rows, n_cols)
# while n > 0:
#     if (n_rows >= n) and (n_cols >= n):
#         break
#     n -= 1
#
# # удаление лишних строк и столбцов
# if n < n_rows:
#     df_pos.drop(df_pos.index[n:], inplace=True)
# if n < n_cols:
#     df_pos.drop(df_pos.columns[n:], axis=1, inplace=True)
#
# # вывод результата
# print(df_pos)




