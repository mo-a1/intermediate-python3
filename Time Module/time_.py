import time

# NOTE :-
# struct_time: it is an object with a named tuple interface so values can be accessed by index and by attribute name.
# attributes: tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst

# time tuple => (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)
# ____________________________________________________________________________________
# method     |         input             | output
# ___________|___________________________|____________________________________________
# strftime   : time tuple | struct_time -> string
# asctime    : time tuple               -> string
# strptime   : string                   -> struct_time
# time       :                          -> float (current time in seconds)
# monotonic  :                          -> float (current time in seconds)
# gmtime     :                          -> struct_time (current gm time)
# localtime  :                          -> struct_time (current local time)
# _____________________________________________________________________________________

time_tuple = (2022, 11, 7, 14, 22, 10, 0, 0, 0)
t1 = time.asctime(time_tuple)
print("time.asctime: ", type(t1), t1)

print("strftime: ", time.strftime("%d-%m-%Y, %H:%M:%S", time_tuple))

print("strptime: ", time.strptime("7-11-2022", "%d-%m-%Y"))

print("time.time(): ", time.time())

print("gmtime: ", time.strftime("%d-%m-%Y, %H:%M:%S", time.gmtime()))
print("localtime: ", time.strftime("%d-%m-%Y, %H:%M:%S", time.localtime()))

print("monotonic: ", time.monotonic())
