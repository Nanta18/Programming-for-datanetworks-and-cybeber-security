from datetime import date, time ,datetime
import pytz
import time

date_1 = "2023-06-12 10:24:47"
date_2 = "2021-10-23 18:56:13"
date_time_format = "%Y-%m-%d %H:%M:%S"
date_time_obj_1 = datetime.strptime(date_1, date_time_format)
date_time_obj_2 = datetime.strptime(date_2, date_time_format)
print("--------------------------------------")
print("a)")
print(date_time_obj_1 - date_time_obj_2) #Counts how much time there is between 2 dates as days, hours, minutes and secconds
print(date_time_obj_1 < date_time_obj_2)
print("--------------------------------------")


time_since_epoch = time.time()
human_readable_time = datetime.fromtimestamp(time_since_epoch)
print("b)")
print("Epoch as secconds " + str(time_since_epoch))
print("Epoch in human readable format " + str(human_readable_time))
# Some of the operations available: type conversions like the datetime above, comparisons between times and timezone conversions 
print("--------------------------------------")