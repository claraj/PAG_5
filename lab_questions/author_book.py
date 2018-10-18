# Homework Week 5, Dictionaries


def main():

    # Don't modify the main method.
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
        elif selection == 'find':
            find_book(books)
        elif selection == 'edit':
            edit_book(books)
        elif selection == 'del':
            delete_book(books)
        elif selection == 'exit':
            print('bye!')
            break
        else:
            print('Not a valid choice, try again')


def menu():
    # Don't modify this method.
    print('add: Add new book')
    print('view: View all books')
    print('find: Find a title for an author')
    print('edit: edit the title for a book')
    print('del: delete a book')
    print('exit: quit program')
    print()


# Make sure you use the exact function names given!
# And, print the exact error messages requested.


# TODO write the add_book function here.
# This function should ask for an author and a title, and add them to the dictionary.
# If the author is already in the dictionary, print "Already in dictionary" and don't modify the dictionary.
# Your program should not crash.


# TODO write the view_books function here. This function should print all of the authors and titles.
# This function should not ask for any input.


# TODO write the find_book function here.
# This function should ask for an author.
# If the author is found in the dictionary, print the title of their book.
# If the author is not found, print 'Not Found'


# TODO write the edit_books function here.
# This function should ask for an author, and the new book title.
# If the author is found in the dictionary, Modify the dictionary so the author's title is the new value.
# If the author is not found, print the string 'Not Found' and don't modify the dictionary. Your program should not crash.


# TODO write the delete_book function here.
# This function should ask for an author. Delete the key-value pair for this author.
# If the author is found in the dictionary, delete that author's key-value pair.
# If the author is not found, print 'Not Found' and don't modify the dictionary. Your program should not crash.



# Don't modify this call to main() either.
if __name__ == '__main__':
    main()
