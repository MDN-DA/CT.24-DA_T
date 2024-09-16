import pandas as pd
import matplotlib.pyplot as plt

# Data used within the matplot lib session

# Can be distributed in the session to save anyone having to type out reems of data

# -----------------------------------------------------------------------------------
#                                  Bar Chart Data
# -----------------------------------------------------------------------------------

df = pd.DataFrame({
    "Locations" : [
    "Twitter",
    "Facebook",
    "LinkedIn",
    "Indeed",
    "Instagram"
],
    "Responses" : [3,11,16,13,2],
})

# -----------------------------------------------------------------------------------
#                                  Stacked Bar Chart Data
# -----------------------------------------------------------------------------------

df = pd.DataFrame({
    "Engineering":[56,13,1],
    "Computer Science":[77,23,4],
    "English Lit":[35,48,9],
    "Economics": [65,45,19]
}, index=["Male", "Female", "Non-Binary"])

# -----------------------------------------------------------------------------------
#                                  Pie Chart Data
# -----------------------------------------------------------------------------------

roles = [    
    "Front-end", 
    "Back-end",
    "Full-stack",
    "DevOps"
    ]

employees = [52,36,28,11]

# -----------------------------------------------------------------------------------
#                                  Scatter
# -----------------------------------------------------------------------------------

number_of_placements=list(range(1,11))
responses_received = [14, 21, 34, 36, 45, 51, 54, 63, 78, 92]


# -----------------------------------------------------------------------------------
#                             Box Plots and Histogram Data
# -----------------------------------------------------------------------------------

dev_ages=[
        45, 23, 57, 27, 37, 39, 61, 48, 23, 27, 
        59, 60, 28, 41, 25, 39, 22, 46, 48, 52, 
        38, 41, 52, 30, 46, 62, 25, 34, 52, 35, 
        48, 43, 21, 40, 22, 22, 57, 25, 21, 30, 
        55, 50, 54, 30, 43, 40, 53, 46, 36, 61, 
        35, 39, 40, 31, 29, 65, 28, 57, 39, 36, 
        20, 49, 42, 29, 62, 52, 29, 57, 39, 32
        ]