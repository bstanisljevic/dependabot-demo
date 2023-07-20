import pandas as pd

df = pd.DataFrame({'A': [True, False, True], 'B': [1, 2, 3]})

# This will work in Pandas 1.5.3
print(df.index.is_boolean())

