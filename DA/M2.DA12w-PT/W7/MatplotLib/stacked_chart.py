import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.DataFrame({
    "Engineering":[56,13,1],
    "Computer Science":[77,23,4],
    "English Lit":[35,48,9],
    "Economics": [65,45,19]
}, index=["Male", "Female", "Non-Binary"])

df=df.T
my_plot=df.plot.barh(stacked=True)
plt.title("Student per Subjects")
plt.ylabel("Subject")
plt.show()
