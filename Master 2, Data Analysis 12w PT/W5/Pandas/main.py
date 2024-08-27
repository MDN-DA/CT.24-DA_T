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