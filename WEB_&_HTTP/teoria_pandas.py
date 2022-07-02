import pandas as pd
personas= pd.read_csv(".csv", sep=";")

#imprimo con head 5 rows del df
print (personas.head())

#print (personas.info)

print(personas.describe())
print()