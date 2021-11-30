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

def brute_force(password, min_length=4, max_length=9):
    chars = string.ascii_lowercase + string.digits 
    attempts = 0
    for password_length in range(min_length, max_length):
        for guess in itertools.product(chars, repeat = password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return f'The password is {guess} (Attempt #{attempts})'
            print(guess, attempts)

def get_password(password):
    common = guess_common_passwords(password)
    return brute_force(password) if common == 0 else common

start_time = time.time()

print(get_password('a123')) #testing using an easy password.
print(round(time.time() - start_time, 2), 's')
