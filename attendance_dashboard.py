import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('data/attendance_data.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Dashboard title
st.title("Engineer Attendance Dashboard")

# Date range filter
st.write("### Select Date Range")
start_date = st.date_input("Start date", df['Date'].min().date())
end_date = st.date_input("End date", df['Date'].max().date())
if start_date > end_date:
    st.error("Error: End date must fall after start date.")
else:
    date_filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

    st.write("### Attendance Data for the Selected Date Range", date_filtered_df)

    # Add "None" to engineer options
    engineer_options = ["None"] + list(date_filtered_df["Name"].unique())
    engineer = st.selectbox("Select Engineer name", engineer_options, index=0)

    if engineer != "None":
        filtered_df = date_filtered_df[date_filtered_df["Name"] == engineer]

        st.write(f"### Attendance Data for {engineer}", filtered_df)

        st.write("### Attendance Summary")
        status_count = date_filtered_df["Status"].value_counts()
        work_hours_summary = filtered_df.groupby("Date")["Work Hours"].sum()

        col1, col2, col3 = st.columns([1, 0.1, 1])

        with col1:
            st.write("Attendance Status Count")
            st.bar_chart(status_count)

        with col3:
            st.write("Work Hours Summary")
            st.line_chart(work_hours_summary)

        st.write("### Work Hours by Day of the Week")
        work_hours_by_day = filtered_df.groupby("Day")["Work Hours"].sum()
        st.bar_chart(work_hours_by_day)
    else:
        st.write("Please select an engineer to see the data.")
