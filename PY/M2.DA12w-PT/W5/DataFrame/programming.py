import pandas as pd
import numpy as np

languages=pd.Series(["Python","JavaScript","HTML","SQL"])
# print(languages)

overflow=pd.Series([3,1,2,4])
# print(overflow)

# df=pd.DataFrame([("Anne",30),("Bill",27),("Charlie",55)],
# columns=["Name","Age"])
# print(df)

df2=pd.DataFrame({
    "Languages": languages,
    "Ranking": overflow
})
# print(df2)
# print()
df2.loc[4]=["PHP",11]
# print(df2)
# print()
df2.loc[3.5]=["KESL",20]
# print(df2)
# print()
df2=df2.sort_index() # reorder
# print(df2)
# print()
df2["Ranking 2022"]=[4,1,2,3,10,15]
# print(df2)
# print()
df2["Ranking 2020"]=[5,10,20,30,24,32]
df2["Ranking 2019"]=[8,9,12,16,14,15]
# print(df2)
# print()
df2.insert(3,"Ranking 2021",[4,8,6,11,45,24]) #add someone forgot in a middle eg.
# print(df2)
# print()
df2.rename(columns={"Ranking":"Ranking 2023"}, inplace=True)
print(df2)
print()
df2=df2.set_index("Languages") # select col/default

print(df2.loc["Python","Ranking 2020"]) # Python 2020, only
print(df2.loc["Python","Ranking 2020"]) # Python 2020, only
print()
print(df2.loc["SQL"])
print()
print(df2.loc[:"HTML",:"Ranking 2019":2])
print()
print(df2.iloc[2])