import datetime

print(f"Print Current Date and Time : ",datetime.datetime.now())
print(f"Print Todays Date : ",datetime.datetime.today())
dt=datetime.datetime.now()
print("Hour:",dt.hour, "Minute:", dt.minute,"Second:", dt.second,"Microsecond",dt.microsecond)
print("Day:",dt.day,"Month:",dt.month,"Year",dt.year)

print("Customize Date:",datetime.date(2023,2,2))
print("Customize Time: ",datetime.time(10,10,10))

print(dt.strftime("%m-%d-%Y %H:%M:%S %A %B"))

print(datetime.datetime.now() + datetime.timedelta(days=30))


