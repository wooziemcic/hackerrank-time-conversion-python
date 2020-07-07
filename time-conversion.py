#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = int(s[:2])
    if 'AM' in s:
       if time == 12:
            time = "00"
            s = time + s[2:-2]
            return s
       else:
        return s.replace("AM","")
    else:
        if time == 12:
            return s.replace("PM","")
        else:
            time += 12
            return str(time) + s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
