import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

number_of_placements=np.array(range(1,11))
responses_received=np.array([14, 21, 34, 36, 45, 51, 54, 63, 78, 92])
m,c=np.polyfit(number_of_placements,responses_received,1)

plt.scatter(number_of_placements,responses_received)
plt.plot(number_of_placements,m*number_of_placements+c)
plt.title("Job Posting Responses")
plt.xlabel("Num of places avertised")
plt.ylabel("Num of places received")
plt.show()