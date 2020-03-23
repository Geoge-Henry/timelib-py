# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: henry
# Created Time: 2019/12/31 14:35

import datetime
import time
from pytz import timezone as tz
import arrow


class TimeLib(object):

    @staticmethod
    def time_str_to_timestamp(time_string, _format="%Y-%m-%d %H:%M:%S"):
        """
        String to timestamp, time_string's default time zone is server timezone
        @:param time_string string
        @:param _format string, default:%Y-%m-%d %H:%M:%S
        """
        return int(time.mktime(time.strptime(time_string, _format)))

    @staticmethod
    def time_str_to_timestamp_by_timezone(time_string,
                                          _format="%Y-%m-%d %H:%M:%S",
                                          from_tz="UTC"):
        """
        String to timestamp according to timezone
        @:param time_string string
        @:param _format string, default:%Y-%m-%d %H:%M:%S
        @:param from_tz string, default:UTC+0
        """
        arrow_time = arrow.get(datetime.datetime.strptime(
            time_string, _format), from_tz).to("UTC")
        return int(arrow_time.timestamp)

    @staticmethod
    def timestamp_to_str(timestamp, _format="%Y-%m-%d %H:%M:%S"):
        """
        Timestamp to string, return time_string's default timezone is server
        timezone
        @:param timestamp int
        @:param _format string, default:%Y-%m-%d %H:%M:%S
        """
        return time.strftime(_format, time.localtime(timestamp))

    @staticmethod
    def timestamp_to_str_by_timezone(timestamp, _format="%Y-%m-%d %H:%M:%S",
                                     to_tz="Asia/Shanghai"):
        """
        Timestamp to string according to timezone(support dst)
        @:param timestamp int
        @:param _format string, default:%Y-%m-%d %H:%M:%S
        @:param to_tz string, default:Asia/Shanghai
        """
        to_tz = tz(to_tz)
        return str(datetime.datetime.fromtimestamp(timestamp, to_tz).strftime(
            _format))

    @staticmethod
    def datetime_str_to_datetime(time_string, _format="%Y-%m-%d %H:%M:%S"):
        """
        String to datetime, return datetime's default timezone is local server
        timezone
        @:param time_string string
        @:param _format string, default:%Y-%m-%d %H:%M:%S
        """
        return datetime.datetime.strptime(time_string, _format)

    @staticmethod
    def datetime_str_to_datetime_by_timezone(time_string, from_tz="UTC",
                                             to_tz="Asia/Shanghai",
                                             _format="%Y-%m-%d %H:%M:%S", ):
        """
        String to datetime according to timezone
        @:param time_string string
        @:param from_tz string, default:UTC+0
        @:param to_tz string, default:Asia/Shanghai
        @:param _format string, default:%Y-%m-%d %H:%M:%S
        """
        arrow_time = arrow.get(datetime.datetime.strptime(
            time_string, _format), from_tz).to(to_tz)
        return arrow_time.datetime

    @staticmethod
    def datetime_to_datetime_str(date, _format="%Y-%m-%d %H:%M:%S"):
        """
        Datetime to string, datetime's default timezone is local server timezone
        @:param date datetime
        @:param _format string, default:%Y-%m-%d %H:%M:%S
        """
        return date.strftime(_format)

    @staticmethod
    def datetime_to_datetime_str_by_timezone(date, from_tz="UTC",
                                             to_tz="Asia/Shanghai",
                                             _format="%Y-%m-%d %H:%M:%S"):
        """
        Datetime to string according to timezone
        @:param date datetime
        @:param from_tz string, default:UTC+0
        @:param to_tz string, default:Asia/Shanghai
        @:param _format string, default:%Y-%m-%d %H:%M:%S
        """
        from_tz = tz(from_tz)
        to_tz = tz(to_tz)
        date = date.replace(tzinfo=from_tz).astimezone(to_tz)
        return date.strftime(_format)

    @staticmethod
    def datetime_to_timestamp(date):
        """
        Datetime to timestamp, datetime's default timezone is server timezone
        @:param date datetime
        """
        return int(time.mktime(date.timetuple()))

    @staticmethod
    def datetime_to_timestamp_by_timezone(date, from_tz="Asia/Shanghai"):
        """
        Datetime to timestamp according to timezone
        @:param date datetime
        @:param from_tz string, default:Asia/Shanghai
        """
        arrow_time = arrow.get(date, from_tz).to("UTC")
        return int(arrow_time.timestamp)

    # 时间戳转datetime
    @staticmethod
    def timestamp_to_datetime(time_stamp):
        """
        Timestamp to datetime, return datetime's default timezone is local
        server timezone
        @:param time_stamp timestamp
        """
        return datetime.datetime.fromtimestamp(time_stamp)

    @staticmethod
    def timestamp_to_datetime_by_timezone(time_stamp, to_tz="Asia/Shanghai",
                                          _format="%Y-%m-%d %H:%M:%S"):
        """
        Timestamp to datetime according to timezone
        @:param time_stamp timestamp
        @:param to_tz string, default:Asia/Shanghai
        """
        to_tz = tz(to_tz)
        return datetime.datetime.fromtimestamp(time_stamp, to_tz)
