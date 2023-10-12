from datetime import datetime, timedelta

date_time_format = "%d-%m-%Y"
date_01 = "01-10-1999"  

#Turns string into a date object
date_01_obj = datetime.strptime(date_01, date_time_format)
day_of_week = date_01_obj.strftime('%A')


#Takes in a date object and returns the weekday
def get_weekday (convert_date):
    day_of_week = convert_date.strftime('%A')
    return day_of_week


answer_a = get_weekday(date_01_obj)
print("--------------------------------------------")
print("a)")
print(answer_a)
print("--------------------------------------------")
print("b)")


date_02_obj = date_01_obj
removed_weeks = 7*27
date_02_obj -= timedelta(removed_weeks)
answer_b = get_weekday(date_02_obj)
print(answer_b)
print("--------------------------------------------")


date_03_obj = date_01_obj
added_days = 157
date_03_obj += timedelta(added_days)
answer_c = get_weekday(date_03_obj)
print("c)")
print(answer_c)
print("--------------------------------------------")