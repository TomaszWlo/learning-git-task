zakupy = {
    'pieczywko' : ['chleb', 'bulki', 'paczek'],
    'warzywko': ['marchew', 'seler', 'rukola']
}


suma = len(zakupy['pieczywko']) + len(zakupy['warzywko'])

for sklep, towar in zakupy.items():
        print(f'Idę do sklepu {sklep.upper()} i kupuje tam {[t.upper() for t in towar]}')
        
print(f'W sumie kupuje {suma} produktow')

print('Skecz Hiszpańska inkwizycja to najlepszy skecz Monty Pythona')

