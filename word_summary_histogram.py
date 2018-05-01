#Word Summary
#Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text.
print('Word Summary:\nWrite a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text. ')


#remove all any punctuation or false characters from the user input
def clean_string(user_string):
    cleaned_string = ''
    for char in user_string:
        if char not in ',.?!@#$^&*()':
            cleaned_string += char
    cleaned_string = cleaned_string.split()
    return cleaned_string

#build out the dictionary after cleaning the string
def build_dict(user_string):
    word_dict = {}
    for word in user_string:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

#main fn asking for user input then running it through the 2 sub functions above and printing output
def main():
    user_string = input('Please enter a sentence: ').lower()
    cleaned_string = clean_string(user_string)
    word_dict = build_dict(cleaned_string)
    print(word_dict)
    return word_dict

main()