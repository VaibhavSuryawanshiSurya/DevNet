""" Write a function that displays all prime numbers between 1 and 1000. """


def isPrimeNumber(N):
    """ A prime number is a natural number greater than 1, which is only divisible by 1 and itself """

    for i in range(2,N+1//2):
        if N%i == 0:
            return False
    else:
        return True

def main():
    
    num = 1000

    prime_number_list = [N for N in range(2,num+1) if isPrimeNumber(N)]

    # print(len(prime_number_list), "prime numbers are available from 1 to 1000")
    print("Prime numbers are", prime_number_list)

if __name__ == '__main__':
    main()