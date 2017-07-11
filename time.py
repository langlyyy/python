
import datetime

i = datetime.datetime.now()

print("当前的日期和时间是 %s" % i)

print('ISO格式的日期和时间是 %s' % i.isoformat())

print("当前的年份是 %s" % i.year)
print("当前的月份是 %s" % i.month)
print("当前的日期是 %s" % i.day)

print('dd/mm/yyyy 格式是 %s/%s/%s' % (i.day, i.month, i.year))

print('当前小时是 %s' % i.hour)
print('当前分钟是 %s'% i.second)


#获取三天前的时间
threeDayago = (datetime.datetime.now()-datetime.timedelta(days=3))
print(threeDayago)

#给定时间戳，计算该时间的几天前时间
timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threedateArray = dateArray -datetime.timedelta(days=0)
print(threedateArray)




