import datetime as dt
import time

# ------------------ Class methods -------------------

print(dt.date.today())

# fromtimestamp
# convert seconds (float num) to date
print(dt.date.fromtimestamp(time.time()))

# fromisoformat
birth_date = dt.date.fromisoformat("1996-11-07")
print(dt.date.today() - birth_date)    # -> timedelta

# ----------------- Instance attributes --------------

print(birth_date.year)
print(birth_date.day)
print(birth_date.month)

# ------------------ Instance methods -------------------

# replace()
print(birth_date.replace(year=2010))

# timetuple()
# Return a time.struct_time such as returned by time.localtime()
print(birth_date.timetuple())

print(birth_date.weekday())

# ctime
print("ctime: ", birth_date.ctime())

# strftime
print(birth_date.strftime("%Y-%m-%d * %A"))


