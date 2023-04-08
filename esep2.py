import pandas as pd
import matplotlib.pyplot as plt

# Считываем данные из CSV-файла
df = pd.read_csv("alphabet_stock_data.csv")

# Преобразуем столбец дат в формат datetime
df['Date'] = pd.to_datetime(df['Date'])

# Выбираем диапазон дат, для которых будем строить гистограмму
start_date = pd.to_datetime('2020-04-01')
end_date = pd.to_datetime('2020-09-30')
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)

# Создаем новый DataFrame, содержащий только строки, соответствующие выбранному диапазону дат
df_subset = df.loc[mask]

# Строим гистограмму объема торгов акциями Alphabet Inc.
plt.figure(figsize=(10, 5))

plt.hist(df_subset['Volume'], bins=30, color='green')

plt.xlabel('Объем торгов', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.title('Гистограмма объема торгов Alphabet Inc.\nс 01.04.2020 по 30.09.2020', fontsize=14)
plt.show()
