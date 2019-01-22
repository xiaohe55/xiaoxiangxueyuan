# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:日期和时间

import time
import datetime

# 获取当前时间戳，单位秒
# print(time.time())

# 获取当前时间的时间元祖
# print(time.localtime(time.time()))
# 获取时间戳格式化的时间元祖
# print(time.localtime(1546491662))

# 格式化当前时间元祖
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 格式化制定时间元祖
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1546491662)))

# print(time.strptime("2019-01-21 08:20:08", "%Y-%m-%d %H:%M:%S"))

# print(time.mktime(time.strptime("2019-01-21 08:20:08", "%Y-%m-%d %H:%M:%S")))

# sleep(秒)程序睡眠时间
'''
start_time = time.time()
time.sleep(5)
end_time = time.time()
print(end_time-start_time)
'''

# 获取当前时间
# print(datetime.datetime.now())
# 时间格式化
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# 计算时间差值
'''
start_time = datetime.datetime.now()
time.sleep(2)
end_time = datetime.datetime.now()
print(end_time-start_time)
print((end_time-start_time).seconds)
'''

# ts = time.time() #当前时间戳
# print(ts)
# print(datetime.datetime.fromtimestamp(ts))

# 计算昨天日期
'''
today = datetime.datetime.today()
print(today.strftime("%Y-%m-%d %H:%M:%S"))
timedelta = datetime.timedelta(days=1)
yesterday = today-timedelta
print(yesterday.strftime("%Y-%m-%d %H:%M:%S"))
'''

