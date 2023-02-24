""" Write a function that reads a text file and determines the number of each letter of 
the alphabet in that text. For example, “I love Python programming” has one “y”, two “m”, 
two “p”, etc. The function should return the count of only the letters that exist in the 
function. """


def number_of_each_letter(input_str):
    """ This functions returns the dictionary of letters with the count of that  letter 
    from the given sentance."""
    
    letter_dict = {}
    lower_input_str= input_str.lower()

    for letter in lower_input_str:
        if letter==' ':
            continue 
        elif letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    
    return letter_dict

def main():

    input_str = input("Enter the sentence:     ")
    letter_dict = number_of_each_letter(input_str)
    print(letter_dict)

if __name__ == "__main__":
    main()
