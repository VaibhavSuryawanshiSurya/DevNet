""" Write a function that takes an integer value and returns the number with its digits reversed. 
For example, given the number 7631, the function should return 1367. """


def reversed_integer(N):
    """ This functions returns the reverse integer of given number."""

    N_str = str(N)
    reverse_N_str = N_str[::-1]
    return int(reverse_N_str)

def main():
    
    N = int(input("Enter the number:     "))
    if N<0:
        print("Please enter positive intiger.")
        main()
    else:
        Rev_integer =  reversed_integer(N)
        print(f"The reverse of given integer {N} is ", Rev_integer)

if __name__ == '__main__':
    main()