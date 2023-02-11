""" Write a function that determines if a number is prime. """


def isPrimeNumber(N):
    """ A prime number is a natural number greater than 1, which is only divisible by 1 and itself """

    for i in range(2,N+1//2):
        if N%i == 0:
            print(f"The {N} is not a prime number.")
            break
    else:
        print(f"The {N} is a prime number.")

def main():
    
    N = int(input("Enter the number:     "))
    if N<=1:
        print("Please enter valid input greather than 1")
        main()
    isPrimeNumber(N)

if __name__ == '__main__':
    main()