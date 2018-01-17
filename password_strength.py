import re
import os
import sys
import getpass


def get_blacklist_data(file_path):
    with open(file_path, 'r', encoding="utf-8") as file_reader:
        blacklist = [line.strip() for line in file_reader]
    return blacklist


def blacklist_check(password, bad_passwords):
    return password in bad_passwords


def check_password_strength(password):
    checks = ['[A-Z]', '[a-z]', '\W', '[0-9]']
    min_lenght = 14
    default_weight = 1.6
    points = 0
    for check in checks:
        if bool(re.search(check, password)):
            points += default_weight
    if len(password) > min_lenght:
        points += default_weight

    if blacklist_check(password, blacklist_passwords) is True:
        return 0
    else:
        points += default_weight
    return points


if __name__ == '__main__':
    try:
        blacklist_passwords = get_blacklist_data(sys.argv[1])
    except (IndexError, FileNotFoundError):
        blacklist_passwords = []
    password = getpass.getpass('Please, enter your password: ')
    password_strength = check_password_strength(password)
    print('Your password strength score {} out of 10.0'
          .format(round(password_strength, 0)))
