from base import BaseCalendar


def print_all_month():
    base_calendar = BaseCalendar(year=2019)
    for month in range(1, 13):
        base_calendar.print_month(month)
        print()


if __name__ == '__main__':
    print_all_month()
