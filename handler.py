
from address_book import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TypeError, ValueError):
            print("Enter the argument for the command")
        except (IndexError, KeyError):
            print("The contact not found.")
        except Exception as e:
            print(e)
                
    return inner


@input_error
def add_contact(args: str, book: AddressBook) -> str:
    """
    add new contact to contacts
    """

    if len(args) == 1:
        name = args[0]
        phone = None
    else: 
        name, phone, *_ = args
        
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)

    return message
    

@input_error
def change_contact(args: str, book: AddressBook) -> str:   
    """
    change phone number for existing contact in contacts
    """
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError
    else:
        if book.find_phone(old_phone):
            book.edit_phone(name, old_phone, new_phone)
        return "Contact updated."
 

@input_error
def show_phone(args: str, book: AddressBook) -> list:              
    """
    show phone numbers for existing contact in contacts
    """
    name, *_ = args
    phones = book.show_phones(name)
    return phones


@input_error
def add_birthday(args: str, book: AddressBook) -> str:
    """ add birthday for requested name in contacts"""
    name, birthday, *_ = args
    book.add_birthday(name, birthday)
    return "Birhday added"


@input_error
def show_birthday(args: str, book: AddressBook) -> str:
    """ return birthday for requested name in contacts """
    name, *_ = args
    birthday = book.show_birthday(name)
    return birthday


@input_error
def birthdays(book: AddressBook) -> list:
    """ return the list of contacts with upcoming birthdays (in 7 days) """
    birthdays = book.get_upcoming_birthdays()
    return birthdays


        


