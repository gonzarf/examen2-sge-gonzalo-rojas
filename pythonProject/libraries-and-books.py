import json
from datetime import date

import pandas as pd

usuarios = {}
file = open("secure-users.json", "r")
usuarios = json.load(file)

print(usuarios)


books = []
librarysId = []
class Book:
    bookId = ""
    bookTitle = ""
    bookEditorial = ""
    bookPublication = 0
    libraryId = ""
    userId = ""

for user in usuarios:
    book = Book()
    book.userId = user["userId"]
    for bookitem in user["books"]:
        book.bookId = bookitem["bookId"]
        book.bookTitle = bookitem["bookTitle"]
        book.bookEditorial = bookitem["bookEditorial"]
        book.bookPublication = bookitem["bookPublication"]
        book.libraryId = bookitem["libraryId"]
        # Metemos el id de la libreria solo si no se encuentra dentro ya
        if bookitem["libraryId"] not in librarysId:
            librarysId.append(bookitem["libraryId"])

        books.append(book)

print(librarysId)

file = open("libraries-and-books.json", "w")


libros_anadir = []
librosLibreria = []
for libId in librarysId:
    for libro in books:
        if libro.libraryId == libId:
            libros_anadir.append(libro)
    libreria = {
        "Libreria": libId,
        "books": json.dumps(libros_anadir, default=lambda o: o.__dict__,
            sort_keys=True)
    }
    librosLibreria.append(libreria)

json.dump(librosLibreria, file, indent= 4)

file = open("libraries-and-books.json", "r")
librerias = json.load(file)

lib_id = []
for item in librerias:
      id = item["Libreria"]
      lib_id.append(id)

df = pd.DataFrame({'ID': lib_id})
df.to_excel(f'{date.today().day}-{date.today().month}-libros-prestados.xlsx')






