import pandas as pd
import numpy as np

data = {'name': ['Jack', 'Jane', 'Amber', 'Crystal', 'Harry'],
        'year':[2000,1999,2002,2003,2001],
        'points': [1.5, 1.7, 3.6, 4.0,3.0 ]}
df = pd.DataFrame(data)
print(df)

# 행 방향의 index
print(df.index)

# 열방향의 index
print(df.columns)

print(df.values)

df.index.name = 'Num'
df.columns.name = 'Info'
print(df)

# 판다스 기초정리 3.DataFrame indexing 전까지 읽음.