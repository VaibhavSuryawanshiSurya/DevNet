""" Write a function that returns N numbers from the Fibonacci series. 
The number N is an input determined by the user using the script. """


def fibonacci_series(N):
    """ A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. """
    
    fs = [0,1]
    for i in range(2,N):
        fs.append(fs[-1] + fs[-2])
    return fs

def main():
    
    N = int(input("Enter the length of Fibonacci series:     "))
    if N<=1:
        print("Please enter valid input greather than 1")
        main()
    fs = fibonacci_series(N)
    print(f"Fibonacci series of length {N} is", fs)

if __name__ == '__main__':
    main()