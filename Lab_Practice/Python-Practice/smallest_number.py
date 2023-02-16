""" Write a function that returns the smallest of three numbers. """

def smallest_number(N1,N2,N3):
    """ This functions returns the smallest numbers from given three number. """

    if N1==N2 and N2==N3:
        print("All numbers are equal.")
    elif N1>N3 and N2>N3:
        return N3
    elif N1>N2 and N3>N2:
        return N2
    elif N2>N1 and N3>N1:
        return N1
    elif N1==N2 or N1==N3:
        print("Out of three, two ",end='')
        return N1
    else:
        print("Out of three, two.",end='')
        return N2

def main():
    
    N1 = int(input("Enter the first number N1:      "))
    N2 = int(input("Enter the second number N2:     "))
    N3 = int(input("Enter the third number N3:      "))
    
    Smallest_Number = smallest_number(N1,N2,N3)
    print("Smallest number is ", Smallest_Number)

if __name__ == '__main__':
    main()