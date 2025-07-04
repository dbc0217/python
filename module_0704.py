from datetime import datetime,date,timedelta
halloween = date(2025,10,31)
print(halloween,type(halloween))
print(halloween.year)
print(halloween.month)
print(halloween.day)
print(halloween.isoformat(),type(halloween.isoformat()))

now_date = date.today()
print(now_date.isoformat())
print(now_date + timedelta(days=1))
print(now_date + timedelta(days=30))

some_day = datetime(2025 , 1 , 2 , 3 , 4 , 5 , 6)
print(some_day)
print(some_day.isoformat())
now_dt = datetime.now()
print(now_dt)
print(now_dt.year)
print(now_dt.month)
print(now_dt.day)
print(now_dt.hour)
print(now_dt.date())
print(now_dt.time())

now_dt = datetime.now()
fmt = "現在是%Y年%m月%d日"
now_string = datetime.strftime(now_dt,fmt)
print(now_string)

date_str = "2025-07-04 14:30:00"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt, type(dt))

import time
now_time = time.time()
for i in range(100000000):
    i
print(time.time()-now_time)