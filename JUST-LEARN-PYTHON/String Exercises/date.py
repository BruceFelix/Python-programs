# Display date, month and year form 10-Jan-2020
# import time
# seconds = time.time()
# local_time = time.ctime(seconds)
# print(local_time) this returns the current time and date
date_str = '10-Jan-2020'
d,m,y = date_str.split("-")
print('date: {0} month: {1} year: {2}'.format(d,m,y))