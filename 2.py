import pandas as pd

# создаем DataFrame
df = pd.DataFrame(["STD, City State",
                   "33, Kolkata West Bengal",
                   "44, Chennai Tamil Nadu",
                   "40, Hyderabad Telengana",
                   "aaaaaaaaaaaaaaaaaaaa"],
                  columns=['row'])

# разделяем значения столбца row на два столбца
df[['1', 'City State']] = df['row'].str.split(', ', expand=True)

# далее разделяем столбец City State на два столбца
df[['2', '3']] = df['City State'].str.split(' ', n=1, expand=True)

# удаляем исходный столбец row и City State
df.drop(['row', 'City State'], axis=1, inplace=True)

print(df)
print("salem")
