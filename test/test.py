# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: henry
# Created Time: 2020/1/2 10:54
import sys
import time
import datetime
sys.path.append("..")
from pytimelib import TimeLib


if __name__ == "__main__":

    # timestamp and timeString
    print("testing timestamp to timeString:")
    timestamp = int(time.time())
    time_str = TimeLib.timestamp_to_str(timestamp)
    print(time_str)
    print("testing timeString to timestamp:")
    timestamp = TimeLib.time_str_to_timestamp(time_str)
    print(timestamp)

    # datetime and timeString
    print("testing datetime to timeString:")
    date_time = datetime.datetime.now()
    time_str = TimeLib.datetime_to_datetime_str(date_time)
    print(time_str)
    print("testing timeString to datetime:")
    date_time = TimeLib.datetime_str_to_datetime(time_str)
    print(date_time)

    # datetime and timestamp
    date_time = datetime.datetime.now()
    print("testing datetime to timestamp:")
    timestamp = TimeLib.datetime_to_timestamp(date_time)
    print(timestamp)
    print("testing timestamp to datetime:")
    date_time = TimeLib.timestamp_to_datetime(timestamp)
    print(date_time)

    # timestamp and timeString by timezone
    print("testing timestamp to timeString by timezone(UTC to Los Angeles):")
    timestamp = int(time.time())
    time_str = TimeLib.timestamp_to_str_by_timezone(
        timestamp, to_tz="America/Los_Angeles")
    print(time_str)
    print("testing timeString to timestamp by timezone(Los Angeles to UTC):")
    timestamp = TimeLib.time_str_to_timestamp_by_timezone(
        time_str, from_tz="America/Los_Angeles")
    print(timestamp)

    # datetime and timeString by timezone
    print("testing datetime to timeString by timezone(UTC to Los Angeles):")
    date_time = datetime.datetime.utcnow()
    time_str = TimeLib.datetime_to_datetime_str_by_timezone(date_time, to_tz="America/Los_Angeles")
    print(time_str)
    print("testing timeString to datetime by timezone(Los Angeles to UTC):")
    date_time = TimeLib.datetime_str_to_datetime_by_timezone(
        time_str, from_tz="America/Los_Angeles", to_tz="UTC")
    print(date_time)

    # datetime and timestamp by timezone
    date_time = datetime.datetime.utcnow()
    print(date_time)
    print("testing datetime to timestamp by timezone(UTC to Los Angeles):")
    timestamp = TimeLib.datetime_to_timestamp_by_timezone(date_time,
                                                          from_tz="UTC")
    print(timestamp)
    print("testing timestamp to datetime by timezone(UTC to Los Angeles):")
    date_time = TimeLib.timestamp_to_datetime_by_timezone(
        timestamp, to_tz="America/Los_Angeles")
    print(date_time)
