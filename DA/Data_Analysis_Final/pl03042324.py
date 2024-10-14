import pandas as pd

pl = pd.read_excel(r"n:\Learn\PLD\DA\Data_Analysis_Final\PL 03-04, 23-24.xlsx")
print(pl.describe())
print()
# Q1_dl=isp["Download (Mb/s)"].quantile(0.25)
# Q3_dl=isp["Download (Mb/s)"].quantile(0.75)
# Q1_up=isp["Upload (Mb/s)"].quantile(0.25)
# Q3_up=isp["Upload (Mb/s)"].quantile(0.75)
# IQR_dl=Q3_dl-Q1_dl
# IQR_up=Q3_up-Q1_up
# outliers_dl = isp[(isp["Download (Mb/s)"] < (Q3_dl+(1.5*IQR_dl))) | (isp["Download (Mb/s)"] > (Q1_dl-(1.5*IQR_dl)))]
# outliers_up = isp[(isp["Upload (Mb/s)"] < (Q3_up+(1.5*IQR_up))) | (isp["Upload (Mb/s)"] > (Q1_up-(1.5*IQR_up)))]
# print(f"IQR Download - Lower Bound: {(Q1_dl-(1.5*IQR_dl)):2f}")
# print(f"IQR Download - Upper Bound: {(Q3_dl+(1.5*IQR_dl)):2f}")
# print(f"IQR Upload - Lower Bound: {(Q1_up-(1.5*IQR_up)):2f}")
# print(f"IQR Upload - Upper Bound: {(Q3_up+(1.5*IQR_up)):2f}")
# print()
# print(outliers_dl)
# print(outliers_up)
