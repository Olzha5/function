import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-11-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1.set_index('Volume')
plt.figure(figsize=(5,5))
plt.suptitle('Alphabet Inc', \
 fontsize=18, color='black')

plt.scatter(df1['Volume'],df2['Low'],color='purple', alpha=0.7)

plt.xlabel("Volume",fontsize=16, color='black')
plt.ylabel("Price", fontsize=16, color='black')
plt.legend(loc='upper left')
plt.show()