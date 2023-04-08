# 11. Как получить позиции элементов серии A в другой серии B?
import pandas as pd
# # Создаем тестовые серии А и В
# ser_A = pd.Series(['item_1', 'item_2', 'item_3', 'item_4','item_6'])
# ser_B = pd.Series(['item_2', 'item_3', 'item_5'])
# # Находим товары серии А, которых нет в серии В
# result = ser_A[~ser_A.isin(ser_B)]
# print (result)



# 5. Как получить полезную информацию

data = pd.read_csv('fish.csv')
data.head(10)  # показать первые 5 строк DataFrame
data.tail() 
print(data.head(10))
print(data.tail() )
data.info()