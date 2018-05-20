#!/usr/bin/python3

import datetime
import geolite2
import re

LOG_NAME = 'log.txt'

stat_1 = [0] * 24
stat_2 = dict()
stat_4 = dict()

def str_to_date(string):
    datetime_object = datetime.datetime.strptime(string, '%d/%b/%Y:%H:%M:%S')
    return datetime_object

def get_country_name(s_ip):
    if not s_ip:
        return None
    reader = geolite2.geolite2.reader()
    if not reader:
        return None
    data = reader.get(s_ip)
    geolite2.geolite2.close()
    if data and 'country' in data:
        country = data['country']['names']['en']
        return country

def get_user_agents(string):
    # s = string.split()
    # print(string)
    ret = list()
    for s in string.split('('):
        ret += (s.split(')')[-1].split())
    return ret
    # r = re.compile(r"[(?:\(([^)]*?)\))]*")
    # s = re.match(r, string)
    # if s:
    #     print(s.groups())

def get_os(string):
    # s = string.split()
    # print(string)
    # ret = list()
    # for s in string.split('('):
    #     ret += (s.split(')')[-1].split())
    # print(ret)
    # return ret
    r = re.compile(r"([^\)]*?)")
    s = re.match(r, string)
    if s:
        print(s.groups())
    # r = re.compile(r"[(?:\(([^)]*?)\))]*")
    # s = re.match(r, string)
    # if s:
    #     print(s.groups())

def main():
    r = re.compile(r"([\d.:]*) - - \[([\w/:]+) \+([\d]+)\] \"([^\"]+?)\" ([\d]+) ([\d]+) \"([^\"]+?)\" \"([^\"]+?)\"")
    f = open(LOG_NAME, 'r')
    messages = f.readlines()
    for m in messages:
        s = re.match(r, m)
        if s:
            # task 1
            date = str_to_date(s.group(2))
            stat_1[date.hour] += 1
            # task 2
            for i in get_user_agents(s.group(8)):
                if not i in stat_2:
                    stat_2[i] = 0
                else:
                    stat_2[i] += 1
            # get_os(s.group(8))
            # task 4
            country = get_country_name(s.group(1))
            if not country:
                print('BOT FOUND: ip=[{}]'.format(s.group(1)))
            elif not country in stat_4:
                stat_4[country] = 0
            else:
                stat_4[country] += 1
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
    print('TASK 1')
    print(stat_1)
    print('TASK 2')
    print(stat_2)
    print('TASK 4')
    print(stat_4)
    # s = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
    # get_os(s)