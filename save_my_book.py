
def save_my_book(laibrary):
    with open("save_all_book.csv","w") as file:
        for eachitem in list:
            list= f"[{title} title], [{year}year], [{price}price], [{author} author], [{quantity} quantity]\n"
            aa = file.write(list)
            print(aa)
        else:
            print("Here something error")
