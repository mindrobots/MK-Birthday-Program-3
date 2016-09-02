# Birthday calculator from Michael Kennedy's Python Jumpstart
import datetime


def pluralize(word, value):
    """ Return either singular or plural form of word based on value being one or more.
        pass tuple of word choices and value
        pluralize(('day', 'days'), number) """

    if value > 1:
        return word[1]
    else:
        return word[0]


def print_headers():
    print('-------------------------------------')
    print('         BIRTHDAY CALCULATOR')
    print('-------------------------------------')
    print()


def get_birthday():
    print('What is your birth date? ')
    year = int(input('Enter year (yyyyy): '))
    month = int(input('Enter month (mm): '))
    day = int(input('Enter day (dd): '))
    return datetime.datetime(year, month, day)


def days_this_year_birthday(birthday, now):
    current_birthday = datetime.datetime(now.year, birthday.month, birthday.day)
    midnight_today = datetime.datetime(now.year, now.month, now.day)
    return int((current_birthday - midnight_today).total_seconds() / 60 / 60 / 24)


def days_next_birthday(birthday, now):
    current_birthday = datetime.datetime(now.year+1, birthday.month, birthday.day)
    midnight_today = datetime.datetime(now.year, now.month, now.day)
    return int((current_birthday - midnight_today).total_seconds() / 60 / 60 / 24)


def print_results(this_bday, next_bday):

    if this_bday < 0:
        print('Your last birthday was {} {} ago.'.format(-this_bday, pluralize(('day', 'days'), abs(this_bday))))
        print('Cheer up, your next birthday is in {} {}.'.format(next_bday, pluralize(('day', 'days'), abs(next_bday))))
    elif this_bday > 0:
        print('Your next birthday is in {} {}.'.format(next_bday, pluralize(('day', 'days'), abs(next_bday))))
    else:
        print("It's you birthday!!!!")


def main():
    print_headers()
    birthday = get_birthday()
    now = datetime.datetime.now()
    diff_this_bday = days_this_year_birthday(birthday, now)
    days_next_bday = days_next_birthday(birthday, now)
    print_results(diff_this_bday, days_next_bday)


if __name__ == '__main__':
    main()
