def word_check(word):
    if word == word[::-1]:
        print('Czy argument jest palindromem : Prawda')
    else:
        print('Czy argument jest palindromem : gówno prawda')

word_check('Patka')
