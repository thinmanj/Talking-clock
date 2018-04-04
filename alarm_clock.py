#!/usr/bin/env python2.7

"""
It convert a the time argument to numerals and pass it to pyttsx
speach engine

it has the following arguments:

usage: alarm_clock.py [-h] [-t] [-v] [time]

Irish clock speaker.

positional arguments:
  time           Time to say - format HH:MM

optional arguments:
  -h, --help     show this help message and exit
  -t, --test     test implememntation
  -v, --verbose  test verbosity
"""

import time
import argparse

from num2words import num2words
import pyttsx


def valid_time(s):
    """
    Returns a time structure if possible, else rise a parsing exception

    to be use as part of argparse

    Keywords:
    s: a string with the format HH:MM

    Returns:
    a time.time_structure


    >>> for x in range(0,24,6):
    ...   for y in range(0,60,15):
    ...       valid_time("{0:02d}:{1:02d}".format(x, y))
    ...
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=15, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=30, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=45, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=6, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=6, tm_min=15, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=6, tm_min=30, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=6, tm_min=45, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=12, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=12, tm_min=15, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=12, tm_min=30, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=12, tm_min=45, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=18, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=18, tm_min=15, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=18, tm_min=30, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=18, tm_min=45, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    >>> valid_time("24:00")
    Traceback (most recent call last):
      File "/usr/local/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.valid_time[1]>", line 1, in <module>
        valid_time("24:00")
      File "./alarm_clock.py", line 65, in valid_time
        raise argparse.ArgumentTypeError(msg)
    ArgumentTypeError: Not a valid time: '24:00'.
    >>> valid_time("10:60")
    Traceback (most recent call last):
      File "/usr/local/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.valid_time[1]>", line 1, in <module>
        valid_time("24:00")
      File "./alarm_clock.py", line 65, in valid_time
        raise argparse.ArgumentTypeError(msg)
    ArgumentTypeError: Not a valid time: '10:60'.

    """

    try:
        return time.strptime(s, '%H:%M')
    except ValueError:
        msg = "Not a valid time: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def get_meridiem(hour):
    """
    Returns if the hour corresponds to a.m. or p.m.

    it's incomplete as it don't check the range of the value

    Keywords:

    Hour: integer,

    Returns:
    a string : "a.m."/"p.m."


    >>> for x in range(24):
    ...   get_meridiem(x)
    ...
    'a.m.'
    'a.m.'
    'a.m.'
    'a.m.'
    'a.m.'
    'a.m.'
    'a.m.'
    'a.m.'
    'a.m.'
    'a.m.'
    'a.m.'
    'a.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    'p.m.'
    """

    if hour < 12:
        return "a.m."
    return "p.m."


def say_time(time):
    """
    retuns a list of string to feed to the speach engine

    first string is constant

    lenght of list is variable

    Keywords:
    time: a time.time_structure with time information

    Returns:

    a list of strings

    >>> from collections import namedtuple
    >>> Time = namedtuple('Time', ['tm_hour', 'tm_min'])
    >>> for x in range(0,24,6):
    ...   for y in range(0,60,15):
    ...     time = Time(x, y)
    ...     say_time(time)
    ...
    ['The time is', 'twelve', 'a.m.']
    ['The time is', 'twelve', u'fifteen', 'a.m.']
    ['The time is', 'twelve', u'thirty', 'a.m.']
    ['The time is', 'twelve', u'forty-five', 'a.m.']
    ['The time is', u'six', 'a.m.']
    ['The time is', u'six', u'fifteen', 'a.m.']
    ['The time is', u'six', u'thirty', 'a.m.']
    ['The time is', u'six', u'forty-five', 'a.m.']
    ['The time is', u'twelve', 'p.m.']
    ['The time is', u'twelve', u'fifteen', 'p.m.']
    ['The time is', u'twelve', u'thirty', 'p.m.']
    ['The time is', u'twelve', u'forty-five', 'p.m.']
    ['The time is', u'eighteen', 'p.m.']
    ['The time is', u'eighteen', u'fifteen', 'p.m.']
    ['The time is', u'eighteen', u'thirty', 'p.m.']
    ['The time is', u'eighteen', u'forty-five', 'p.m.']

    """

    time_list = ['The time is']
    if not time.tm_hour:
        time_list.append('twelve')
    else:
        time_list.append(num2words(time.tm_hour))
    if time.tm_min:
        time_list.append(num2words(time.tm_min))
    time_list.append(get_meridiem(time.tm_hour))
    return time_list


def main():
    """ Main function that calls argpars, and depending on arguments do
    testing or tries to speak the argument that's expected a time"""

    parser = argparse.ArgumentParser(description='Irish clock speaker.')
    parser.add_argument('time', type=valid_time,
                        help='Time to say - format HH:MM', nargs='?')
    parser.add_argument("-t", "--test", help="test implememntation",
                        action="store_true")
    parser.add_argument("-v", "--verbose", help="test verbosity",
                        action="store_true")

    args = parser.parse_args()

    if not (args.test or args.time):
        parser.error('No action requested, add a time or -t/--test')

    if args.test:
        import doctest
        doctest.testmod()
        return 0

    engine = pyttsx.init()
    map(lambda x: engine.say(x), say_time(args.time))
    engine.runAndWait()


if __name__ == "__main__":
    main()
