from datetime import datetime
time_format = "%H:%M:%S"
time1 = '6:00:00'
time2 = '12:00:00'
diff_time = datetime.strptime(time2,time_format) - datetime.strptime(time1,time_format)
print (diff_time)
