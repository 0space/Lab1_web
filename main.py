#!/usr/bin/python3

import re
import datetime

LOG_NAME = 'log.txt'

stat_1 = [0] * 24

def str_to_date(string):
    datetime_object = datetime.datetime.strptime(string, '%d/%b/%Y:%H:%M:%S')
    return datetime_object

def main():
    r = re.compile(r"([\d.:]*) - - \[([\w/:]+) \+([\d]+)\] \"([^\"]+?)\" ([\d]+) ([\d]+) \"([^\"]+?)\" \"([^\"]+?)\"")
    f = open(LOG_NAME, 'r')
    messages = f.readlines()
    for m in messages:
        s = re.match(r, m)
        if s:
            date = str_to_date(s.group(2))
            stat_1[date.hour] += 1
            continue
            print(s.groups())
        else: 
            print('ANOMALY FOUND: {}'.format(m))
            continue
            # break

if __name__ == "__main__":
    # m = "\"GET / HTTP/1.1\""
    # r = re.compile(r"\"([\w\s/.]+?)\"")
    # s = re.match(r, m)
    # print(s.groups())
    # s = '22/Feb/2018:09:03:22'
    # str_to_date(s)
    main()
    print(stat_1)