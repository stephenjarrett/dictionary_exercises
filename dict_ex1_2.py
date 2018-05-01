#Exercise 1
#Given the following dictionary, representing a mapping from names to phone numbers:
# Write code to do the following:
#1 Print Elizabeth's phone number.
#2 Add an entry to the dictionary: Kareem's number is 938-489-1234.
#3 Delete Alice's phone entry.
#4 Change Bob's phone number to '968-345-2345'.
#5 Print all the phone entries.

print('Exercise 1')

phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

#1
print('Elizabeth\'s phone number: ' + phonebook_dict['Elizabeth'])
#2
phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict)
#3
del phonebook_dict['Alice']
print(phonebook_dict)
#4
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)
#5
print(phonebook_dict.values())
print()

#Exercise 2 - Nested Dictionaries
#1 Write a python expression that gets the email address of Ramit.
#2 Write a python expression that gets the first of Ramit's interests.
#3 Write a python expression that gets the email address of Jasmine.
#4 Write a python expression that gets the second of Jan's two interests.

print('Exercise 2 - Nested Dictionaries')
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

#1
print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])