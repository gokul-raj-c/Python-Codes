"""1. File Parsing & Data Extraction
 You are given a `.txt` file containing logs in the format:
 [2024-05-10 10:02:01] ERROR: Sensor disconnected
 [2024-05-10 10:05:22] INFO: Reconnected successfully
 Task: Write a script to extract all timestamps and corresponding error messages.
 """

with open('sample_logs.txt','r') as file:
    for x in file:
        if 'ERROR' in x:
            print(x)
