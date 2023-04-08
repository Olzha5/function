import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV-файла
df = pd.read_csv('alphabet_stock_data.csv')

# Преобразуем столбец дат в формат datetime
df['Date'] = pd.to_datetime(df['Date'])

# Указываем диапазон дат для построения
start_date = pd.to_datetime('2020-04-01')
end_date = pd.to_datetime('2020-09-30')
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)

# Создать новый DataFrame, содержащий только те строки, которые попадают в диапазон дат
df_subset = df.loc[mask]

# Установите столбец даты в качестве индекса
df_subset = df_subset.set_index('Date')

# Создайте сложенный график цен открытия и закрытия
fig, ax = plt.subplots(figsize=(10, 6))
df_subset[['Open', 'Close']].plot(kind='area', stacked=True, ax=ax)
ax.set_xlabel('Дата', fontsize=12)
ax.set_ylabel('Цена', fontsize=12)
ax.set_title('Сложенный график цен открытия и закрытия для Alphabet Inc.\nс 01-04-2020 по 30-09-2020', fontsize=14)
plt.show()