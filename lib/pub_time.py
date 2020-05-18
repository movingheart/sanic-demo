#!/usr/bin/env python

"""
FileName: time_lib
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 19:38:25
"""


import datetime
import re
import time

from dateutil.relativedelta import relativedelta

FORMAT_TIME_MONTH = "%Y-%m"
FORMAT_DATE = "%Y-%m-%d"
FORMAT_TIME_DAY = "%Y-%m-%d 00:00:00"
FORMAT_TIME_HOUR = "%Y-%m-%d %H:00:00"
FORMAT_TIME_MINUTE = "%Y-%m-%d %H:%M:00"
FORMAT_TIME_SECOND = "%Y-%m-%d %H:%M:%S"
FORMAT_TIME_MICRO_SECOND = "%Y-%m-%d %H:%M:%S.%f"
FORMAT_TIME_ISO = "%Y-%m-%dT%H:%M:%SZ"

TIME_UNIT_SECOND = 1
TIME_UNIT_MINUTE = 2
TIME_UNIT_HOUR = 3
TIME_UNIT_DAY = 4
TIME_UNIT_MONTH = 5
TIME_UNIT_YEAR = 6


def _parse_time_str(time_str: str, fmt: str = None):
    """
    解析时间字符串
    :param time_str:时间字符串
    :param fmt: 指定的时间字符串格式，若无自动判断
    :return:
    """
    if fmt:
        return datetime.datetime.strptime(time_str, fmt)

    if re.match(r'^\d{4}-\d{2}-\d{2}$', time_str):
        t = datetime.datetime.strptime(time_str, '%Y-%m-%d')
    elif re.match(r'^\d{4}-\d{2}$', time_str):
        t = datetime.datetime.strptime(time_str, '%Y-%m')
    elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$', time_str):
        t = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M')
    elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', time_str):
        t = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    elif re.match(r'^\d{8}$', time_str):
        t = datetime.datetime.strptime(time_str, "%Y%m%d")
    elif re.match(r'^\d{10}$', time_str):
        t = datetime.datetime.strptime(time_str, "%Y%m%d%H")
    elif re.match(r'^\d{12}$', time_str):
        t = datetime.datetime.strptime(time_str, "%Y%m%d%H%M")
    elif re.match(r'^\d{14}$', time_str):
        t = datetime.datetime.strptime(time_str, "%Y%m%d%H%M%S")
    else:
        raise ValueError("时间格式错误")

    return t


def convert_time_format(time_str: str, out_format: str, utc=False):
    """
    转换时间字符串格式
    :param time_str: 时间字符串
    :param out_format: 输出的时间格式
    :param utc: 是否使用UTC时间
    :return:
    """
    in_format = ""
    if re.match(r'^\d{4}-\d{2}-\d{2}$', time_str):
        in_format = '%Y-%m-%d'
    elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', time_str):
        in_format = '%Y-%m-%d %H:%M:%S'

    t = _parse_time_str(time_str, in_format)
    if utc:
        t = t + datetime.timedelta(hours=-8)

    return t.strftime(out_format)


def str_add_time(time_str, add_days=0, add_hours=0, add_minutes=0, add_seconds=0, fmt="%Y-%m-%d %H:%M:%S"):
    """
    给一个时间字符串进行时间的增减，返回一个新的时间字符串
    :param time_str: 待增减的时间字符串
    :param add_days: 增加的天数
    :param add_hours: 增加的小时数
    :param add_minutes: 增加的分钟数
    :param add_seconds: 增加的秒数
    :param fmt: 结果字符串的时间格式
    :return:
    """
    t = _parse_time_str(time_str)
    t = t + datetime.timedelta(days=add_days, hours=add_hours, minutes=add_minutes, seconds=add_seconds)
    return t.strftime(fmt)


def timestamp2iso(timestamp: int, z='Z', convert_to_utc: bool = True) -> str:
    """
    时间戳直接转换为iso时间
    :param timestamp: 时间戳，e.g. 1462948788
    :param z: 时间结尾是否带'Z'
    :param convert_to_utc: 是否转化为utc时间
    :return: str
    """
    t = datetime.datetime.utcfromtimestamp(timestamp) if convert_to_utc else datetime.datetime.fromtimestamp(timestamp)
    return t.isoformat() + ".000Z" if z == "Z" else t.isoformat() + ".000"


def timestamp2time_str(timestamp, timestamp_unit="s", time_format=FORMAT_TIME_SECOND):
    """
    时间戳转成时间字符串
    :param timestamp:
    :param timestamp_unit:
    :param time_format:
    :return:
    """
    timestamp = int(timestamp) if timestamp_unit == "s" else int(float(timestamp) / 1000)
    t = datetime.datetime.fromtimestamp(timestamp)
    return t.strftime(time_format)


