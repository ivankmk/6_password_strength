import re
import os
import sys
import urllib.request


def get_password_strength(password):
    if blacklist_check(password) == 0:
        return 0
    elif blacklist_check(password) is None:
        return None
    else:
        return blacklist_check(password)+password_checker(password)


def blacklist_check(password):
    try:
        url_address = ('https://raw.githubusercontent.com'
        '/danielmiessler/SecLists/master/Passwords/500-worst-passwords.txt')
        raw_file = urllib.request.urlopen(url_address).read().decode('utf-8')
        blacklist = [line for line in raw_file.split('\n')]
        if password in blacklist:
            return 0
        else:
            return 1.6
    except urllib.error.URLError:
        return None


def password_checker(password):
        checks = ['[A-Z]', '[a-z]', '[^a-zA-Z0-9]', '[0-9]']
        points = 0
        for check in checks:
            if bool(re.search(check, password)) is True:
                points += 1.6
            else:
                continue
        if len(password) > 14:
            points += 1.6
        else:
            pass
        return points


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No password provided')
    else:
        score = get_password_strength(sys.argv[1])
        print('You password strength score {} out of 10.0'
              .format(round(score, 0)))
