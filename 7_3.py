import pandas as pd

def skiprows(x):
    return x % 50 != 0

df = pd.read_csv('BostonHousing.csv', skiprows=skiprows)

print(df)
