import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

try:
    num_engineers = 10
    data = []
    start_date = datetime.now() - timedelta(days=30)
    for day in range(30):
        date = start_date + timedelta(days=day)
        day_of_week = date.strftime('%A')
        for engineer_id in range(1, num_engineers + 1):
            name = f"Engineer_{engineer_id}"
            status = random.choice(["Present", "Absent"])
            login_time = (datetime.combine(date, datetime.min.time()) + timedelta(hours=random.randint(7, 10))).time() if status == "Present" else None
            logout_time = (datetime.combine(date, datetime.min.time()) + timedelta(hours=random.randint(16, 19))).time() if status == "Present" else None
            work_hours = ((datetime.combine(datetime.today(), logout_time) - datetime.combine(datetime.today(), login_time)).seconds // 3600) if status == "Present" else 0
            remarks = random.choice(["", "Worked remotely", "Attended a meeting"]) if status == "Present" else "On leave"
            
            data.append([engineer_id, name, date.date(), day_of_week, status, login_time, logout_time, work_hours, remarks])

    df = pd.DataFrame(data, columns=["Engineer ID", "Name", "Date", "Day", "Status", "Login Time", "Logout Time", "Work Hours", "Remarks"])

    os.makedirs('data', exist_ok=True)

    output_file = 'data/attendance_data.csv'
    df.to_csv(output_file, index=False)
    
    if os.path.isfile(output_file):
        print(f"File '{output_file}' created successfully.")
    else:
        print(f"Failed to create the file '{output_file}'.")
    
    print(df)

except Exception as e:
    print(f"An error occurred: {e}")
