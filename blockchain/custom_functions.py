from datetime import datetime, timedelta, date
import random
import time

from hashlib import sha256



def rndTimeStamp_hourly(year, day_num, number_of_timestamps):
    day_num_str = str(day_num+1)
    day_num_str.rjust(3 + len(day_num_str), '0')
    day_month = datetime.strptime(str(year) + "-" + day_num_str, "%Y-%j").strftime("%m %d")
    start =  datetime(year, int(day_month.split(" ")[0]), int(day_month.split(" ")[1])) + random.uniform(1,1.10) * timedelta(hours=0)
    
    if number_of_timestamps == 1:
        time = start + timedelta(minutes=random.uniform(1,15))
    else:
        time = start + timedelta(minutes=random.uniform(15,45))
    timestamps = [str(time).split(".")[0]]

    for i in range(1, number_of_timestamps):
        nexthour = start + timedelta(hours=i)
        nexttime = nexthour + timedelta(minutes=random.uniform(15, 45))
        timestamps.append(str(nexttime).split(".")[0])
    
    return timestamps