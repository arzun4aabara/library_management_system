"""Core library management functions for the Library Management System."""

import pandas as pd


def add_book(books_df, book_data):
    """Add a new book if the book ID does not already exist."""
    existing_ids = books_df["book_id"].astype(str).str.strip().str.lower()

    if book_data["book_id"].strip().lower() in existing_ids.values:
        return books_df, False, "Book ID already exists."

    new_row = pd.DataFrame([book_data])
    books_df = pd.concat([books_df, new_row], ignore_index=True)

    return books_df, True, "Book added successfully."


def view_all_books(books_df):
    """Return all books in the inventory."""
    return books_df


def update_book(books_df, book_id, updated_data):
    """Update details of an existing book."""
    matching_rows = (
        books_df["book_id"].astype(str).str.strip().str.lower()
        == book_id.strip().lower()
    )

    if not matching_rows.any():
        return books_df, False, "Book ID not found."

    for column, value in updated_data.items():
        if value != "":
            books_df.loc[matching_rows, column] = value

    return books_df, True, "Book updated successfully."


def remove_book(books_df, book_id):
    """Remove a book from the inventory using its ID."""
    matching_rows = (
        books_df["book_id"].astype(str).str.strip().str.lower()
        == book_id.strip().lower()
    )

    if not matching_rows.any():
        return books_df, False, "Book ID not found."

    books_df = books_df[~matching_rows].reset_index(drop=True)

    return books_df, True, "Book removed successfully."


def view_available_books(books_df):
    """Return only books that are currently available."""
    return books_df[
        books_df["availability"].astype(str).str.strip().str.lower() == "available"
    ]


def search_books(books_df, column_name, keyword):
    """Search books by title, author, or genre."""
    return books_df[
        books_df[column_name].astype(str).str.contains(
            keyword,
            case=False,
            na=False
        )
    ]


def borrow_book(books_df, book_id):
    """Borrow a book if it is currently available."""
    matching_rows = (
        books_df["book_id"].astype(str).str.strip().str.lower()
        == book_id.strip().lower()
    )

    if not matching_rows.any():
        return books_df, False, "Book ID not found."

    current_status = books_df.loc[matching_rows, "availability"].iloc[0]

    if str(current_status).strip().lower() == "borrowed":
        return books_df, False, "Book is already borrowed."

    books_df.loc[matching_rows, "availability"] = "Borrowed"

    return books_df, True, "Book borrowed successfully."


def return_book(books_df, book_id):
    """Return a book if it is currently borrowed."""
    matching_rows = (
        books_df["book_id"].astype(str).str.strip().str.lower()
        == book_id.strip().lower()
    )

    if not matching_rows.any():
        return books_df, False, "Book ID not found."

    current_status = books_df.loc[matching_rows, "availability"].iloc[0]

    if str(current_status).strip().lower() == "available":
        return books_df, False, "Book is already available."

    books_df.loc[matching_rows, "availability"] = "Available"

    return books_df, True, "Book returned successfully."