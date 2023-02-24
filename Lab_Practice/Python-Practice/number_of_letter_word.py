""" Write a function that indicates the number of one-letter words, two-letter words, 
three-letter words, etc. For example, “I love Python programming” has zero one-letter 
words, two two-letter words, one three-letter word, zero four- and five-letter words, 
one six-letter word, and one word with more than six letters. """

from num2words import num2words

def number_of_letter_word(input_str):
    """ This functions returns the dictionary of word length with the count of that 
    word of same length from the given sentance. """

    word_count_dict = {}
    words_list = input_str.split()

    for word in words_list:
        length_word = len(word)
    
        if length_word not in word_count_dict:
            word_count_dict[length_word] = 1
        else:
            word_count_dict[length_word] += 1
    
    return word_count_dict

def main():

    input_str = input("Enter the sentence:     ")
    word_count_dict = number_of_letter_word(input_str)

    for i in word_count_dict:
        print(f"{num2words(word_count_dict[i])} {num2words(i)}-letter word",end=',')

if __name__ == "__main__":
    main()