def time_str2timestamp(time_str: str, timestamp_unit: str = "s") -> int:
    """
    字符串转时间戳
    :param time_str: 时间字符串
    :param timestamp_unit: 时间戳单位，'s'，秒；'ms'，毫秒
    :return: 时间戳，整数
    """
    t = _parse_time_str(time_str)
    timestamp = t.timestamp()
    timestamp = int(timestamp) if timestamp_unit == "s" else int(timestamp * 1000)
    return timestamp


def gen_dates_str(start_date_str: str, end_date_str: str) -> list:
    """
    生成有序的不重复的日期字符串列表
    :param start_date_str: 开始日期，含
    :param end_date_str: 结束日期，含
    :return:
    """
    st = _parse_time_str(start_date_str, FORMAT_DATE)
    et = _parse_time_str(end_date_str, FORMAT_DATE)
    diff_days = (et - st).days + 1
    result = {(st + datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(diff_days)}
    return sorted(result)


def gen_hours_str(start_hour_str, end_hour_str):
    """
    生成小时时间的 set 集合
    :param start_hour_str: 开始日期，含
    :param end_hour_str: 结束日期，含
    :return:
    """
    if re.match("^\d{4}-\d{2}-\d{2}$", start_hour_str):
        st = _parse_time_str(start_hour_str, FORMAT_DATE)
    else:
        st = _parse_time_str(start_hour_str, FORMAT_TIME_HOUR)

    if re.match("^\d{4}-\d{2}-\d{2}$", end_hour_str):
        # 对于输入的日期类型，需要对截止日期加1天
        et = _parse_time_str(end_hour_str, FORMAT_DATE) + datetime.timedelta(days=1)
    else:
        # 对于输入的时间类型，需要对截止时间加1小时
        et = _parse_time_str(end_hour_str, FORMAT_TIME_HOUR) + datetime.timedelta(hours=1)

    diff_hours = int((et - st).days * 24 + (et - st).seconds / 3600)
    result = {(st + datetime.timedelta(hours=x)).strftime(FORMAT_TIME_HOUR) for x in range(diff_hours)}
    return sorted(result)


def gen_5min_str(start_time_str, end_time_str):
    """
    生成 5min 一个时间节点的时间字符串
    :param start_time_str: 开始时间，含
    :param end_time_str: 结束时间，含
    :return:
    """
    if re.match("^\d{4}-\d{2}-\d{2}$", start_time_str):
        st = _parse_time_str(start_time_str, FORMAT_DATE)
    else:
        st = _parse_time_str(start_time_str, FORMAT_TIME_MINUTE)

    if re.match("^\d{4}-\d{2}-\d{2}$", end_time_str):
        # 对于输入的日期类型，需要对截止日期加1天
        et = _parse_time_str(end_time_str, FORMAT_DATE) + datetime.timedelta(days=1)
    else:
        # 对于输入的时间类型，需要对截止时间加1小时
        et = _parse_time_str(end_time_str, FORMAT_TIME_MINUTE)

    start_time_minute = st.minute
    end_time_minute = et.minute
    first = st + datetime.timedelta(minutes=5 - (start_time_minute % 5))
    last = et - datetime.timedelta(minutes=(end_time_minute % 5))

    delta = last - first
    count_5min = (60 * 60 * 24 * delta.days + delta.seconds) // 300

    data = [(first + datetime.timedelta(minutes=5 * x)).strftime(FORMAT_TIME_MINUTE) for x in range(count_5min + 1)]
    return data


def now_time_str(fmt: str = FORMAT_TIME_SECOND) -> str:
    """
    获得当前时间的字符串表现形式
    :param fmt: 时间格式
    :return:
    """
    return datetime.datetime.now().strftime(fmt)


def now_iso_time(z: str = "Z") -> str:
    """
    获取iso8601格式的时间
    :param z: 时间结尾是否带'Z'
    :return: str
    """
    iso_time = datetime.datetime.utcnow().isoformat()
    return iso_time + "Z" if z == "Z" else iso_time


def now_time_value(unit) -> int:
    """
    获取当前时间的值
    :return:
    """
    assert unit in (TIME_UNIT_YEAR, TIME_UNIT_MONTH, TIME_UNIT_DAY, TIME_UNIT_HOUR, TIME_UNIT_MINUTE,
                    TIME_UNIT_SECOND), "valid time unit"
    if unit == TIME_UNIT_YEAR:
        return datetime.datetime.now().year
    if unit == TIME_UNIT_MONTH:
        return datetime.datetime.now().month
    if unit == TIME_UNIT_DAY:
        return datetime.datetime.now().day
    if unit == TIME_UNIT_HOUR:
        return datetime.datetime.now().hour
    if unit == TIME_UNIT_MINUTE:
        return datetime.datetime.now().minute
    if unit == TIME_UNIT_SECOND:
        return datetime.datetime.now().second


def now_minute() -> int:
    """
    获取当前小时
    :return:
    """
    return datetime.datetime.now().minute


def now_timestamp(unit="s", integer=True):
    """
    获取当前时间戳
    :param unit: 时间戳单位：s，秒；ms，毫秒
    :param integer:
    :return:
    """
    timestamp = time.time() if unit == "s" else time.time() * 1000
    timestamp = int(timestamp) if integer else timestamp
    return timestamp


def future_time_str(add_months: int = 0, add_days: int = 0, add_hours: int = 0, add_minutes: int = 0,
                    add_seconds: int = 0,
                    fmt: str = "%Y-%m-%d") -> str:
    """
    获得未来若干天后的日期的字符串表示
    :param add_months:
    :param add_days:
    :param add_hours:
    :param add_minutes:
    :param add_seconds:
    :param fmt:
    :return:
    """
    f = datetime.datetime.now().today() + relativedelta(months=add_months, days=add_days, hours=add_hours,
                                                        minutes=add_minutes, seconds=add_seconds)
    return f.strftime(fmt)


def gen_druid_ios_interval(start_time: str, end_time: str) -> str:
    """
    生成 druid 查询用的 iso 时间段
    :param start_time: 开始时间，含
    :param end_time: 结束时间，不含
    :return:
    """
    return "{}/{}".format(convert_time_format(start_time, FORMAT_TIME_ISO, True),
                          convert_time_format(end_time, FORMAT_TIME_ISO, True))


def get_last_month(fmt: str = FORMAT_DATE) -> tuple:
    """
    获取上一个月的起始日期
    :param fmt:输出的时间格式
    :return:
    """
    today = datetime.date.today()
    d = today - relativedelta(months=1)  # 这个1指上一个月
    start_date = datetime.date(d.year, d.month, 1).strftime(fmt)  # 这里获取上一个月的
    end_date = (datetime.date(today.year, today.month, 1) - relativedelta(days=1)).strftime(fmt)  # 这里获取上个月最后一天
    return start_date, end_date


def is_valid_time(time_str: str, fmt: str = FORMAT_DATE) -> bool:
    """
    检查是否是一个有效的时间字符串
    :param time_str:
    :param fmt:
    :return:
    """
    if not time_str:
        return False
    try:
        time.strptime(time_str, fmt)
        return True
    except:
        return False


def timespan_cross_midnight(start_time: str, end_time: str) -> bool:
    """
    检查时间段是否跨半夜 00:00:00
    :param start_time:
    :param end_time:
    :return:
    """
    start_date = convert_time_format(start_time, FORMAT_DATE)
    end_date = convert_time_format(end_time, FORMAT_DATE)
    return start_date < end_date


def time_difference(start_time: str, end_time: str = None, fmt: str = None, unit=TIME_UNIT_SECOND) -> int:
    """
    从 start_time_str 到 end_time_str 的时间差值，单位为秒
    :param start_time: 开始时间字符串
    :param end_time: 结束时间字符串，默认为当前时间字符串
    :param fmt: 指定时间字符串的时间格式
    :param unit: 返回的时间差值的单位
    :return: 时间差值，单位为秒
    """
    if fmt:
        start = _parse_time_str(start_time, fmt)
        end = _parse_time_str(end_time, fmt) or datetime.datetime.now()
    else:
        start = _parse_time_str(start_time)
        end = _parse_time_str(end_time) or datetime.datetime.now()

    difference = end - start
    if unit == TIME_UNIT_SECOND:
        result = difference.seconds
    elif unit == TIME_UNIT_MINUTE:
        result = difference.seconds / 60
    elif unit == TIME_UNIT_HOUR:
        result = difference.seconds / 60 / 60
    else:
        result = difference.days

    return result


def gen_date_couples(start_date: str, end_date: str, max_interval: int) -> list:
    """
    生成[开始，结束]日期的配对组合
    :param start_date: 开始日期，含
    :param end_date: 结束日期，含
    :param max_interval: 日期组合的最大间隔差
    :return: [(small_date,big_date)] 形式的结果
    """
    assert start_date <= end_date, "start_date 需小于 end_date"
    assert max_interval >= 0, "max_interval 不得为负数"
    dates = gen_dates_str(start_date, end_date)
    result = []
    for small_date in dates:
        for big_date in [x for x in dates if x >= small_date]:
            if time_difference(small_date, big_date, FORMAT_DATE, TIME_UNIT_DAY) <= max_interval:
                result.append((small_date, big_date))
    return result


if __name__ == '''__main__''':
    c = time_difference("2019-08-04", "2019-09-04", FORMAT_DATE, TIME_UNIT_DAY)
    print(c)
