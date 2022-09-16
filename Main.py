from Library import Library 
from Student import Student

# Main Driver
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
                if(len(centralLibrary.availableBooks)==0):
                    print('Sorry, No book is available now. We will catch you soon :)')
                else:
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
        
