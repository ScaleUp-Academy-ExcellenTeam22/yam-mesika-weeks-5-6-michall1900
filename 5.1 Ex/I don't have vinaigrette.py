from datetime import datetime, timedelta
from random import randrange


DATE_FORMAT = "%Y-%m-%d"


def random_date(starting_date: datetime, ending_date: datetime) -> datetime:
    """
    Picking a randomize date in range [starting date, ending date].
    I got help from
    https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    :param starting_date: Starting datetime to peek random date between it to ending date.
    :param ending_date: Ending datetime to peek random date between it to starting date (needs to be after
                        starting date).
    :return: datetime .
    """
    # picking random seconds in range [first_date.total_seconds, second_date.total_seconds]
    random_sec = randrange(abs(ending_date - starting_date).total_seconds()+86400)
    return starting_date + timedelta(seconds=random_sec)


def is_date_in_week_day(date: datetime, day: int) -> bool:
    """
    Check if the current date is on the wanted weak day.
    I got help from:
    https://www.delftstack.com/howto/python/python-datetime-day-of-week/
    :param date: The wanted date to check its weak day
    :param day: int (monday=0, sunday=6.). For check if the date is pointing on that day.
    :return: true if week day of date same to the given day
    """
    return date.weekday() == day


def receive_dates_return_random_date_between() -> datetime:
    """
    Receive from user two dates in format -YYYY-MM-DD and return date between them.
    :return: datetime - Between two dates.
    """
    starting_date = datetime.strptime(input("Please enter your starting date in format YYYY-MM-DD: "), DATE_FORMAT)
    ending_date = datetime.strptime(input("Please enter your ending date in format YYYY-MM-DD: "), DATE_FORMAT)
    return random_date(starting_date, ending_date)


def main_i_dont_have_vinaigrette() -> None:
    """
    Receive from user two dates and, pick randomize date between them and chek if the date is monday.
    If it is, it print "I don't have vinaigrette :(", else it print "I have vinaigrette :)".
    :return: None.
    """
    # Receives random date on given dates range
    date_picked = receive_dates_return_random_date_between()
    print(f"At date {date_picked.strftime(DATE_FORMAT)} ", end="")
    print("I don't have vinaigrette :( ") if is_date_in_week_day(date_picked, 0) else print("I have vinaigrette :) !!")


if __name__ == "__main__":
    main_i_dont_have_vinaigrette()
