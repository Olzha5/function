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

# Создайте фигуру с двумя подграфиками для цен открытия и закрытия
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 6))

# Построить гистограмму цен открытия
ax1.hist(df_subset['Open'], bins=20, color='blue')
ax1.set_xlabel('Цена открытия', fontsize=12)
ax1.set_ylabel('Частота', fontsize=12)
ax1.set_title('Гистограмма цен открытия для Alphabet Inc.\nс 01-04-2020 по 30-09-2020', fontsize=14)

# Построить гистограмму цен закрытия
ax2.hist(df_subset['Close'], bins=20, color='green')
ax2.set_xlabel('Цена закрытия', fontsize=12)
ax2.set_ylabel('Частота', fontsize=12)
ax2.set_title('Гистограмма цен закрытия Alphabet Inc.\nс 01-04-2020 по 30-09-2020', fontsize=14)

plt.tight_layout()
plt.show()