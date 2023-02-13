# import datetime
# from datetime import  date
# d1=datetime.datetime.now()
# print(d1)
# d2=d1.strftime('%d/%m/%Y')
# print(d2)
# today=date.today()
# print(today)
#
# timestamp = date.fromtimestamp(1326244364)
# print("Date =", timestamp)

# for more info see (https://www.programiz.com/python-programming/datetime)
# from datetime import time
#
# t1=time(11,23,9)
# print(t1)
# t2=time(11,23,6,20)
# print(t2)



# from datetime import datetime
#
# # datetime(year, month, day)
# a = datetime(2022, 12, 28)
# print(a)
#
# # datetime(year, month, day, hour, minute, second, microsecond)
# b = datetime(2022, 12, 28, 23, 55, 59, 342380)
# print(b)


# from datetime import datetime,time
# d1=datetime(2018,7,12,7,9,33)
# d2=datetime(2019,6,10,5,55,13)
# print(d1,d2)
# print(type(d1))
# d3=d1-d2
# print(d3)
# print(type(d3))


# from datetime import timedelta
#
# t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
# print("Total seconds =", t.total_seconds())


from datetime import datetime

# # current date and time
# now = datetime.now()
#
# t = now.strftime("%H:%M:%S")
# print("Time:", t)
#
# s1 = now.strftime("%m/%d/%y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("s1:", s1)
#
# s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("s2:", s2)
# print(type(s2))

d1=datetime.now()
d2=d1.strftime("%Z")
print((d2))
