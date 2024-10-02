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
                del_books()
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
            print("ข้อมูลในไฟล์ไม่ถูกต้อง แต่ละหนังสือต้องมี 5 บรรทัด")
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
        print("=" * 60)

    except FileNotFoundError:
        print("ไม่พบไฟล์ 'book_in_stock.txt'")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
# ตัวอย่างการเรียกใช้งาน
show_book()



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
    book_id_to_update = input("Enter the Book ID of the book to update: ")

    # Reading the book data from the file
    books = []
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
        if book['id'] == book_id_to_update:
            print("Book found. Current details:")
            print(f"Name: {book['name']}")
            print(f"Category: {book['category']}")
            print(f"Price: {book['price']}")
            print(f"Add Date: {book['add_date']}")

            # Updating book details
            book['name'] = input("Enter new Book Name (or press Enter to keep the current): ") or book['name']
            book['category'] = input("Enter new Book Category (or press Enter to keep the current): ") or book['category']
            book['price'] = input("Enter new Book Price (or press Enter to keep the current): ") or book['price']
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

    
def search_book(): 
    print("")

def del_books():
    print("")

def filter_books():
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

