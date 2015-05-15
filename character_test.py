#!/usr/bin/env python
#-*- coding: gbk -*-
#
'''
    Author : xiequnqun@jd.com
    Date   : 20150513
    
'''

import os
import sys

# print default code 
print "[use file encode]"
chStr = '测'
print chStr
print(' '.join(format(ord(x), 'b') for x in chStr))

# convert gbk to utf 
print "[gbk to utf]"
cUtfStr = chStr.decode("gbk")
print cUtfStr
print(' '.join(format(ord(x), 'b') for x in cUtfStr)) 

# with prefix u the str is convert to utf
print "[string with prefix unicode]"
utfStr = u"测"
print utfStr
print(' '.join(format(ord(x), 'b') for x in utfStr)) 

# convert utf to gbk
print "[utf to gbk]"
cGbkStr = utfStr.encode("gbk")
print cGbkStr
print(' '.join(format(ord(x), 'b') for x in cGbkStr)) 

'''
  conclusions"
  1.coding: gbk it specified the file code type used by python complier
  2.encode,decode function return unicode strings  decode means convert to utf  
    while encode means convert utf to specified character set
'''
