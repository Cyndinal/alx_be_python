from datetime import datetime,timedelta
# “YYYY-MM-DD HH:MM:SS”.
def display_current_datetime():
    current_time = datetime.now()
    current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time {current_time}")

def calculate_future_date():
    time_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=time_add)
    future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date {future_date}")



display_current_datetime()
calculate_future_date()