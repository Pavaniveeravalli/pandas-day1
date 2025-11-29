import pandas as pd
abc=pd.read_excel("./student.xlsx")
# print(abc)

abc["Name"]=abc["Name"].str.strip().str.upper()
print(abc)

# print(abc.head(2))
# print(abc.tail(1))
# print(abc.info())
# print(abc.shape)
# print(abc.describe())
# print(abc.columns)
# print(abc.nunique())
# print(abc.sample(5))