"""
 8. Pandas Analysis
 You are given a CSV of student grades. Some students have missing values.
 Task: Clean the data, fill missing values with the class average, and generate a summary of average
 marks per subject.
"""

import pandas as pd
df = pd.read_csv('data.csv')
count=df.isnull().sum()
if(sum>0):
    df.fillna(df.mean(numeric_only=True), inplace=True)
else:
    print("no missing values")
print(df)

subject_avg = df.drop('Name',axis=1).mean()

print("Average", subject_avg)
