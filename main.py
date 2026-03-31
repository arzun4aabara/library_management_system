"""Main program for the Library Management System."""

from file_handler import load_books, save_books
from library_manager import (
    add_book,
    view_all_books,
    update_book,
    remove_book,
    view_available_books,
    search_books,
    borrow_book,
    return_book,
)
from display import (
    display_main_menu,
    display_member_menu,
    display_admin_menu,
    display_books,
    display_message,
    display_success,
    display_error,
)
from validation import (
    is_valid_book_id,
    is_valid_text,
    is_valid_year,
    is_valid_menu_choice,
    is_valid_search_field,
)


def admin_menu(books_df):
    """Handle admin operations."""
    while True:
        display_admin_menu()
        choice = input("Enter your choice: ")

        if not is_valid_menu_choice(choice, 1, 5):
            display_error("Invalid choice.")
            continue

        choice = int(choice)

        if choice == 1:
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            genre = input("Enter Genre: ")
            year = input("Enter Year: ")

            if not (
                is_valid_book_id(book_id)
                and is_valid_text(title)
                and is_valid_text(author)
                and is_valid_text(genre)
                and is_valid_year(year)
            ):
                display_error("Invalid book details.")
                continue

            book_data = {
                "book_id": book_id,
                "title": title,
                "author": author,
                "genre": genre,
                "year": int(year),
                "availability": "Available",
            }

            books_df, success, message = add_book(books_df, book_data)

            if success:
                save_books(books_df)
                display_success(message)
            else:
                display_error(message)

        elif choice == 2:
            book_id = input("Enter Book ID to update: ")

            updated_data = {
                "title": input("New Title (leave blank to skip): "),
                "author": input("New Author (leave blank to skip): "),
                "genre": input("New Genre (leave blank to skip): "),
                "year": input("New Year (leave blank to skip): "),
                "availability": input(
                    "New Status (Available/Borrowed or blank): "
                ),
            }

            books_df, success, message = update_book(
                books_df, book_id, updated_data
            )

            if success:
                save_books(books_df)
                display_success(message)
            else:
                display_error(message)

        elif choice == 3:
            display_books(view_all_books(books_df))

        elif choice == 4:
            book_id = input("Enter Book ID to remove: ")

            books_df, success, message = remove_book(books_df, book_id)

            if success:
                save_books(books_df)
                display_success(message)
            else:
                display_error(message)

        elif choice == 5:
            break

    return books_df


def member_menu(books_df):
    """Handle member operations."""
    while True:
        display_member_menu()
        choice = input("Enter your choice: ")

        if not is_valid_menu_choice(choice, 1, 5):
            display_error("Invalid choice.")
            continue

        choice = int(choice)

        if choice == 1:
            display_books(view_available_books(books_df))

        elif choice == 2:
            field = input("Search by (title/author/genre): ")

            if not is_valid_search_field(field):
                display_error("Invalid search field.")
                continue

            keyword = input("Enter search keyword: ")

            results = search_books(books_df, field, keyword)
            display_books(results)

        elif choice == 3:
            book_id = input("Enter Book ID to borrow: ")

            books_df, success, message = borrow_book(books_df, book_id)

            if success:
                save_books(books_df)
                display_success(message)
            else:
                display_error(message)

        elif choice == 4:
            book_id = input("Enter Book ID to return: ")

            books_df, success, message = return_book(books_df, book_id)

            if success:
                save_books(books_df)
                display_success(message)
            else:
                display_error(message)

        elif choice == 5:
            break

    return books_df


def main():
    """Main program loop."""
    books_df = load_books()

    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if not is_valid_menu_choice(choice, 1, 3):
            display_error("Invalid choice.")
            continue

        choice = int(choice)

        if choice == 1:
            books_df = member_menu(books_df)

        elif choice == 2:
            books_df = admin_menu(books_df)

        elif choice == 3:
            display_message("Thank you for using the Library System.")
            break


if __name__ == "__main__":
    main()