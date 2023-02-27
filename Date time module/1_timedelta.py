import datetime as dt

# timedelta:  A duration expressing the difference between two date, time, or datetime instances
# to microsecond resolution.

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# date and date      -> timedelta
# date and timedelta -> date

a = dt.timedelta(35.12, 20)
print(a)

ts = a.total_seconds()
print(ts)
