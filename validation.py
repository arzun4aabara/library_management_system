"""Validation functions for the Library Management System."""


def is_valid_book_id(book_id):
    """Check if the book ID is not empty."""
    return isinstance(book_id, str) and book_id.strip() != ""


def is_valid_text(value):
    """Check if a text field is valid (not empty)."""
    return isinstance(value, str) and value.strip() != ""


def is_valid_year(year):
    """Check if the year is a valid number."""
    if not str(year).isdigit():
        return False

    year = int(year)

    if 1000 <= year <= 9999:
        return True

    return False


def is_valid_menu_choice(choice, min_option, max_option):
    """Check if the menu choice is within the allowed range."""
    if not str(choice).isdigit():
        return False

    choice = int(choice)

    return min_option <= choice <= max_option


def is_valid_search_field(field):
    """Check if the search field is allowed."""
    allowed_fields = ["title", "author", "genre"]
    return field.lower() in allowed_fields