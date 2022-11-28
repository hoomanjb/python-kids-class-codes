# LPIC1  -> linux , os
# DataBase  ->
# GIT & Docker  -> Tools , مدیریت پروژه - ابزار مجازی سازی
# Django -> framework

# asyncio
# multi proces
# threde

# ########################################################
# import adder
# import adder as adr
# from adder import my_adder, my_adder2, name
# from adder import *  # pishnehad nemishe!!!
# import new_dir.new_file
# from new_dir.new_file import divide
#
#
# a = my_adder(5, 7)
# b = my_adder2(6, 8, 2)
# print(a)
# print(b)
# print(name)
#
# print(divide(10, 5))

# ###############################################
from adder import Calculator
# import adder
#
# def my_adder(x, y):
#     return x + y
#
# print(my_adder(6, 7))
# print(adder.my_adder(8, 9))
# cal = adder.Calculator(5, 7)
#
# print(cal.sum())

# ###############################################
import datetime as dt
from datetime import datetime

# now_object = datetime.now()
#
# print(now_object)
# print(type(now_object))
# print(now_object.year)
# print(now_object.month)
# print(now_object + 'yechizi')

from datetime import date, time, datetime, timedelta

# time_obj = time(hour=18, minute=22, second=44)
# tt = '18:22:44'
# print(time_obj)
# print(tt)

# date_obj = date(year=2019, month=10, day=24)
# date_str = '2019-10-24'
# print(date_obj)
# print(date_str)

# a = timedelta(seconds=-122412253)
#
# print(type(a))
# dd = datetime.now()
# b = dd + a
# print(b)


# today = date.today()
# print(today)

# now = datetime.now()
# print(now)
#
# current_time = time(now.hour, now.minute, now.second)
# print(current_time)
#
# result = datetime.combine(today, current_time)
# print(result)


# datetime_str = '01-25-2019 14:10:36'
# format_datetime = '%m-%d-%Y %H:%M:%S'
# result = datetime.strptime(datetime_str, format_datetime)
# print(type(result))


# %m  month  11
# %d  day  05
# %Y  year 2012
# %H  hour 14  0-23
# %M  minute 10
# %S  second 01
# %B  month name August

# x = datetime(year=2018, month=8, day=10, hour=15, minute=45, second=55)
# print(x.strftime('%B'))
# print(x.strftime('%b'))
#
# print(x.strftime('%A'))
# print(x.strftime('%a'))
#
# print(x.strftime('%w')) # weakday from (0-6) 0 is sunday
#
# print(x.strftime('%y'))
#
# print(x.strftime('%I'))  # hour 0-12
#
# print(x.strftime('%p'))
#
# print(x.strftime('%j'))  # day 001-366
#
# print(x.strftime('%U'))  # week number of year


now = datetime.now()
print(now)
# tomorrow +5:+20:+30
yechizi = timedelta(days=-143123)

print(now + yechizi)


