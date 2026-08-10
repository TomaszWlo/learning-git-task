import logging
logging.basicConfig(level=logging.INFO)

operacja = int(input('Podaj działanie, poslugujac sie odpowiednia liczba: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie : '))


if operacja == 1:
    ilosc_liczb = int(input('Ile liczb chcesz dodać ? : '))
    suma = 0

    for i in range(ilosc_liczb):
        liczba = float(input(f'Podaj liczbe nr: {i + 1}:'))
        suma += liczba

    logging.info(f'Dodaje liczby. Wynik: {suma}')
    print(f'Wynik to {suma}')

elif operacja == 2:
    nr1 = float(input('Podaj liczbe nr 1: '))
    nr2 = float(input('Podaj liczbe nr 2: '))

    logging.info(f'Odejmuje {nr1} i {nr2}')
    odejmowanie = (nr1) - (nr2)
    print(f'Wynik to {odejmowanie}')

elif operacja == 3:
    ilosc_mnoznikow = int(input('Ile liczb chcesz pomnożyć ? : '))
    iloczyn = 1
    
    for i in range(ilosc_mnoznikow):
        mnoznik = float(input(f'Podaj liczbe nr {i +1} :'))
        iloczyn *= mnoznik

    logging.info(f'Mnożę liczby. Wynik: {iloczyn}')
    print(f'Wynik to {iloczyn}')

elif operacja == 4:
    nr1 = float(input('Podaj liczbe nr 1: '))
    nr2 = float(input('Podaj liczbe nr 2: '))

    logging.info(f'Dzielę {nr1} i {nr2}')
    dzielenie = (nr1) / (nr2)
    print(f'Wynik to {dzielenie}')