from save_my_book import save_my_book

def add_my_books(laibrary):
    title= input("Enter a Book Title:")
    author= input("Enter Author Name: ")
    year= int(input("Enter pulising year: "))
    price= int(input("Enter Book price: "))
    isbn= int(input("Enter isbn number: "))
    quantity= int(input("Enter quantity number:"))

    book={
        "title": title,
        "author": author,
        "year": year,
        "price": price,
        "isbn": isbn,
        "quantity": quantity
    }

    laibrary.append(book)
    save_my_book(laibrary)
    print("Book added successfully")
    return laibrary
