import pandas as pd
headers = ['Name', 'Age', 'Weight']
values = ['Ayoub', 20, 80]

my_ser = pd.Series(data=values, index=headers)
print(my_ser)