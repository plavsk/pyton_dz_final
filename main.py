import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

unical = data['whoAmI'].unique()
one_hot = pd.DataFrame()

for val in unical:
    one_hot[val] = (data['whoAmI'] == val).astype(int)

one_hot.head()   