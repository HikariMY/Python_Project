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
    category_details = {}
    total_items = 0
    total_categories = 0

    try:
        with open("book_in_stock.txt", "r") as book_file:
            lines = book_file.readlines()

        # ตรวจสอบว่าจำนวนบรรทัดต้องเป็นกลุ่มละ 5 บรรทัด
        if len(lines) % 5 != 0:
            print("Data is not complete ")
            return

        # ดึงข้อมูลหนังสือและจัดกลุ่มตามหมวดหมู่
        for i in range(0, len(lines), 5):
            book_id = lines[i].strip()       # รหัสหนังสือ (บรรทัดที่ 1)
            book_name = lines[i+1].strip()   # ชื่อหนังสือ (บรรทัดที่ 2)
            category = lines[i+2].strip()    # หมวดหมู่หนังสือ (บรรทัดที่ 3)
            price = float(lines[i+3].strip()) # ราคา (บรรทัดที่ 4)
            book_date = lines[i+4].strip()   # วันที่เพิ่มหนังสือ (บรรทัดที่ 5)

            if category:
                category = category.lower()  # เปลี่ยนเป็นตัวพิมพ์เล็ก
                if category not in category_details:
                    category_details[category] = {
                        "books": [],
                        "total_price": 0.0
                    }
                
                # เพิ่มข้อมูลหนังสือในหมวดหมู่
                category_details[category]["books"].append({
                    "id": book_id,
                    "name": book_name,
                    "price": price,
                    "date": book_date
                })
                category_details[category]["total_price"] += price
                total_items += 1

        # แสดงผลสรุปตามหมวดหมู่
        total_categories = len(category_details)
        print("=" * 95)
        print("Summary Report:")
        print("Added Book:\n")

        for category, details in category_details.items():
            print(f"      Category : {category.capitalize()}")
            print(f"      Number of Products: {len(details['books'])}")
            for book in details["books"]:
                print(f"      {book['id']:<10}{book['name']:<20}{category:<15}{book['price']:<10}{book['date']}")
            print(f"      Total Price :{details['total_price']:.2f}")
            print("-" * 95)

        print(f"      Total Item: {total_items}")
        print(f"      Total Category: {total_categories}")
        print("=" * 95)

    except FileNotFoundError:
        print("File 'book_in_stock.txt' not fond.")
    except Exception as e:
        print(f"Error: {e}")

def add_book():
    import re
    import os

    try:
        add_book_count = int(input("How many books do you want to add: "))

        existing_ids = set()
        if os.path.exists("book_in_stock.txt"):
            with open("book_in_stock.txt", "r") as book_files:
                lines = book_files.readlines()
                existing_ids = {lines[i].strip() for i in range(0, len(lines), 5) if lines[i].strip().isdigit()}

        try:
            with open("book_in_stock.txt", "a") as book_files:
                for count in range(1, add_book_count + 1):
                    print(f'Enter data for book #{count}')
                    
                    while True:
                        try:
                            book_id = int(input("Book ID: "))
                            if str(book_id) in existing_ids:
                                print("Book ID already exists. Please enter a unique ID.")
                            else:
                                existing_ids.add(str(book_id)) 
                                break
                        except ValueError:
                            print("Please enter a valid integer for Book ID. Ex. 100.")
                    
                    book_name = input("Book Name: ")

                    while True:
                        book_category = input("Book Category (manga/novel): ").lower()
                        if book_category in ['manga', 'novel']:
                            break
                        else:
                            print("Invalid category. Please enter 'manga' or 'novel'.")
                    
                    while True:
                        try:
                            book_price = float(input("Book Price: "))
                            break
                        except ValueError:
                            print("Please enter a valid float for Book Price.")
                    
                    while True:
                        add_date = input("Add Date (DD-MM-YYYY): ")
                        date_pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
                        if re.match(date_pattern, add_date):
                            break
                        else:
                            print("Please enter Date in format DD-MM-YYYY.")

                    book_files.write(f"{book_id}\n{book_name}\n{book_category}\n{book_price:.2f}\n{add_date}\n")
                    print(f"Book #{count} Saved.")

        except Exception as e:
            print(f"An unexpected error occurred while adding books: {e}")

    except ValueError:
        print("Please enter a valid integer number for the number of books.")



def update_book():
    import re
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

                    while True:
                        book['add_date'] = input("Enter new Add Date (DD-MM-YYYY) (or press Enter to keep the current): ") or book['add_date']
                        date_pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
                        if re.match(date_pattern, book['add_date']):
                            break
                        else:
                            print("Please enter Date in formate DD-MM-YYYY")

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
    try:
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

            while True:  # Loop to keep asking for book searches
                book_name_to_search = input("Enter the Book Name or Book ID to search (or type 'exit' to back to main menu): ")
                
                if book_name_to_search.lower() == 'exit':
                    main()
                    break
                
                # Searching for the book
                book_found = False
                for book in books:
                    if book['id'] == book_name_to_search or book['name'].lower() == book_name_to_search.lower():
                        print("Book found. Details:")
                        print(f"ID: {book['id']}")
                        print(f"Name: {book['name']}")
                        print(f"Category: {book['category']}")
                        print(f"Price: {book['price']}")
                        print(f"Add Date: {book['add_date']}")
                        book_found = True
                        break

                if not book_found:
                    print("Book ID not found.")
                
        except FileNotFoundError:
            print("Error: The book_in_stock.txt file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def del_book():
    book_id_to_delete = input("Enter the Book ID of the book to Delete: ")
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
        # กรองรายการหนังสือที่ไม่ตรงกับ book_id ที่ต้องการลบ
        confirm = input(f"Are you sure you want to delete Book ID: {book_id_to_delete} ? 'Y' Yes 'N' No: ")
        if confirm == 'Y' or confirm == 'y':
            updated_books = [book for book in books if book['id'] != book_id_to_delete]
            if len(books) == len(updated_books):
                raise ValueError("No book found with the given ID.")
        else:
            updated_books = [book for book in books]
            raise ValueError("Canceled. Returning to main menu.")
        # เช็คว่า book_id ตรงที่ต้องการลบมีอยู่ในไฟล์หรือไม่
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
    try:
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

            while True :
                book_category = input("Enter the Category to search (manga or novel): ").lower()
                if book_category in ['manga','novel'] :
                    break
                else:
                    print("Please enter manga or novel")
                    # Searching for the book
            filters = [book for book in books if book['category'] == book_category]
            
            if len(filters) == 0:
                print(f"Books in the '{book_category}' category not found.")
            else:
                print("-" * 95)
                print(f"      Category : {book_category.capitalize()}")
                print(f"      Number of Products: {len(filters)}")
            for book in filters:
                print(f"      {book['id']:<10}{book['name']:<20}{book['category']:<15}{book['price']:<10}{book['add_date']}")
            print("-" * 95)              
        except FileNotFoundError:
            print("Error: The book_in_stock.txt file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def exit_program():
    choice = input("Are you sure you want to exit? 'y' , 'n'\nYour Choice: ")
    if choice.lower() == 'y':
        exit()
    elif choice.lower() == 'n':
        main()
    else:
        print("Invalid option. Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()

