import json
class Book_Management:
    def saveBook(self, books):
        with open("BookData.json", 'w') as file:
            json.dump(books, file)
    
    def fetchBook(self):
        try:
            with open("BookData.json", 'r') as file:
                books = json.load(file)
                return books
        except FileNotFoundError:
            return []
    
    def bookID(self, books):
        books_ids = set()
        for book in books:
            books_ids.add(book['id'])
        
        if books_ids:
            book_id = max(books_ids) + 1
        else:
            book_id = 1
        
        return book_id

        
    
    def addBook(self, books):
        try:
            id = self.bookID(books)
            name = input("Enter Book Name: ")
            price = float(input("Enter Book Price: "))
            author = input("Enter Author Name: ")
            edition = input("Enter Edition Number: ")

            book = {'id': id, 'name': name, 'price': price, 'author': author, 'edition': edition}
            books.append(book)
            self.saveBook(books)

            print(f"Book details uploaded successfully with ID: {id}")
             
        except ValueError:
            print("Pls input price in float format!!!")
    
    def viewBook(self):
        books = self.fetchBook()
        if len(books) < 1:
            print("Library is Empty!!")
        
        else:
            print("Total Number Of Books Available: ", len(books))
            for book in books:
                print(book, '\n')

    def deleteBook(self, books):
        try:
            id = int(input("Enter Book ID: "))
            for book in books:
                if book['id'] == id:
                    books.remove(book)
                    self.saveBook(books)
                    print("Book Deleted Successfully with BookID: ", id)
                    return
            print(f"Book with BookID {id} not Found!!")
        except ValueError:
            print("Pls Enter Valid BookID!!")
    
    def updateBook(self, books):
        try:
            id = int(input("Enter Book ID: "))
            for book in books:
                if book['id'] == id:
                    name = input("Enter New Name: ")
                    price = int(input("Enter New Price: "))
                    author = input("Enter New Author Name: ")
                    edition = input("Enter New Edition Number: ")

                    book['name'] = name
                    book['price'] = price
                    book['author'] = author
                    book['edition'] = edition
                    self.saveBook(books)
                    print(f"Book with BookID {id} successfully updated!!")
                    return
            print(f"Book with BookID {id} did not Found!!")
        except ValueError:
            print("Invalid BookID!!")

    def searchByID(self):
        try:
            id = int(input("Enter BookID: "))
            books = self.fetchBook()
            for book in books:
                if book['id'] == id:
                    print(book)
                    return
            print(f"Book with BookID {id} Not Found!!")
        except ValueError:
            print("Invalid BookID!!")

    def searchByName(self):
        try:
            name = input("Enter Book Name: ")
            books = self.fetchBook()
            found = False
            for book in books:            
                if book['name'] == name:
                    print(book, '\n')
                    found = True
            if not found:
                print(f"Book with name {name} not Found!")
            
        except FileNotFoundError:
            return []

