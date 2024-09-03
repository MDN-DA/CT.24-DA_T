import pandas as pd

isp=pd.read_excel(r"n:\Learn\PLD\DA\M2.DA12w-PT\(3)ISP\group_results.xlsx")
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
print(isp.describe())