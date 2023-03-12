import datetime as dt

# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

print(dt.datetime(2015, 11, 7, 14, 20, 19))   # -> datetime object

print(dt.datetime.today())
print(dt.datetime.now(), " -- ", dt.datetime.now(dt.timezone.utc))
print(dt.datetime.utcnow())

dtn = dt.datetime.now(dt.timezone.utc)
print(dtn.date())
print(dtn.time())
print(dtn.timetz())
