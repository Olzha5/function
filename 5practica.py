
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range('1/1/2000', periods=10), columns=list('ABCD'))
diff_df = df.diff()
df.plot()
df.plot.bar()
df.plot.barh(stacked=True)
df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
df.plot.hist(bins=20)
df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
diff_df.hist(bins=20)
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area()
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
#  Создание DataSet с двумя столбцами
data = {'x': np.arange(1, 11), 'y': np.random.randn(10)}
df = pd.DataFrame(data)

# Гистограмма
df.plot(kind='bar', x='x', y='y', color='blue')
plt.title('Гистограмма')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Линейная диаграмма
df.plot(kind='line', x='x', y='y', color='red')
plt.title('Линейная диаграмма')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Точечная диаграмма
df.plot(kind='scatter', x='x', y='y', color='green')
plt.title('Точечная диаграмма')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Круговая диаграмма
sums = df.groupby(df['y'] > 0).size()
labels = ['Отрицательные', 'Положительные']
colors = ['red', 'green']
plt.pie(sums, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Круговая диаграмма')
plt.show()
plt.show()







































































# import matplotlib as mpl
# import matplotlib.pyplot as plot
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(10,4), index=pd.date_range('1/1/2000', periods=10), columns=list('ABCD'))
# df.plot.bar(stacked=True)
# df.plot()
# plot.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
#  periods=10), columns=list('ABCD'))
# df.plot()
# print(df.plot())
# iloc primer
# df = pd.DataFrame([[200, 150], [5000.5, 1500.1]],
#                   index=['python', 'sql'],
#                   columns=['students', 'price'])
# df.iloc[1]
# print(df.iloc[1])
# ##loc primer
# df = pd.DataFrame([ [200,    150], 
#                     [5000.5, 1500.1]],
#                     index=['python', 'sql'],
#                     columns=['students', 'price'])
# df
# print(df)
# # В метод read_csv() 
# df = pd.read_csv('fish.csv')
# # head - вывод первых N строк таблицы
# df.head(3)
# print(df.head(3))
# df.tail(5)
# print(df.tail(5))





# data = {'col1': [100.0, 5.0, 10.5],        
#         'col2': [200.0, 4.0, 11.4],
#         'col3': [300.0, 3.0, 12.3]}
# df = pd.DataFrame(data, index=['a', 'b', 'c'])
# result_one = df.loc['a']
# result_two = df.loc[:, 'col2']
# result_three = df.iloc[:, :2]
# result_four = df.iloc[-1:]
# print(df)
# print("result_one:")
# print(result_one)
# print(df)
# print("result_two:")
# print(result_two)
# print("result_three:")
# print(result_three)
# print(df)
# print("result_four:")
# print(result_four)








## 5 practica 
# import pandas as pd
# df = pd.read_csv('fish.csv')
# # df.shape
# # print(df.shape)

# df.info()


# import numpy as np
# import pandas as pd


# df = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))

# print(df)

# minRow= df.min(axis=1)
# print('min')
# print(minRow)
# print('max')
# maxRow = df.max(axis=1)
# print(maxRow)








# import pandas as pd
# import numpy as np
# df = pd.read_csv('fish.csv')
# df = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))

# min_by_max = df.apply(lambda row: min(row.max(), axis=0))
# print(min_by_max)


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range('1/1/2000', periods=10), columns=list('ABCD'))
# diff_df = df.diff()
# df.plot()
# # df.plot.bar()
# # # df.plot.barh(stacked=True)
# # # df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
# # # np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
# # # df.plot.hist(bins=20)
# # # df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
# # # np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
# # # diff_df.hist(bins=20)
# # # df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# # # df.plot.area()
# # # df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
# # # df.plot.pie(subplots=True)# Создание DataSet с двумя столбцамиdata = {'x': np.arange(1, 11), 'y': np.random.randn(10)}
# df = pd.DataFrame(data)

# # Гистограммаdf.plot(kind='bar', x='x', y='y', color='blue')
# plt.title('Гистограмма')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# # Линейная диаграммаdf.plot(kind='line', x='x', y='y', color='red')
# plt.title('Линейная диаграмма')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# # Точечная диаграммаdf.plot(kind='scatter', x='x', y='y', color='green')
# plt.title('Точечная диаграмма')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# # Круговая диаграммаsums = df.groupby(df['y'] > 0).size()
# labels = ['Отрицательные', 'Положительные']
# colors = ['red', 'green']
# plt.pie(sums, labels=labels, colors=colors, autopct='%1.1f%%')
# plt.title('Круговая диаграмма')
# plt.show()

# plt.show()
