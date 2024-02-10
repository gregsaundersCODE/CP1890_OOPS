from datetime import datetime, date, time

date_today= date.today()
print(date_today)
datetime_now = datetime.now()

halloween = date(year=2024,  month=10, day= 5)
print(halloween)
print(type(halloween))

meeting = time (hour=23, minute=59, second=59)
print(meeting)
print(type(meeting))

appointment = time (hour=2, minute=45, second=45)
print(appointment)
print(type(appointment))

print(halloween.day)
print(halloween.month)
print(halloween.year)
print(meeting.hour)
print(meeting.minute)
print(appointment.hour)
print(appointment.minute)

