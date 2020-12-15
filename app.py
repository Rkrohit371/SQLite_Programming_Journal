from database import add_entry, get_entries, create_table

menu = """
Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

You selection: """

welcome = "Welcome to the programming diary!"
print(welcome)

def promt_new_entry():
        entry_content = input("What you have learnt today? ")
        entry_date = input("Enter the date: ")

        add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
            print(f"{entry['date']}\n{entry['content']}\n\n")

create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        promt_new_entry()

    elif user_input == "2":
        view_entries(get_entries())
        
    else:
        print("Invalid option, please try again!")