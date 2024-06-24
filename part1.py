import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date, time, store, item, cost, payment = data
        print("{0}\t{1}".format(item, cost))
