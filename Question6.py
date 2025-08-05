"""
 6. Exception Handling in Real World
 You are processing 1000 Excel files. Occasionally, a file is corrupted or missing some columns.
 Task: Write a Python function that opens each file, reads specific columns, and logs an error if
 something fails without stopping the entire process
"""

import pandas as pd
file = ['file1.csv']
try:
    df = pd.read_csv(file)
    print(df.head())
except Exception as e:
    print("Error", e)