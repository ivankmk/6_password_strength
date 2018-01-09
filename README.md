# Password Strength Calculator

Script will check your password and revert strength rank:
 0 - highly weak password (in list of 500 worst passwords);
 10 - strong password;

 # Requirements

  - Python 3.5
  - Packages: getpass

Optional, but desirable - you can check your password based on the file with worst/compromised passwords. You can use your own file or [this one](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/500-worst-passwords.txt'). Save it into the folder with the script.

Also keep in mind, without check inserted password in the list with words password list, maximum score which you can get is 8.

If your password in the worst password list - you will get 0.


# How to launch

  ```bash

  $ python lang_frequency.py <file_with_bad_passwords># possibly requires call of python3 executive instead of just python
  Please, enter your password:
  You password strength score 10.0 out of 10.0
  ```

  The same with Windows environment;


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
