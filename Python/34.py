import calendar

month, day, year = map(int,input().split())
week_day = calendar.weekday(year,month,day)
d = dict()
d = { 
    0:"MONDAY",
    1:"TUESDAY",
    2:"WEDNESDAY",
    3:"THURSDAY",
    4:"FRIDAY",
    5:"SATURDAY",
    6:"SUNDAY",
    }
print(d[week_day])