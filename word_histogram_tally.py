#Word Histogram tally
#Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.
print('Word Summary:\nGiven a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters. ')


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
    return word_dict

#takes the word_dict and lists the top three words
def histo_tally():
    word_dict = main()
    count = 1
    print('The top three words are: ')
    for key,value in sorted(word_dict.items()):
        if count <= 3:
            print(key,':',value)
            count += 1
    return 

histo_tally()