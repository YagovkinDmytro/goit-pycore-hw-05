def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Please enter 'Name' and 'Phone number'"
    name, phone = args
    if name in contacts:
        user_input = input("Contact already exists. Do you want to update it? (yes/no): ")
        if user_input.strip().lower() == "yes":
            return change_contact(args, contacts)
        else:
            return "Contact not added."
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Please enter 'Name' and 'Phone number'"
    name, phone = args
    if args in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Please enter 'Name'"
    if args[0] in contacts:
        return contacts[args[0]]
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts available."
    for key, value in contacts.items():
        return (f"Name: {key} || Phome#: {value}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()