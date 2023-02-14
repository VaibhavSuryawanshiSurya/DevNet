""" Write a function that returns the sum of the first N natural numbers. """


def sumNaturalNumber(N):
    """ This functions returns the sum of first N natural numbers, natural numbers start from 1."""
    
    Num_list = list(range(1,N+1))
    return sum(Num_list)

def main():
    
    N = int(input("Enter the count of first N natural numbers:     "))
    if N<1:
        print("Please enter valid natural numbers.")
        main()
    sum_number = sumNaturalNumber(N)
    print(f"Sum of first {N} natural numbers is", sum_number)


if __name__ == '__main__':
    main()