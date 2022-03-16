"""Receives from user two different dates in format YYYY-MM-DD,
pick random date between the given dates and check if the weak day of
the random date is monday.
If it is, monday is the date that I don't have vinaigrette.
When the date is on monday, the program print that I don't have vinaigrette,
otherwise it print that I have vinaigrette.

"""

from datetime import datetime, timedelta
from random import randrange
import time


TIME_FORMAT = "%Y-%m-%d"


def rand_time(first_date: datetime, second_date: datetime, date_format: str) -> str:
    """Picking a randomize date in range [first date-second date].
    I got help from
    https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    :param first_date: first time type for tip of range.
    :param second_date: second time type for second tip of range.
    :param date_format: the wanted date print format.
    :return: date's string format as constant TIME_FORMAT.
    """
    if first_date.date() == second_date.date():
        return first_date.strftime(date_format)
    # picking random seconds in range [first_date.total_seconds, second_date.total_seconds]
    random_dif_sec = randrange(abs(first_date - second_date).total_seconds()+86400)
    return (min(first_date, second_date) + timedelta(seconds=random_dif_sec)).strftime(date_format)


def is_date_in_week_day(date: str, day: int) -> bool:
    """Check if the current date is on the wanted weak day.
    I got help from:
    https://www.delftstack.com/howto/python/python-datetime-day-of-week/
    :param date: string, the wanted date to check its weak day
    :param day: int (monday=0, sunday=6.), for check if the date is pointing
                on that day.
    :return: true if week day of date same to the given day
    """
    return datetime.strptime(date, TIME_FORMAT).weekday() == day


def main_i_dont_have_v():

    # Receives dates from user
    first_date_str = input("Please enter your first date in format YYYY-MM-DD: ")
    first_date = datetime.strptime(first_date_str, TIME_FORMAT)
    second_date_str = input("Please enter your second date in format YYYY-MM-DD: ")
    second_date = datetime.strptime(second_date_str, TIME_FORMAT)

    # Receives random date on given dates range
    date_picked = rand_time(first_date, second_date, TIME_FORMAT)
    print(f"At date {date_picked} ", end="")
    # Check if it is monday and print result.
    if is_date_in_week_day(date_picked, 0):
        print("I don't have vinaigrette :( ")
    else:
        print("I have vinaigrette :) !!")


if __name__ == "__main__":
    main_i_dont_have_v()
