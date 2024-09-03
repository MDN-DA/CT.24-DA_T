import pandas as pd

df=pd.read_excel("n:/Learn/PLD/DA/M2.DA12w-PT/W6/Cleaning/cleaning_activity.xlsx")
df.info()
print(df)
df=df.drop(columns=["Transaction Type","Till ID","Unnamed: 0"])
df.at[60,"Cost"]=6.0
df=df.drop(64)
df=df.dropna(how="any")
df=df.drop_duplicates()
# df=["Staff"]=df["Staff"].str.capitalize()
# print()
# def split_up_basket(strg):
#     strg = strg.strip("[","]","[")
#     strg = strg.strip("'","")
#     items = strg.split(',')
#     stripped_items = ...

def split_basket(string):
    items = string.split(',')
    stripped_items = [item.strip() for item in items]
    return stripped_items

# print(df.explode("Basket").value_counts())
# print(df)
# # df.to_excel("mb_sales_c2.xlsx", index=False