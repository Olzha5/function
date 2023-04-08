import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.random(4), columns=['random'])
print(df)

df = df.applymap(lambda x: '{:.2%}'.format(x))

print(df)
