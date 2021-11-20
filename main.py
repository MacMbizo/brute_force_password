import itertools
import string
import time

def guess_common_passwords(password):
    with open('common_passwords.txt', 'r') as passwords:
        data = passwords.read().splitlines()

    for i, match in enumerate(data):
        if match == password:
            return f'The password is {match} (Common password #{i})'

    return 0

