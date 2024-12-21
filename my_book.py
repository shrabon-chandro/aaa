import add_my_book

laibrary = []

while True:
    print("welcome to My library management system")
    print("0. Exit")
    print("1. Add book")
    print("2. view all book")

    select= input("Enter your choice: ")

    if select=="0":
        print("Thanks you for using library management system")
        break
    elif select=="1":
        laibrary = add_my_book.add_my_book(laibrary)
    elif select=="2":
        print("select 2")
    else:
        print("Chose a valid number")
