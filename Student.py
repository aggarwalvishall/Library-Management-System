
class Student:
    def requestBorrowBook(self):
        reqBook = input('Enter the name of the book you want to borrow:')
        self.book = reqBook
        return self.book

    def returnBook(self):
        returnBook = input('Enter the name of the book you want to return:')
        self.book = returnBook
        return self.book 