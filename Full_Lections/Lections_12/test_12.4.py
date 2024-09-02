class Name:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def full_name(self):
        return f'{self._name} {self._surname}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

user = Name('Kirill', 'Ten')
print(f'{user.name = }\n{user.surname = }\n{user.full_name = }')