from math import sqrt

def get_primes(numbers):
    for number in numbers:
        if is_prime(number) and number > 1:
            yield number


def is_prime(number):
    for x in range(2, int(sqrt(number)) + 1):
        if number % x == 0:
            return False
    return True


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))