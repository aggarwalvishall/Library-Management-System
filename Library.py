class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        self.availableBooks = listOfBooks

    def displayAllBooksPresentInLibrary(self):
        print('Books present in library are: ')
        for index,book in enumerate(self.books):
            print(f'  {index+1}){book}')
    
    def displayAvailableBooks(self):
        if(len(self.availableBooks)==0):
                    print('Sorry, No book is available now. We will catch you soon :)')
        else:
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