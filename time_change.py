#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hours = int(s[0] + s[1])
    minutes = int(s[3] + s[4])
    seconds =  int(s[6] + s[7])
    am_pm = s[8] + s[9]
    
    if am_pm == 'AM' and hours == 12:
        hours = 0
    if am_pm == 'PM' and hours < 12:
        hours += 12
    
    return '%02d:%02d:%02d' % (hours, minutes, seconds)

 
print(timeConversion('12:00:01AM'))
print(timeConversion('12:00:01PM'))
print(timeConversion('01:00:01PM'))
