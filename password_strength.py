import re
import os
import sys
import getpass


def get_blacklist_data(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file_reader:
            blacklist = file_reader.read()
        return blacklist
    except FileNotFoundError:
        return None


def blacklist_check(password, bad_passwords):
    point_weight = 1.6
    if bad_passwords is None:
        return 0
    elif password in bad_passwords:
        return None
    else:
        return point_weight


def check_password_strength(password):
    point_weight = 1.6
    checks = ['[A-Z]', '[a-z]', '[^a-zA-Z0-9]', '[0-9]']
    min_lenght = 14
    points = 0
    for check in checks:
        if bool(re.search(check, password)):
            points += point_weight
    if len(password) > min_lenght:
        points += point_weight
    return points


if __name__ == '__main__':
    blacklist_passwords = get_blacklist_data(sys.argv[1])
    password = getpass.getpass('Please, enter your password: ')
    is_it_compromised = blacklist_check(password, blacklist_passwords)
    check_result = check_password_strength(password)
    if is_it_compromised is None:
        print('Your password strength score 0.0 out of 10.0')
    else:
        print('Your password strength score {} out of 10.0'
              .format(round(is_it_compromised+check_result, 0)))
