#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""""Tests that login() has the correct required parameters."""

import authentication
import getpass

def login(username, maxattempts):
    """ This fnction tests: correct required parameters are passed for login.
        If user name is in user databse it executes further. Function provides
        maximum number of passwords attempts possible, and maximum attempts
        limit provide a limit for while counter loop. If user name and password
        found authentication turns to be true .

    Args:
        username(str): The name of the user to authenticate.
        maxattempts(int, optional): Max  allowed attempts before returned False

    Return:
        bool: Returns boolean if username and password found in database

    Example:
        >>> import task_02
        >>> task_02.login('mike', 2)
        Please enter your password:
        Incorrect username or password. Attempts left 1.
        Please enter your password:
        mike, You are logged in
        True

        >>> task_02.login('violet', 2)
        Please enter your password:
        Incorrect username or password. Attempts left 1.
        Please enter your password:
        Incorrect username or password. Attempts left 0.
        False

    """

    user_validates = False                       # defensive programming


    attempt = 1
    while attempt <= maxattempts:
        passwords = getpass.getpass('Please enter your password: ')

        user_validates = authentication.authenticate(username, passwords)

        # authentication for username,password = True/False

        if user_validates is False:
            print ('Incorrect username or password.\n'
                   'Attempts left {}. '.format(maxattempts-attempt))
            attempt += 1
            continue

        else:
            print '{}, You are logged in'.format(username.upper())
        break

    return user_validates


if __name__ == '__main__':
    print login('violet', 2)
