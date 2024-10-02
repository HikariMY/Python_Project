def main():
    print('-' * 30)
    print("\tBook Sleepwalker")
    print("\tBook Management")
    print('=' * 30)
    print("Management Menu")
    print('-' * 30)
    while True:
        try:
            menu = int(input("\t1.Show Book\n\t2.Add Book\n\t3.Update Book\n\t4.Search Book\n\t5.Delete Book\n\t6.Filter Book\n\t7.Exit\nYour Choice: "))
            if menu == 1:
                show_book()
            elif menu == 2:
                add_book()
            elif menu == 3:
                update_book()
            elif menu == 4:
                search_book()
            elif menu == 5:
                del_book()
            elif menu == 6:
                filter_books()
            elif menu == 7:
               exit_program()
            else:
                print("Number you entered is not an option")
        except ValueError:
            print("Please enter only numbers 1-7")
    


def show_book():
    print("")

def add_book():
    try:
        add_book_count = int(input("How many books do you want to add: "))

        try:
            with open("book_in_stock.txt", "a") as book_files:
                for count in range(1, add_book_count + 1):
                    print(f'Enter data for book #{count}')
                    try:
                        book_id = int(input("Book ID: "))
                    except ValueError:
                        print("Please enter a valid integer for Book ID Ex.100?.")

                    book_name = input("Book Name: ")

                    while True:
                        book_category = input("Book Category (manga/novel): ").lower()
                        if book_category in ['manga','novel']:
                            break
                        else:
                            print("Invalid category. Please enter 'manga' or 'novel'.")
                    while True:
                        try:
                            book_price = float(input("Book Price: "))
                            break
                        except ValueError :
                            print("Please enter a valid float ")

                add_date = input("Add Date (DD-MM-YYYY): ")

                book_files.write(f"{book_id}\n")
                book_files.write(f"{book_name}\n")
                book_files.write(f"{book_category}\n")
                book_files.write(f"{book_price:.2f}\n")
                book_files.write(f"{add_date}\n")
                print()

        except Exception as e :
            print(f"An unexpected error occurred: {e}")
    except ValueError :
        print("Plaese Enter a Inter numbers")

def update_book():
    try:
        book_id_to_update = input("Enter the Book ID of the book to update: ")

        # Reading the book data from the file
        books = []
        try:
            with open("book_in_stock.txt", "r") as book_file:
                lines = book_file.readlines()

            # Grouping lines into book entries
            for i in range(0, len(lines), 5):
                book = {
                    "id": lines[i].strip(),
                    "name": lines[i+1].strip(),
                    "category": lines[i+2].strip(),
                    "price": lines[i+3].strip(),
                    "add_date": lines[i+4].strip()
                }
                books.append(book)

            # Searching for the book to update
            book_found = False
            for book in books:
                if book['id'].lower() == book_id_to_update.lower():
                    print("Book found. Current details:")
                    print(f"Name: {book['name']}")
                    print(f"Category: {book['category']}")
                    print(f"Price: {book['price']}")
                    print(f"Add Date: {book['add_date']}")

                    # Updating book details
                    book['name'] = input("Enter new Book Name (or press Enter to keep the current): ") or book['name']

                    while True:
                        book['category'] = input("Enter new Book Category (or press Enter to keep the current): ") or book['category']
                        if book['category'] in ['manga','novel']:
                            break
                        else:
                            print("Invalid category. Please enter 'manga' or 'novel'.")
                    # Validate price input
                    new_price = input("Enter new Book Price (or press Enter to keep the current): ")
                    if new_price:
                        while not new_price.replace('.', '', 1).isdigit():
                            print("Invalid price. Please enter a valid number.")
                            new_price = input("Enter new Book Price (or press Enter to keep the current): ")
                        book['price'] = format(float(new_price), '.2f') or format(float(book['price']), '.2f')
                    
                    book['add_date'] = input("Enter new Add Date (or press Enter to keep the current): ") or book['add_date']

                    book_found = True
                    break

            if not book_found:
                print("Book ID not found.")

            # Writing the updated data back to the file
            with open("book_in_stock.txt", "w") as book_file:
                for book in books:
                    book_file.write(f"{book['id']}\n")
                    book_file.write(f"{book['name']}\n")
                    book_file.write(f"{book['category']}\n")
                    book_file.write(f"{book['price']}\n")
                    book_file.write(f"{book['add_date']}\n")

            if book_found:
                print("Book details updated successfully.")

        except FileNotFoundError:
            print("Error: The book_in_stock.txt file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


    
def search_book(): 
    print("")

def del_book():
    book_id_to_delete = input("Enter the Book ID of the book to update: ")
    # อ่านข้อมูลจากไฟล์
    books = []
    try:
        with open("book_in_stock.txt", "r") as book_file:
            lines = book_file.readlines()
            # จัดกลุ่มข้อมูลเป็นรายการหนังสือ
            
            for i in range(0, len(lines), 5):
                book = {
                    "id": lines[i].strip(),
                    "name": lines[i+1].strip(),
                    "category": lines[i+2].strip(),
                    "price": lines[i+3].strip(),
                    "add_date": lines[i+4].strip()
                }
                books.append(book)
            print(books)

        # กรองรายการหนังสือที่ไม่ตรงกับ book_id ที่ต้องการลบ
        updated_books = [book for book in books if book['id'] != book_id_to_delete]
        print(updated_books)

        # เช็คว่า book_id ตรงที่ต้องการลบมีอยู่ในไฟล์หรือไม่
        if len(books) == len(updated_books):
            raise ValueError("No book found with the given ID.")

        # เขียนข้อมูลที่เหลือกลับไปยังไฟล์
        with open("book_in_stock.txt", "w") as book_file:
            for book in updated_books:
                book_file.write(f"{book['id']}\n")
                book_file.write(f"{book['name']}\n")
                book_file.write(f"{book['category']}\n")
                book_file.write(f"{book['price']}\n")
                book_file.write(f"{book['add_date']}\n")


        print("Book deleted successfully.")

    except FileNotFoundError:
        print("Error: The book_in_stock.txt file was not found.")
    except ValueError as ve:
        print(ve)  # แสดงข้อความเมื่อไม่พบ book_id ที่ต้องการลบ

def filter_books():
    print("")

def exit_program():
    choice = input("Are you sure you want to exit? 'Y' , 'N'\nYour Choice: ")
    if choice.lower() == 'y':
        exit()
    elif choice.lower() == 'n':
        main()
    else:
        print("Invalid option. Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()

