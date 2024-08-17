# ここにコードを書いてください
class Library:
    def __init__(self):
        # プライベート属性として本のリストを格納
        self._books = []

    def add_book(self, title, author):
        # 新しい本を辞書として追加
        self._books.append({"title": title, "author": author})

    def remove_book(self, title):
        # タイトルで指定した本を削除
        self._books = [book for book in self._books if book["title"] != title]

    def retrieve_books(self):
        # 現在の本のリストを返す
        return self._books

# Example usage:
if __name__ == "__main__":
    my_library = Library()
    my_library.add_book("1984", "George Orwell")
    my_library.add_book("To Kill a Mockingbird", "Harper Lee")
    
    print("Books in library:")
    for book in my_library.retrieve_books():
        print(book)
    
    my_library.remove_book("1984")

    print("\nBooks in library after removal:")
    for book in my_library.retrieve_books():
        print(book)