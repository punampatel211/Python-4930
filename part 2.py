from datetime import datetime, timedelta

# Add 1 day
new_time = datetime.now() + timedelta(days=1)
print("Add 1 day:", new_time)

# Subtract 60 seconds
new_time = datetime.now() - timedelta(seconds=60)
print("Subtract 60 seconds:", new_time)

# Add 2 years
new_time = datetime.now() + timedelta(days=365*2)
print("Add 2 years:", new_time)
