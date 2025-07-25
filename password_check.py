#Password Strength Checker
import string

#Functions to check different character types.
def check_length(pw):
    if len(pw)>= 8:
        return 1
    else:
        return 0

def check_uppercase(pw):
    for char in pw:
        if char.isupper():
            return 1
    return 0

def check_number(pw):
    for char in pw:
        if char.isdigit():
            return 1
    return 0

def check_special(pw):
    special_chars = string.punctuation
    for char in pw:
        if char in special_chars:
            return 1
    return 0


password = str(input('Enter your password: '))

#Exit is password is strong enough
while password != 'q':

    score = 0
    score += check_number(password)
    score += check_length(password)
    score += check_special(password)
    score += check_uppercase(password)


    strength = {0:'Very Weak',1:'Weak',2:'Medium',3:'Strong',4:'Very Strong'}

    suggestions = []

    if check_length(password) == 0:
        suggestions.append('Use at least 8 characters.')
    if check_number(password) == 0:
        suggestions.append('Include at least one number.')
    if check_uppercase(password) == 0:
        suggestions.append('Include at least one uppercase letter.')
    if check_special(password) == 0:
        suggestions.append('Include at least one special character.')

    print()
    if score == 0 or score == 1:
        print(f'Strength: {strength[score]} ❌')

    elif score == 2:
        print (f'Strength: {strength[score]} ⚠️')


    elif score == 3 or score == 4:
        print (f'Strength: {strength[score]} ✅')

    if suggestions:
        print()
        print('Suggestions to improve your password: ')
        for suggestion in suggestions:
            print('-', suggestion)

    print()
    password = str(input("Try again (Or type 'q' to quit): "))
