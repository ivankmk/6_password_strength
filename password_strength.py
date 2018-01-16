import re
import os
import sys
import getpass


def get_default_weight():
    return 1.6


def get_blacklist_data(file_path):
    with open(file_path, 'r', encoding="utf-8") as file_reader:
        blacklist = [line.strip() for line in file_reader]
    return blacklist


def blacklist_check(password, bad_passwords):
    if password in bad_passwords:
        return 0
    else:
        return get_default_weight()


def check_password_strength(password):
    checks = ['[A-Z]', '[a-z]', '[^a-zA-Z0-9]', '[0-9]']
    min_lenght = 14
    points = 0
    for check in checks:
        if bool(re.search(check, password)):
            points += get_default_weight()
    if len(password) > min_lenght:
        points += get_default_weight()
    return points


if __name__ == '__main__':
    try:
        blacklist_passwords = get_blacklist_data(sys.argv[1])
    except IndexError:
        blacklist_passwords = []
    password = getpass.getpass('Please, enter your password: ')
    is_it_compromised = blacklist_check(password, blacklist_passwords)
    if is_it_compromised == 0:
        print('Your password strength score 0.0 out of 10.0')
    else:
        password_strength = check_password_strength(password)
        print('Your password strength score {} out of 10.0'
              .format(round(is_it_compromised+password_strength, 0)))
