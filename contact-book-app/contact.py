class PhoneBook:
    contacts = {}
    total_contact = 0

    def menu(self):
        print("1. Create Contact: ")
        print("2. View Contact: ")
        print("3. Update Contact: ")
        print("4. Delete Contact: ")
        print("5. Search Contact: ")
        choice = int(input("Choose: "))
        return choice

    def create_contact(self):
        try:
            name = input("Enter name: ").lower()
            if name in self.contacts:
                print(f"Contact with {name} already exists")
            else:
                age = int(input("Enter age: "))
                email = input("Enter email: ")
                phone_number = input('Enter Phone Number: ')
                self.contacts[name] = {
                    'Age': age,
                    'Email': email,
                    'Phone Number': phone_number
                }
                print("Contact saved ...")
                self.total_contact += 1
        except Exception as e:
            print("Something went wrong", e)

    def view_contacts(self):
        if self.total_contact == 0:
            print("No contact exists")
        else:
            for name, information in self.contacts.items():
                print("Contact Name", name)  # Key --> Ayaz
                # Print Values
                print("Contact Age: ", information['Age'])
                print("Contact Email: ", information['Email'])
                print("Contact Phone Number: ", information['Phone Number'])
                print("------------------------------")
        print("Total Contact: ", self.total_contact)

    def update_contact(self):
        name = input("Enter name: ").lower()
        if not name in self.contacts:
            print(f"Contact with {name} not exists")
        else:
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            phone_number = input('Enter Phone Number: ')
            self.contacts[name] = {
                'Age': age,
                'Email': email,
                'Phone Number': phone_number
            }
            print("Contact Updated ...")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ").lower()

        if not name in self.contacts:
            print(f"Contact with {name} not exists")
        else:
            del self.contacts[name]
            print(f"Contact for {name} has been deleted.")
            self.total_contact -= 1

    def search_contact(self):
        name = input("Enter the name of the contact to search: ")
        if not name in self.contacts:
            print(f"Contact with {name} not exists")
        else:
            contact = self.contacts[name]
            print(f"Details for {name}:")
            print(f"Age: {contact['Age']}")
            print(f"Email: {contact['Email']}")
            print(f"Phone Number: {contact['Phone Number']}")

pp = PhoneBook()

while True:
    result = pp.menu()
    if result == 1:
        pp.create_contact()
    elif result == 2:
        pp.view_contacts()
    elif result == 3:
        pp.update_contact()
    elif result == 4:
        pp.delete_contact()
    elif result == 5:
        pp.search_contact()
    else:
        print("Invalid Input Please Try again")

print("Thank you for using our program..")

# print(random.randint(1,10))