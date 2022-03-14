"""
This program receives from user two different dates in format YYYY-MM-DD,
pick random date between the given dates and check if the weak day of
the random date is monday.
If it is, monday is the date that I don't have vinaigrette.
When the date is on monday, the program print that I don't have vinaigrette,
otherwise it print that I have vinaigrette.

"""

from datetime import datetime
from random import random
import time


TIME_FORMAT = "%Y-%m-%d"
DAY_VALUE = 0


def rand_time(first_time: time, second_time: time, format=TIME_FORMAT):
    """
    This function is picking a randomize date in range first time-second time.
    I got help from
    https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    :param first_time: first time type for tip of range.
    :param second_time: second time type for second tip of range.
    :param format: the wanted date print format.
    :return: date's string format as constant TIME_FORMAT.
    """

    # check what is the minimum and maximum time for range.
    start_time = min(first_time, second_time)
    end_time = max(first_time, second_time)
    # picking new date.
    random_time = start_time + random()*(end_time-start_time)
    return time.strftime(format, time.localtime(random_time))


def is_date_in_week_day(date: str, day=DAY_VALUE):
    """
    The function check if the current date is on the wanted weak day.
    I got help from:
    https://www.delftstack.com/howto/python/python-datetime-day-of-week/
    :param date: string, the wanted date to check its weak day
    :param day: int (monday=0, sunday=6.), for check if the date is pointing
                on that day.
    :return: true if week day of date same to the given day
    """
    return datetime.strptime(date, TIME_FORMAT).weekday() == day


# Receives dates from user
first_date_str = input("Please enter your first date in format YYYY-MM-DD: ")
first_date = time.mktime(time.strptime(first_date_str, TIME_FORMAT))
second_date_str = input("Please enter your second date in format YYYY-MM-DD: ")
second_date = time.mktime(time.strptime(second_date_str, TIME_FORMAT))
# Receives random date on given dates range
date_picked = rand_time(first_date, second_date)
print(f"At date {date_picked}...")
# Check if it is monday and print result.
if is_date_in_week_day(date_picked):
    print("I don't have vinaigrette :( ")
else:
    print("I have vinaigrette :) !!")

