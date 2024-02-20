# Dates #
from datetime import datetime

now = datetime.now ()
def print_date (date):
    print (date.year)
    print (date.month)
    print (date.day)
    print (date.hour)
    print(date.timestamp ())

print_date (now) 
print ("Ahora time")


year_2025 = datetime (2025,1,1)

print_date (year_2025)

from datetime import time

current_time = time (21,9,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print ("Ahora fecha")

from datetime import date

current_date = date.today ()

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date (2024,4,13)
print(current_date.day)
print(current_date.month)
print(current_date.year)


current_date = date (current_date.year,current_date.month,current_date.day +1)

print (current_date.day)

print (year_2025 - now)
diff = year_2025.date () - current_date
print (diff)

print (year_2025.time())

from datetime import timedelta
#h

star_delta = timedelta (200,100,100,weeks=30)
end_delta = timedelta (300,100,100,weeks=35)
print (end_delta + star_delta)
print (end_delta - star_delta)