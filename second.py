def hello(name,age) :
  {  print(f'{name} is {age} years old') }
hello('Dhruv',18)

def student_info(*args,**kwargs) :
    print(args)
    print(kwargs)

classes = ['Math','Sci']
info = {'name':'dhruv','age':18}
student_info(*classes,**info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):   
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def days_in_month(year, month):
   
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))

import os
print(os.__file__)

