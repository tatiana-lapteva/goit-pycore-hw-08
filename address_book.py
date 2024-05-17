

from collections import UserDict
from datetime import datetime, timedelta, date
import re


class Field:
    def __init__(self, value: str) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)
    

class Name(Field):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        

class Phone(Field):

    def __init__(self, phone: str) -> None:
        if len(phone) == 10:
            super().__init__(phone)
        else:
            raise ValueError("invalid phone number")
    
    def __str__(self) -> str:
        return str(self.value)


class Birthday(Field):

    def __init__(self, value: str) -> None:
        self._birthday = None
        self.birthday = value
        super().__init__(self.birthday)
        
    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, value):
        pattern = r"\d{2}.\d{2}.\d{4}"
        if not re.match(pattern, value):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        self._birthday = datetime.strptime(value, '%d.%m.%Y').date()



class Record:
    
    def __init__(self, name: str) -> None:
        self.name = Name(name)   
        self.phones: list[Phone] = []
        self.birthday = None
        
        
    def add_phone(self, phone: str) -> None:
        if phone not in self.phones:
            self.phone = Phone(phone)
            self.phones.append(self.phone)
        else:
            raise ValueError("phone {phone} already exists in contact")


    def remove_phone(self, phone: str) -> None:
        self.phones = [p for p in self.phones if p.value != phone]
        
                
    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        index = self.phones.index(old_phone)
        self.phones[index] = Phone(new_phone).value      
            

    def find_phone(self, phone: str) -> str:
        for p in self.phones:
            if p.value == phone:
                return phone
    
    def show_phones(self) -> list:
        phones = [p.value for p in self.phones]
        return phones

    def add_birthday(self, birthday: str) -> None:
        if self.birthday is None:
            self.birthday = Birthday(birthday)
        else:
            raise NameError("Birthdate already exists")
        

    def show_birthday(self) -> str:
        birthday = self.birthday
        return birthday
        
    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, \
            phones: {';'.join(p.value for p in self.phones)}, \
                birthday: {self.birthday}"
    


class AddressBook(UserDict):
        
    def add_record(self, record: Record) -> None:
        if record.name.value in self.data:
            self.data.update({record.name.value: record})
        else:
            self.data[record.name.value] = record


    def find(self, name: str) -> Record|None:
        if name in self.data:
            return self.data[name]
        else:
            return None
        
    def show_phones(self, name: str) -> list:
        return self.data[name].show_phones()


    def find_phone(self, phone: str) -> bool:
        find_phone = lambda result: True if phone in self.data.values().__iter__() else False
        return find_phone(phone)
         

    def edit_phone(self, name: str, old_phone: str, new_phone: str) -> None:
        self.data[name].edit_phone(old_phone, new_phone)


    def delete(self, name: str) -> None:
        del self.data[name]

  
    def add_birthday(self, name: str, birthday: str) -> None:
        self.data[name].add_birthday(birthday)


    def show_birthday(self, name: str) -> str:
        birthday = self.data[name].show_birthday()
        return birthday


    def get_upcoming_birthdays(self) -> list:
        today = datetime.today().date()
        upcoming_birthdays = []
                    
        for contact in self.data.items():
            birthday_this_year = date(today.year, contact[1].birthday.value.month, contact[1].birthday.value.day)
            if birthday_this_year < today:
                birthday_this_year = date(today.year+1, contact[1].birthday.value.month, contact[1].birthday.value.day)
            birthday_weekday = birthday_this_year.isoweekday()
            
            if birthday_weekday == 6:
                birthday_this_year += timedelta(days=2)                
            elif birthday_this_year == 7:
                birthday_this_year += timedelta(days=1)

            if (birthday_this_year - today).days >= 0 and (birthday_this_year - today).days <= 7:
                upcoming_birthdays.append({'name': contact[0], 
                                        'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")})
        return upcoming_birthdays

    