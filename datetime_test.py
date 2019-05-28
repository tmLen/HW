from datetime import datetime, timedelta
#Напечатайте в консоль даты: вчера, сегодня, месяц назад
def print_date(dt, delta=timedelta(days=0)):
    return (dt - delta).strftime('%Y-%m-%d %H:%M:%S')

print(print_date(datetime.now()))
print(print_date(datetime.now(), timedelta(days=1)))
print(print_date(datetime.now(), timedelta(days=30)))


#Превратите строку "01/01/17 12:10:03.234567" в объект datetime
str = '01/01/17 12:10:03.234567'
dt = datetime.strptime(str, '%d/%m/%y %H:%M:%S.%f')
print(dt)