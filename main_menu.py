def main():
    print('-' * 20)
    print("\t\tBook Sleepwalker")
    print("\t\tBook Management")
    print("Management Menu")
    while True:
        try:
            menu = int(input("\t1.Show Book\n\t2.Add Book\n\t3.Search Book\n\t4.View Report\n\t5.Exit\nYour Choice: "))
            if menu == 1:
                show_book()
            elif menu == 2:
                add_book()
            elif menu == 3:
                search_book()
            elif menu == 4:
                view_report()
            elif menu == 5:
                exit_program()
            else:
                print("Number you entered is not an option")
        except ValueError:
            print("Please enter only numbers 1-5")


def show_book():
    print("")

def add_book():
    
    add_book_count = int(input("How many books do you want to add: "))

    with open("book_in_stock.txt", "a") as book_files:
        for count in range(1, add_book_count + 1):
            print(f'Enter data for book #{count}')
            book_id = int(input("Book ID: "))
            book_name = input("Book Name: ")
            book_category = input("Book Category: ")
            book_price = float(input("Book Price: "))
            add_date = input("Add Date (DD-MM-YYYY): ")
            book_files.write(f"{book_id}\n")
            book_files.write(f"{book_name}\n")
            book_files.write(f"{book_category}\n")
            book_files.write(f"{book_price}\n")
            book_files.write(f"{add_date}\n")
            print()

def update_book():
    book_id = int(input("Enter the Book ID for Update: "))

    books = []
    with open("book_in_stock.txt") as book_files:
        lines = book_files.readlines()

    for element in range(0, len(lines), 5):
        book = {
            'book_id': lines[element].strip(),
            'book_name': lines[element + 1].strip(),
            'book_category': lines[element + 2].strip(),
            'book_price': lines[element + 3].strip(),
            'add_date': lines[element + 4].strip()
        }
        books.append(book)

    book_found = False
    for book in books :
        if book['book_id'] == book_id :
            print("Book found. Current details:")
            print(f"Name: {book['name']}")
            print(f"Category: {book['category']}")
            print(f"Price: {book['price']}")
            print(f"Add Date: {book['add_date']}")

            book['book_name'] = input("Enter new Book Name or Enter to keep the current name") or book['book_name']
            book['book_category'] = input("Enter new Book Category or Enter to keep the current category") or book['book_category']
            book['book_price'] = input("Enter new Book Name or Enter to keep the current price") or book['book_price']
    

def search_book():
    

    print("")

def view_report():
    print("")

def exit_program():
    choice = input("Are you sure you want to exit? 'Y' , 'N'\nYour Choice: ")
    if choice.lower() == 'y':
        exit()
    elif choice.lower() == 'n':
        main()
    else:
        print("Invalid option. Please enter 'Y' or 'N'")


if __name__ == "__main__":
    main()

