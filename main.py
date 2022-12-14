"""
Dysponujesz już całkiem rozbudowanym programem do obsługi wizytówek. Po dodaniu kilku elementów wyślij go Mentorowi.

Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna przechowywać
podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej klasy (BusinessContact)
rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram numer
+48 123456789 i dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.
Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.
Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje dwa
parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.
"""
from faker import Faker


class BaseContact:
    def __init__(self, name, surname, privatephone, email):
        self.name = name
        self.surname = surname
        self.privatephone = privatephone
        self.email = email
        # Variables
        self._label_length = len(f'{self.name} {self.surname}')

    def __str__(self):
        return f'{self.name} {self.surname} - {self.email}'

    def contact(self):
        """
        Contact function which writes cellphone number.

        :return: string
        """
        return f'Wybieram numer {self.privatephone} i dzwonię do {self.name} {self.surname}'

    @property
    def label_length(self):
        return self._label_length


class BusinessContact(BaseContact):
    def __init__(self, position, company, cellphone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.cellphone = cellphone

    def contact(self):
        return f'Wybieram numer {self.cellphone} i dzwonię do {self.name} {self.surname}.'


def create_contacts(x, y=True):
    """
    Creates contacts using BaseContact or BusinessContact class. Uses Faker library for random result.

    :param x: number of contacts to be created.
    :param y: True / False. If True then function will return BaseContact cards else it will be BusinessContact.
    :return: append the collected_cards list.
    """
    collected_cards = []
    for item in range(x):
        a = fake.first_name()
        b = fake.last_name()
        c = fake.company()
        d = fake.job()
        e = '{0}{1}@{2}'.format(a.lower(), b.lower(), fake.free_email_domain())
        i = f'{fake.country_calling_code()}'
        f = f'{i} {fake.lexify(text="(??)-??-???-???", letters="0123456789")}'
        g = f'{i} {fake.lexify(text="???-???-???", letters="0123456789")}'

        if y:
            collected_cards.append(BaseContact(a, b, f, e))
        else:
            collected_cards.append(BusinessContact(d, c, g, a, b, f, e))
    return collected_cards


def order(x):
    if x == 1:
        return lambda business_card: business_card.name
    elif x == 2:
        return lambda business_card: business_card.surname
    else:
        return lambda business_card: business_card.email


def print_by(x, to_be_sorted):
    """
    Sorts by name / surname or email.

    :param x: 1 - by name, 2 - by surname, everything else - email.
    :param to_be_sorted: list to be sorted.
    :return: strings of all cards __str__, strings of all cards contact() function, label_length
    """

    by_order = sorted(to_be_sorted, key=order(x))
    for card in by_order:
        print(card)
        print(card.contact())
        print(f'Label length = {card.label_length}')
        print('\n')


if __name__ == '__main__':
    fake = Faker()
    print_by(1, create_contacts(10, True))
