import datetime

print(datetime.datetime.now())
print(datetime.datetime.today())
dt=datetime.datetime.now()
print(dt.day,dt.time(),dt.weekday(),dt.date(),dt.hour,dt.minute,dt.month,dt.second,dt.microsecond)
print(datetime.date(2023,1,2))
print(datetime.time(10,10,10))
print(datetime.datetime(2023,1,1,10,10,10))
print(dt.strftime("%H:%M:%S %m/%d/%y %A %B "))

print(datetime.date.today() + datetime.timedelta(days=7))
print(datetime.datetime.today() + datetime.timedelta(hours=5,minutes=30))