"""
Bot-helper, works with user contacts
"""

from parse import parse_input
from handler import add_contact, change_contact, show_phone, show_birthday, add_birthday, birthdays
from serialization import save_data, load_data


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    try:
        while True:
            user_input = input("Enter a command:").strip().lower()
            command, *args = parse_input(user_input)        
            
            if command in ["close", "exit"]:
                print("Good Bye!")
                save_data(book)
                yield None

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":                 # add name phone
                print(add_contact(args, book))
                
            elif command == "change":              # change name old_phone new_phone
                print(change_contact(args, book))

        
            elif command == "phone":               # phone name
                print(show_phone(args, book))
           
            elif command == "all":                 # all
                for record in book.values():
                    print(record)

            elif command == "add-birthday":        # add-birthday name birth_date
                print(add_birthday(args, book))
        
            elif command == "show-birthday":       # show-birthday name
                print(show_birthday(args, book))

            elif command == "birthdays":           # birthdays
                print(birthdays(book))
        
            else:
                print("Invalid command.")
    
    except GeneratorExit:
        pass
    


if __name__ == "__main__":
    gen = main()
    next(gen)
    gen.close()
