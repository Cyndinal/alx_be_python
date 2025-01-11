from datetime import datetime,timedelta
# “YYYY-MM-DD HH:MM:SS”.
def display_current_datetime():
    current_time = datetime.now()
    print(f"Current date and time {current_time}")

def calculate_future_date():
    time_add = int(input("Enter days to add "))
    future_date = datetime.now() + timedelta(days=time_add)
    print(f"Future date {future_date}")



display_current_datetime()
calculate_future_date()