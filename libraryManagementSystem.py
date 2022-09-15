class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        self.availableBooks = listOfBooks

    def displayAllBooksPresentInLibrary(self):
        print('Books present in library are: ')
        for index,book in enumerate(self.books):
            print(f'  {index+1}){book}')
    
    def displayAvailableBooks(self):
        print('\nBooks available in library are: ')
        for index,book in enumerate(self.availableBooks):
            print(f'  {index+1}){book}')
    
    def borrowBook(self, bookName):
        if bookName not in self.books:
            print('Sorry, this book is not available in our Library.')
        
        elif bookName in self.availableBooks:
            print(f'You have been issued {bookName} Book.\nPlease keep it safe and Happy Reading :)')
            self.availableBooks.remove(bookName) 
        else:
            print('Sorry, this book has already been issued by someone else :(')
    
    def returnBook(self, bookName):
        if bookName not in self.availableBooks:
            self.availableBooks.append(bookName)
            print('Thank you for returning this book, Hope you enjoy reading :)')
        else:
            print('Sorry, wrong attempt.')

class Student:
    def requestBorrowBook(self):
        reqBook = input('Enter the name of the book you want to borrow:')
        self.book = reqBook
        return self.book

    def returnBook(self):
        returnBook = input('Enter the name of the book you want to return:')
        self.book = returnBook
        return self.book 


if __name__ == "__main__":
    listOfBooks = ["Data Structure and Algorithms","RS Aggarwal","HK Das","Let's Us C"]
    centralLibrary = Library(listOfBooks)
    student = Student()
    print("Welcome to our Library :)",end='')

    while(True):      
        optionText = '''
         ___________________________________
        |             Menu :                |
        | 1. List Of All Books              |
        | 2. List Of Available Books        |
        | 3. Request for Borrow a Book      |
        | 4. Return a Book                  |
        | 5. Exit The Library               |
        |___________________________________|
        Please choose an option:'''
        try:
            choice = int(input(optionText))

            if choice == 1:
                centralLibrary.displayAllBooksPresentInLibrary()

            elif choice == 2:
                centralLibrary.displayAvailableBooks()

            elif choice == 3:
                bookName = student.requestBorrowBook()
                centralLibrary.borrowBook(bookName)

            elif choice == 4:
                bookName = student.returnBook()
                centralLibrary.returnBook(bookName)

            elif choice == 5:
                print('Thanks for coming to our Library :)')
                exit()

            else:
                print('Please choose an appropriate option.')
        
        except:
            print('Sorry, Invalid input. Try again!')
        
