import re
import os
import sys
import getpass


POINT_WEIGHT = 1.6


def blacklist_check(password, bad_passwords):
    try:
        with open(bad_passwords, 'r', encoding="utf-8") as file_reader:
            blacklist = file_reader.read()
        if password in blacklist:
            return None
        else:
            return POINT_WEIGHT
    except FileNotFoundError:
        return 0


def password_checker(password):
    checks = ['[A-Z]', '[a-z]', '[^a-zA-Z0-9]', '[0-9]']
    MIN_LENGHT = 14
    points = 0
    for check in checks:
        if bool(re.search(check, password)):
            points += POINT_WEIGHT
    if len(password) > MIN_LENGHT:
        points += POINT_WEIGHT
    return points


if __name__ == '__main__':
    password = getpass.getpass('Please, enter your password: ')
    try:
        bad_password = blacklist_check(password, sys.argv[1])
    except IndexError:
        bad_password = 0
    check_result = password_checker(password)
    if bad_password is None:
        print('You password strength score 0.0 out of 10.0')
    else:
        print('You password strength score {} out of 10.0'
              .format(round(bad_password+check_result, 0)))
