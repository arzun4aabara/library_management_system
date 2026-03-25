# File handling functions using pandas
import pandas as pd

CSV_FILE = "books.csv"

COLUMNS = [
    "book_id",
    "title",
    "author",
    "genre",
    "year",
    "availability"
]

def load_books():
# Load book records from the CSV file

    try:
        books_df = pd.read_csv(CSV_FILE)

    except FileNotFoundError:
        books_df = pd.DataFrame(columns=COLUMNS)
        books_df.to_csv(CSV_FILE, index=False)

    return books_df


def save_books(books_df):
# Save the DataFrame back to the CSV file

    books_df.to_csv(CSV_FILE, index=False)