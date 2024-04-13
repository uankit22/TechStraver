#Ankit Upadhyay,, uankit281@gmail.com

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {'phone_number': phone_number, 'email': email}
        print(f'Contact {name} added successfully.')

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} removed successfully.')
        else:
            print(f'Contact {name} not found.')

    def search_contact(self, name):
        found = False
        name = name.lower()
        for contact_name, details in self.contacts.items():
            if name in contact_name.lower():
                found = True
                print(f'Name: {contact_name}')
                print(f'Phone Number: {details["phone_number"]}')
                print(f'Email: {details["email"]}')
        if not found:
            print(f'No contacts found with name containing "{name}".')

    def display_all_contacts(self):
        if self.contacts:
            print("All Contacts:")
            for name, details in self.contacts.items():
                print(f'Name: {name}, Phone Number: {details["phone_number"]}, Email: {details["email"]}')
        else:
            print("No contacts found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n------ Contact Book Menu ------")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            while len(phone_number) < 10:
                print("Phone number should be at least 10 digits long. Please enter a valid phone number.")
                phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            while "@gmail.com" not in email:
                print("Only @gmail.com email addresses are supported.")
                email = input("Enter email address: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == '2':
            contact_book.display_all_contacts()
            name = input("Enter contact name to remove: ")
            contact_book.remove_contact(name)
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            contact_book.display_all_contacts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
