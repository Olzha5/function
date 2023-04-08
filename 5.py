# # 11. Как получить позиции элементов серии A в другой серии B?
import pandas as pd
# Создаем тестовые серии А и В
ser_A = pd.Series(['item_1', 'item_2', 'item_3', 'item_4','item_6'])
ser_B = pd.Series(['item_2', 'item_3', 'item_5'])
# Находим товары серии А, которых нет в серии В
result = ser_A[~ser_A.isin(ser_B)]
print (result)

# import pandas as pd
# data = pd.read_csv('fish.csv')
# data.head()  # показать первые 5 строк DataFrame
# data.tail() 
# data.info()
# print(data.head())
# print(data.tail() )

# import pandas as np
# import pandas as df
# import pandas as pd
# Пример 1
# Преобразовать индексы объекта Series в столбец DataFrame
# test_list = 'abcedf'
# test_arr = np.arange(len(test_list))
# test_dict = dict(zip(test_list, test_arr))
# s = pd.Series(test_dict)
# # сбрасываем индексы
# df = s.to_frame().reset_index()
# # присвоение имёен столбцам
# df.columns=['letter', 'number']
# print(df.columns)

#2 primer
# получаем номер строки и столбца (индексацию) по условию

# row, col = np.where(df.values == 5)
# print('индексы строк и столбцов:')
# print(row)
# print(col)
# print()
# # получаем данные по индексации (подобно индексации в матрице)
# if (row.size != 0) and (col.size != 0):
#  print('данные по индексации (строка, столбец):')
#  print(df.iat[row[0], col[0]])
#  print(df.iloc[row[0], col[0]])
#  print()
# # получаем данные по индексации и именованому объекту (смешанный тип)
# if (row.size != 0) and (col.size != 0):
#  print('данные по индексации и наименованию:')
#  print(df.at[row[0], 1])
#  print(df.at[row[0], 'letter'])
#  print()
 
# # получаем по условию столбцы и строки DataFrame
# # (loc;at - принимают строки(столбцы) с определенными метками из индекса (именованные метки))
# # (iloc, iat) - принимают номера строк и столбцов
# ans1 = df.loc[df['letter'] == 'a']
# print('данные по условию:')
# print(ans1)


#4 primer
# import pandas as np
# n = 0
# col = 'a'
# # создаем DataFrame
# df = pd.DataFrame(np.random.randint(low=1, high=100, size=30).reshape(10, 3), columns=list('abc'))
# print(df)
# print()
# # получаем искомый номер строки
# ans = df[col].argsort()[::-1].iloc[n]
# print(ans)





# import pandas as pd
# import pandas as np
# import random
# df = pd.DataFrame(np.random.randint(-20, 20, 100).reshape(10,10))
# print(df)
# print()
# # оставляем только положительные значения вектора
# arr = df[df > 0].values.flatten()
# arr_qualified = arr[~np.isnan(arr)]
# # определяем размерность квадратной матрицы
# n = int(np.floor(arr_qualified.shape[0]**.5))
# # формируем матрицу из положительных значений
# top_indexes = np.argsort(arr_qualified)[::-1]
# output = np.take(arr_qualified, sorted(top_indexes[:n**2])).reshape(n, n)
# # переводим в объект DataFrame
# df2 = pd.DataFrame(data=output.astype('i'), columns=np.arange(output.shape[1]))
# print(df2)
