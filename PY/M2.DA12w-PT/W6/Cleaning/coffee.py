import pandas as pd

df=pd.read_excel("n:/Learn/PLD/PY/M2.DA12w-PT/W6/Cleaning/first_hour_sales.xlsx")
df.info()
# print(df.describe())
# df=df.set_index("Transaction ID")
df=df.drop(columns=["Till ID","Unnamed: 0"])
df=df.dropna(how="any")
# print(df[df.duplicated()])
df=df.drop_duplicates()
df.at[15.0,"Cost"]=6.00
print(df)
def float_to_time(time_record):
    time_record = str(time_record)
    hours, minutes = time_record.split('.')
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return timestamp
df["Time"]=df["Time"].apply(float_to_time)
df["Time"]=pd.to_datetime(df["Time"],format='%H:%M').dt.time
print(df)
def split_basket(str):
    items=str.split(",")
    stripped_items = [item.strip()for item in items]
    return stripped_items
df["Basket"]=df["Basket"].apply(split_basket)
print(df["Basket"])
exploded_data = df.explode("Basket")
print(exploded_data["Basket"].value_counts())