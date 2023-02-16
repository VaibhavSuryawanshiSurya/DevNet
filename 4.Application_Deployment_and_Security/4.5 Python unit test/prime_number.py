import unittest

def is_prime_number(N):
    """ A prime number is a natural number greater than 1, which is only divisible by 1 and itself """

    for i in range(2,N+1//2):
        if N%i == 0:
            return False
    else:
        return True

if __name__ == '__main__':
    print("5 is Prime number:   ", is_prime_number(5))
    print("4 is Prime number:   ", is_prime_number(4))