import pandas as pd

class GoodreadsUtils:
    def __init__(self, csv_file):
        self.book_csv = pd.read_csv(csv_file)


    def count_books_in_shelves(self, csv_file: str = None, target_shelf: str = "nyc-collection", check_shelf: str = "read"):
        df = pd.read_csv(csv_file) if csv_file else self.book_csv
        
        if "Bookshelves" not in df.columns:
            raise ValueError("CSV must contain the 'Bookshelves' column")
        
        target_books = df[df["Bookshelves"].str.contains(target_shelf, na=False, case=False)]
        total_books = len(target_books)
        
        read_books = target_books[target_books["Bookshelves"].str.contains(check_shelf, na=False, case=False)].shape[0]
        read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
        
        return total_books, read_books, read_percentage

if __name__ == "__main__":
    GR = GoodreadsUtils("griffin_goodreads.csv")
    total_books, read_books, read_percentage = GR.count_books_in_shelves(target_shelf="top-100-book-poster")
    print(f"Of {total_books} books on shelf 'top-100-book-poster', {read_percentage:.2f}% have been read.")