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

# Построить гистограммы цен открытия, закрытия, максимума и минимума
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
df_subset['Open'].plot.hist(bins=20, ax=axes[0, 0])
axes[0, 0].set_xlabel('Цена открытия', fontsize=12)
df_subset['Close'].plot.hist(bins=20, ax=axes[0, 1])
axes[0, 1].set_xlabel('Цена закрытия', fontsize=12)
df_subset['High'].plot.hist(bins=20, ax=axes[1, 0])
axes[1, 0].set_xlabel('Высокая цена', fontsize=12)
df_subset['Low'].plot.hist(bins=20, ax=axes[1, 1])
axes[1, 1].set_xlabel('Низкая цена', fontsize=12)
fig.suptitle('Гистограммы цен открытия, закрытия, максимума и минимума\для акций Alphabet Inc.\с 01-04-2020 по 30-09-2020', fontsize=14)
plt.tight_layout()
# Запустим plot
plt.show()