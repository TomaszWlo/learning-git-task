def word_check(word):

    '''
    Funkcja sprawdza czy podany argument string jest palindromem
    czyli slowem które czyta sie tak samo od przodu i od tylu
    '''

    if word == word[::-1]:
        print('Czy argument jest palindromem : Prawda')
    else:
        print('Czy argument jest palindromem : gówno prawda')

word_check('Patka')
