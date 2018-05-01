#Letter 
#Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word.
print('Letter summary')
print('Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word.')

user_string = input('Please enter a string: ').lower()
alphabet_dict = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in user_string:
    if letter in alphabet_dict:
        alphabet_dict[letter] = alphabet_dict[letter] + 1
    elif letter in alphabet:
        alphabet_dict[letter] = 1
        
print(alphabet_dict)
