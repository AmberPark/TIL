import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Series
# obj = pd.Series([4, 7, -5, 3])
# print(obj)
# print(obj.index)

sdata = {'Kin': 35000, 'Jack':67000, 'Joan': 30000, 'Choi': 40000}
obj2 = pd.Series(sdata)
# print(obj2)

obj2.name = 'Lunch'
obj2.index.name = 'Names'
print(obj2)