import matplotlib.pyplot as plt

years=[2018,2019,2020,2021,2022,2023]
python_pos=[7,4,4,3,4,3]
js_pos=[1,1,1,1,1,1]
sql_pos=[4,3,3,4,3,4]
html_pos=[2,2,2,2,2,2]
ts_pos=[12,10,9,7,5,5]
plt.plot(years,python_pos, label="Python")
plt.plot(years,js_pos,label="JavaScript",linestyle="dashed")
plt.plot(years,sql_pos,label="SQL",linestyle="dotted")
plt.plot(years,html_pos,label="HTML",linestyle="dashdot")
plt.plot(years,ts_pos,label="TypeScript")
plt.title("Most popular Languages in Stack Overflow Survey")
plt.xlabel("Year")
plt.ylabel("Position")
plt.legend()
plt.ylim(bottom=20, top=0)
plt.show()