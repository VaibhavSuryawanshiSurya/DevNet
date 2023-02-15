""" Write a program that receives a sentence and separates the words by spaces. 
For example, if I receive the text "I love programming in Python", it should 
return "I" "love" "programming" "in" "Python" in a list. """


def separate_words(input_str):
    """ This functions returns the list of separate words from the given sentance"""
    
    words_list = input_str.split()
    return words_list

def main():

    input_str = input("Enter the sentence:     ")
    words_list = separate_words(input_str)
    print(words_list)

if __name__ == "__main__":
    main()
