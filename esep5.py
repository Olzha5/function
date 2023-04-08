import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV-файла
df = pd.read_csv("alphabet_stock_data.csv")

# Преобразуем столбец дат в формат datetime
df["Date"] = pd.to_datetime(df["Date"])

# Указываем диапазон дат для построения
start_date = pd.to_datetime("2020-04-01")
end_date = pd.to_datetime("2020-09-30")
mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)

# Создать новый DataFrame, содержащий только те строки, которые попадают в диапазон дат
df_subset = df.loc[mask]

# Создание горизонтального столбчатого графика цен открытия и закрытия
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(y=df_subset["Date"], width=df_subset["Open"], height=0.5, color="red", label="Open")
ax.barh(y=df_subset["Date"], width=df_subset["Close"], height=0.5, color="blue", label="Close")
ax.set_xlabel("Цена", fontsize=12)
ax.set_ylabel("Дата", fontsize=12)
ax.set_title("Цены открытия и закрытия акций Alphabet Inc. с 01 апреля 2020 г. по 30 сентября 2020 г.", fontsize=14)
ax.legend(loc="lower right")
plt.tight_layout()
# Запустим plot
plt.show()
