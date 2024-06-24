from datetime import datetime, timedelta

def add_time(feet, inches):
    total_inches = feet * 12 + inches
    days = total_inches // 24
    hours = (total_inches % 24) // 1
    minutes = (total_inches % 1) * 60
    
    new_time = datetime.now() + timedelta(days=days, hours=hours, minutes=minutes)
    print("New time after adding feet and inches:", new_time)

# Example usage
datetime_object = datetime.now()
print("Current datetime:", datetime_object)
add_time(5, 8)
