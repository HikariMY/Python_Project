def main():
    print('-' * 20)
    print("\t\tBook Sleepwalker")
    print("\t\tBook Mangement")
    print("Mangement Menu")
    while True:
        try:
            menu = int(input("\t1.Show Book\n\t2.Add Book\n\t3.Search Book\n\t4.View Report\n\t5.Exit\nYour Chioce: "))
            if menu == 1:
                show_book
            elif menu == 2:
                add_book
            elif menu == 3:
                search_book
            elif menu == 4:
                view_report
            elif menu == 5:
                exit_program()
            else:
                print("Number you enter is not in option")
        except ValueError:
            print("Please Enter Only numbers 1-5")


def show_book():
    print("")

def  add_book():
    print("")

def  search_book():
    print("")

def  view_report():
    print("")

def  exit_program():
    chioce = input("Are you sure to Exit\nYour Chioce: ")
    if chioce in ['y','Y'] :
        exit()
    elif chioce in ['n','N']:
        main() 
    else:
        print("Invalid option. Please enter y or n ")



if __name__ == "__main__":
    main()