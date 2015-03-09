#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
'''
    Author : xiequnqun@jd.com
    Date   : 20140919
    
'''
import time
from datetime import datetime
from datetime import timedelta


def getNowDeltaDays(delta):
    d1 = datetime.now()
    d2 = d1 + timedelta(days = delta)
    deltaDate = d2.strftime("%Y%m%d")
    return str(deltaDate)
    
def getStartDeltaDays(now_time,delta):
    d2 = now_time + timedelta(days = delta)
    deltaDate = d2.strftime("%Y%m%d")
    return str(deltaDate)

#print getNowDeltaDays(-1)

def Str2Datetime(strt):
    return datetime.strptime(strt,'%Y%m%d')
'''
print Str2Datetime('20141029')
'''
def Datetime2Time():
    pass

def Time2Str():
    "2014-10-30 10:32:00"
    print time.strftime('%Y-%m-%d %H:%M:00',time.localtime(time.time()))
    

def Str2Time():
    print time.strptime('2014-10-30',"%Y-%m-%d")
    
   

def TimeStamp2Time():
    timeArray = time.localtime(1414550549)
    print timeArray

#把datetime转成字符串  
def datetime_toString(dt):  
    return dt.strftime("%Y-%m-%d-%H")  

#把字符串转成datetime  
def string_toDatetime(string):  
    return datetime.strptime(string, "%Y-%m-%d-%H")  

#把字符串转成时间戳形式  
def string_toTimestamp(strTime):  
    return time.mktime(string_toDatetime(strTime).timetuple())  

#把时间戳转成字符串形式  
def timestamp_toString(stamp):  
    return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))  

#把datetime类型转外时间戳形式  
def datetime_toTimestamp(dateTim):  
    return time.mktime(dateTim.timetuple())


def getOneYear(year):
    start = str(year)+"0101"
    day_set = []
    start = datetime.strptime(start,'%Y%m%d')
    for i in range(0,365):
        day = getStartDeltaDays(start,i)
        day_set.append(day)
    return day_set

def getDetailTime():
        timeStamp = time.time() - 60*60*24*25
        cur_time = time.strftime('%Y-%m-%d %H:%M:00',time.localtime(timeStamp))
        print cur_time
        date = time.strftime('%Y%m%d',time.localtime(timeStamp))
        print date
        mim =time.strftime('%M',time.localtime(timeStamp))
        print mim
        hour = time.strftime('%H',time.localtime(timeStamp))
        print hour
        day = time.strftime('%d',time.localtime(timeStamp))
        print day
        
def getNowDeltaMinutes(delta):
    d1 = datetime.now()
    d2 = d1 + timedelta(minutes = delta)
    print d1
    print d2
    deltaDate = d2.strftime("%Y%m%d %H:%M:%S")
    return str(deltaDate)

#分钟递增
def getStartDeltaMinutes(start,delta):
    result = start + timedelta(minutes = delta)
    return result

#获取按照分钟递增的值
def GenIntervalByMinuter(start,end):
    time_set = []
    start = datetime.strptime(start,'%Y-%m-%d %H:%M')
    end   = datetime.strptime(end,'%Y-%m-%d %H:%M')
    cur_time = start 
    while 1:
        cur_time = getStartDeltaMinutes(cur_time,1)
        #time_struct = time.strptime(str(cur_time),'%Y-%m-%d %H:%M:%S')
        time_set.append(cur_time)
        if cur_time == end:
            print "end"
            break
    return time_set
      
print "minute test"       
#time_set = GenIntervalByMinuter("2014-11-01 14:00","2014-11-01 14:59")
#获取按天递增的时间值
def GenIntervalByMinuter(start,end):
    time_set = []
    start = datetime.strptime(start,'%Y-%m-%d %H:%M')
    end   = datetime.strptime(end,'%Y-%m-%d %H:%M')
    cur_time = start 
    while 1:
        cur_time = getStartDeltaMinutes(cur_time,1)
        #time_struct = time.strptime(str(cur_time),'%Y-%m-%d %H:%M:%S')
        time_set.append(cur_time)
        if cur_time == end:
            print "end"
            break
    return time_set


   
