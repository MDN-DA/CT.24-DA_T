import pandas as pd

isp = pd.read_excel(r"n:\Learn\PLD\DA\M2.DA12w-PT\(3)ISP\results2024-9-3-1143.xlsx")
isp=isp.drop(columns=["Unnamed: 0"])
print(isp)
print()
print(f"Mean:\n{isp.mean(numeric_only=True)}")
print()
print(f"Median:\n{isp.median(numeric_only=True)}")
print()
print(f"Fastest:\n{isp.max(numeric_only=True)}")
print()
print(f"Slowest:\n{isp.min(numeric_only=True)}")
print()
print()
print(isp.describe())
print()
Q1_dl=335.05
Q3_dl=355.96
Q1_up=155.10
Q3_up=163.70
IQR_dl=Q3_dl-Q1_dl
IQR_up=Q3_up-Q1_up
print(f"IQR Download - Lower Bound: {(Q1_dl-(1.5*IQR_dl)):2f}")
print(f"IQR Download - Upper Bound: {(Q3_dl+(1.5*IQR_dl)):2f}")
print(f"IQR Upload - Lower Bound: {(Q1_up-(1.5*IQR_up)):2f}")
print(f"IQR Upload - Upper Bound: {(Q3_up+(1.5*IQR_up)):2f}")