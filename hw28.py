import bcrypt

class Users:
    def __init__(self, password, first_name, last_name, address, phones, *args, **kwargs):
        self._password = self.hash_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.address = self.validate_address(address)
        self.phones = self.validate_phone(phones)

    def hash_password(password):
        pwd = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), pwd)

    @property
    def get_fullname(self):
        return self.first_name.strip() + ' ' + self.last_name.strip()

    def validate_phone(phone):
        if not all(len(i) <= 15 for i in phone):
            raise LengthException('Enter valid data')
        return phone

    def validate_address(address):
        keys = ['city', 'billing_address', 'index']
        if not all(key in i.keys() for key in keys for d in address):
            raise ValueError("Invalid data")
        return address

    def information(self):
        return print(self.last_name + ',' + self.first_name + ',' + str(self.address) + ',' + str(self.phones))

    @property
    def password(self):
        raise PasswordException('Access Denied(You have no rights)')

    @password.setter
    def password(self, password):
        self._password = self.hash_password(password)

    @password.deleter
    def password(self):
        delattr(self._password)




ivan = Users(password = 'something', first_name = 'Ivan', last_name = 'Agafonov', 
                                          address = [{'city': 'Kharkiv', 'billing_address': 'Lermontova 16/26', 'index': '63460'},
                                          {'city': 'Kharkiv', 'billing_address': 'Ya ne skazhu', 'index': '63460'}],
                                          phones = ['0665634423', '7948218418248', '0957384856'])
