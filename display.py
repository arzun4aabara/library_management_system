"""Display functions for the Library Management System."""


def display_main_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Library Member")
    print("2. Admin")
    print("3. Exit")


def display_member_menu():
    """Display the library member menu options."""
    print("\n" + "=" * 50)
    print("         LIBRARY MEMBER MENU")
    print("=" * 50)
    print("1. View Available Books")
    print("2. Search for Books")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Back to Main Menu")


def display_admin_menu():
    """Display the admin menu options."""
    print("\n" + "=" * 50)
    print("              ADMIN MENU")
    print("=" * 50)
    print("1. Add New Book")
    print("2. Update Book Details")
    print("3. View Inventory")
    print("4. Remove a Book")
    print("5. Back to Main Menu")


def display_books(books_df):
    """Display books in a formatted table."""
    if books_df.empty:
        print("\nNo books found.")
        return

    print("\n" + "-" * 110)
    print(
        f"{'Book ID':<10}"
        f"{'Title':<35}"
        f"{'Author':<25}"
        f"{'Genre':<15}"
        f"{'Year':<8}"
        f"{'Status':<12}"
    )
    print("-" * 110)

    for _, row in books_df.iterrows():
        print(
            f"{str(row['book_id']):<10}"
            f"{str(row['title'])[:34]:<35}"
            f"{str(row['author'])[:24]:<25}"
            f"{str(row['genre'])[:14]:<15}"
            f"{str(row['year']):<8}"
            f"{str(row['availability']):<12}"
        )

    print("-" * 110)


def display_message(message):
    """Display a general message."""
    print(f"\n{message}")


def display_success(message):
    """Display a success message."""
    print(f"\nSuccess: {message}")


def display_error(message):
    """Display an error message."""
    print(f"\nError: {message}")