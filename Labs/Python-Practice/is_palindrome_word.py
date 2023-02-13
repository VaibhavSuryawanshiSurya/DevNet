""" Write a program that determines if a word is a palindrome. """


def palindrome(input_str):
    """ a word, phrase, or sequence that reads the same backwards as forwards. """
    
    lower_str = input_str.lower()
    if lower_str == lower_str[::-1]:
        print(f"Given string '{input_str}' is a Palindrome. ")
    else:
        print(f"Given string '{input_str}' is not a Palindrome. ")

def main():

    input_str = input("Enter the word:     ")
    palindrome(input_str)

if __name__ == "__main__":
    main()