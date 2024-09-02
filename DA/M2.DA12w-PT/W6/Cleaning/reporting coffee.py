import pandas as pd
from ydata_profiling import ProfileReport

df=pd.read_excel("n:/Learn/PLD/DA/M2.DA12w-PT/W6/Cleaning/mb_sales_c2.xlsx")
profile=ProfileReport(df)
profile.to_file('mb_sales.html')