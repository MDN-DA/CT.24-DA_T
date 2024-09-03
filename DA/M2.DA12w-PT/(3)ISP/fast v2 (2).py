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
Q1_dl=isp["Download (Mb/s)"].quantile(0.25)
Q3_dl=isp["Download (Mb/s)"].quantile(0.75)

IQR_dl=Q3_dl-Q1_dl

lower_bound = Q1_dl-(1.5*IQR_dl)
upper_bound = Q3_dl+(1.5*IQR_dl)

df_non_outliers = isp[~((isp["Download (Mb/s)"] < lower_bound) | (isp["Download (Mb/s)"] > upper_bound))]

# df_non_outliers.to_excel(f"outliers_of_results2024-9-3-1143.xlsx")