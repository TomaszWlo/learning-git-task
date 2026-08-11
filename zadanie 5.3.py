from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def contact(self):
        print(f'Wybieram nr {self.phone} i dzownię do {self.name} {self.surname}')

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)



class BusinesContact(BaseContact):
    def __init__(self, job, company_name, b_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company_name = company_name
        self.b_phone = b_phone

    def contact(self):
        print(f'Wybieram nr {self.b_phone} i dzownię do {self.name} {self.surname}')



def create_contact(card_type, number_of_cards):
    business_cards = []

    if card_type == 1:
        for i in range(number_of_cards):
            business_card = BaseContact(
            name = fake.first_name(),
            surname = fake.last_name(),
            phone = fake.phone_number(),
            email = fake.email(),
        )
            business_cards.append(business_card)

    if card_type == 2:
        for i in range(number_of_cards):
            business_card = BusinesContact(
            name = fake.first_name(),
            surname = fake.last_name(),
            phone = fake.phone_number(),
            email = fake.email(),
            job = fake.job(),
            company_name = fake.company(),
            b_phone = fake.phone_number(),
        )
            business_cards.append(business_card)
            
    for card in business_cards:
        print(card)

create_contact(2,5)



3
   
    



