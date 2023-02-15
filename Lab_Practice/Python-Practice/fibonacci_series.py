""" Write a function that returns N numbers from the Fibonacci series. 
The number N is an input determined by the user using the script. """


def fibonacciSeries(N):
    """ A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. """
    
    fibonacci_series = [0,1]
    for i in range(2,N):
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series

def main():
    
    N = int(input("Enter the length of Fibonacci series:     "))
    if N<=1:
        print("Please enter valid input greather than 1")
        main()
    fibonacci_series = fibonacciSeries(N)
    print(f"Fibonacci series of length {N} is", fibonacci_series)

if __name__ == '__main__':
    main()