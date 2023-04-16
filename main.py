from operation import Book_Management
import sys

class Main:
    def execution(self, choice):
        if choice == 1:
            print("-----Add Book------")
            book_man_obj.addBook(fetch_det_obj)
        
        if choice == 2:
            print("-----View Book-----")
            book_man_obj.viewBook()
        
        if choice == 3:
            print("-----Delete Book-----")
            book_man_obj.deleteBook(fetch_det_obj)

        if choice == 4:
            print("-----Update Book-----")
            book_man_obj.updateBook(fetch_det_obj)
        
        if choice == 5:
            print("-----Search Book By BookID-----")
            book_man_obj.searchByID()
        
        if choice == 6:
            print("-----Search Book By Name-----")
            book_man_obj.searchByName()

        
        if choice == 0:
            print("Thank you!!")
            sys.exit()

if __name__ == "__main__":
    main_obj = Main()
    book_man_obj = Book_Management()
    fetch_det_obj = book_man_obj.fetchBook()

    while True:
        try:
            choice = int(input("Enter \n1. Add Book \n2. View Book \n3. Delete Book \n4. Update Book \n5. Search Book By ID \n6. Search Book By Name \n0. Exit \n"))
            main_obj.execution(choice)
        except ValueError:
            print("Choose valid option!!")
        