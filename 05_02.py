from datetime import date, time ,datetime, timedelta
import pytz
import time

date_time_format = "%Y-%m-%d %H:%M:%S"
date_01 = "2020-09-28  18:47:50"
date_time_obj_1 = datetime.strptime(date_01, date_time_format)
date_time_obj_2 = datetime.strptime(date_01, date_time_format)

#Prints all date values separately
print("--------------------------------------------")
print("Year " + str(date_time_obj_1.year))
print("Month " + str(date_time_obj_1.month))
print("Day " + str(date_time_obj_1.day))
print("Hour " + str(date_time_obj_1.hour))
print("--------------------------------------------")

#Adds +1 Year, +1 Month, +1 Day and +1 Hour to the time
date_time_obj_2 += timedelta(days=365)
date_time_obj_2 += timedelta(days=30)
date_time_obj_2 += timedelta(days=1)
date_time_obj_2 += timedelta(hours=1)

# Creates strings  of all time values
date_01_year = str(date_time_obj_2.year)
date_01_month = str(date_time_obj_2.month)
date_01_day = str(date_time_obj_2.day)
date_01_hour = str(date_time_obj_2.hour)
date_01_minute = str(date_time_obj_2.minute)
date_01_second = str(date_time_obj_2.second)

print("After adding 1 year, 1 month, 1 day and 1 hour")
print(date_01_year + "-" + date_01_month + "-" + date_01_day + " " + date_01_hour + ":" + date_01_minute + ":" + date_01_second)
print("--------------------------------------------")
print("It's year " + date_01_year + ", day " + date_01_day + " of month " + date_01_month + " and it is " + date_01_hour + ":" + date_01_minute + ":" + date_01_second + ".")
print("--------------------------------------------")
