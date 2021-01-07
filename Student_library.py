class Library:
    def __init__(self, BookList):
        self.bookList = BookList

    def display_books(self):
        for index, books in enumerate(self.bookList, 1):
            print(f"{index}. {books}")

    def borrow_a_book(self, bookname):
        if bookname in self.bookList:
            print(f"You have issued a book named {bookname},Please keep it safe and return in 20 days")
            self.bookList.remove(bookname)
            return True
        else:
            print(f"The book names {bookname} is not available at this time or has been issued by someone else , "
                  f"Please try again after some time")
            return False

    def return_a_book(self, bookname):
        def return_choice_func():
            return_choice = int(input(f"This Book {bookname} not Issued to anyone , if You still Want to add/donate to "
                                      f"Library "
                                      f"Then "
                                      f"Choose From Options \n1. Yes if you want to add/Donate \n2. No if you want to cancle this \n"))
            if return_choice == 1:
                self.bookList.append(bookname)
                print(
                    f"Thanks for Returning the book named {bookname} ,Hope You enjoyed reading this ,Have A Nice Day!")
            elif return_choice == 2:
                print("The return process has been cancelled")
            else:
                print("Invalid Input , please try agian...")
                return_choice_func()

        if bookname in self.bookList:
            return_choice_func()
        else:
            self.bookList.append(bookname)
            print(f"Thanks for Returning the book named {bookname} ,Hope You enjoyed reading this ,Have A Nice Day!")


class Student():
    def request_a_book(self):
        self.bookList = input("Please Enter the book name you want to borrow or request :- \n")
        return self.bookList

    def returnbook(self):
        self.bookList = input("Please Enter a Book You want to Return or Add To Library :- \n")
        return self.bookList


central = Library(["Vedas", "Mahabharat", "Ramayan", "Bhagwat Gita"])
student = Student()
welecome = '''**************************Welcome To The Library**********************************:- 
                        1. Display All available Books
                        2. Borrow/Request a Book
                        3. Add/Return a Book 
                        4. Exit The library
                        Enter Your Choice \n'''


def welcome_func():
    while (True):
        print(welecome)
        welecome_choice = int(input())
        if welecome_choice in range(1, 5):
            if welecome_choice == 1:
                central.display_books()
            elif welecome_choice == 2:
                central.borrow_a_book(student.request_a_book())
            elif welecome_choice == 3:
                central.return_a_book(student.returnbook())
            else:
                print("Thanks for using Library ,Hope You enjoyed Our service,Have A Nice Day!")
                exit()
        else:
            print("Invalid Input,Please try again...")
            welcome_func()


welcome_func()
