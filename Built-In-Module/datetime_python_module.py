from datetime import datetime, timedelta

today_date_time=datetime.now()
print("Print Todays Date and Time :",today_date_time)
#print("Print Todays UTC Date and Time :",datetime.utcnow())
print("Print Date :",today_date_time.date())
print("Print Time :",today_date_time.time())
print("Print Today's Date and Time :",today_date_time.today())
print("formated date : ",today_date_time.strftime("%d/%m/%y"))
print("formated Time : ",today_date_time.strftime("%H:%M:%S"))
print("formated date and Time : ",today_date_time.strftime("%d/%m/%y %H:%M:%S"))

with open("log_file.txt","a") as file_name:
    file_name.write(f"{datetime.now().strftime("%d-%m-%y %H:%M:%S")} - Inserting id:00012 customer data into Database\n")

print("calculating current date + next 10 day : ",datetime.now() - timedelta(days=10))
print("Print only Year :",datetime.now().year)
print("Print only Day :",datetime.now().timestamp())