

def main():

    books = {'JK Rolling': 'Harry Potter',
             'Al Sweigart': 'Automate the Boring Stuff With Python',
             'Margaret Wise Brown': 'Goodnight Moon'}

    while True:
        menu()
        selection = input('enter selection')
        if selection == 'add':
            add_book(books)
        elif selection == 'view':
            view_books(books)
        elif selecton == 'edit':
            edit_book(books)
        elif selection == 'del':
            delete_book(books)
        elif selection == 'exit':
            print('bye!')
            break
        else:
            print('Not a valid choice, try again')


def menu():
    print('add: Add new book')
    print('view: View all books')
    print('edit: edit the title for a book')
    print('del: delete a book')
    print('exit: quit program')
    print()


# TODO write the add_book function here...
