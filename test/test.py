# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: henry
# Created Time: 2020/1/2 10:54
import sys
import time
import datetime
sys.path.append("..")
import pytimelib


if __name__ == "__main__":

    # timestamp and timeString
    print("testing timestamp to timeString:")
    timestamp = int(time.time())
    time_str = pytimelib.TimeLib.timestamp_to_str(timestamp)
    print(time_str)
    print("testing timeString to timestamp:")
    timestamp = pytimelib.TimeLib.time_str_to_timestamp(time_str)
    print(timestamp)

    # datetime and timeString
    print("testing datetime to timeString:")
    date_time = datetime.datetime.now()
    time_str = pytimelib.TimeLib.datetime_to_datetime_str(date_time)
    print(time_str)
    print("testing timeString to datetime:")
    date_time = pytimelib.TimeLib.datetime_str_to_datetime(time_str)
    print(date_time)

    # datetime and timestamp
    print("testing datetime to timestamp:")
    timestamp = pytimelib.TimeLib.datetime_to_timestamp(date_time)
    print(timestamp)
    print("testing timestamp to datetime:")
    date_time = pytimelib.TimeLib.timestamp_to_datetime(timestamp)
    print(date_time)

