""" Write a function that allows you to calculate the factorial of a number. """


def factorialNumber(N):
    """ The factorial number is the product of an integer & all the integers below it till 1.
        Factorial of 0 is also 1."""
    
    if N == 0:
        return 1

    return factorialNumber(N-1)*N

def main():

    N = int(input("Enter the length of Fibonacci series:     "))
    
    if N<0:
        print("Please enter positive numbers")
        main()
    
    factorial_sum = factorialNumber(N)
    print(f"Factorial of {N}! is", factorial_sum)

if __name__ == "__main__":
    main()