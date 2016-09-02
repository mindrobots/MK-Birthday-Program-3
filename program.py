# Birthday calculator from Michael Kennedy's Python Jumpstart
import datetime


def print_headers():
    print('-------------------------------------')
    print('         BIRTHDAY CALCULATOR')
    print('-------------------------------------')
    print()


def get_birthday():
    print('What is your birthdate? ')
    year = int(input('Enter year (yyyyy): '))
    month = int(input('Enter month (mm): '))
    day = int(input('Enter day (dd): '))
    return datetime.datetime(year, month, day)


def compare_dates(birthday, now):
    current_birthday = datetime.datetime(now.year, birthday.month, birthday.day)
    midnight_today = datetime.datetime(now.year, now.month, now.day)
    return int((current_birthday - midnight_today).total_seconds() / 60 / 60 / 24)


def print_results(dt):

    if abs(dt) > 1:
        day_days = 'days'
    else:
        day_days = 'day'

    if dt < 0:
        print('Your last birthday was {} {} ago.'.format(-dt, day_days))
    elif dt > 0:
        print('Your next birthday is in {} {}.'.format(dt, day_days))
    else:
        print("It's you birthday!!!!")


def main():
    print_headers()
    birthday = get_birthday()
    now = datetime.datetime.now()
    diff = compare_dates(birthday, now)
    print_results(diff)


if __name__ == '__main__':
    main()
