from re import A

class Book:
    ## Инициализация
    def __init__(self, books, writter, data, circulation, decript):
        self.books = books.strip()
        self.writter = writter.strip()
        self.data = data.strip()
        self.circulation = circulation.strip()
        self.decript = decript.strip()
    
    ## Вывод содержимого экземпляра (вывод книги)
    def print(self):
        
        print(f"Название книги : {self.books}\n"
              f"Автор: {self.writter}\n"
              f"Год Печати : {self.data}\n"
              f"Издатель: {self.circulation}\n"
              f"Описание: {self.decript}\n")

    ## Возвращает название книги
    def get_books(self):
        return self.books

    ## Меняет название
    def set_books(self, name):
        self.books = books

    ## Возвращает автора
    def get_writter(self):
        return self.writter

    ## Меняет автора
    def set_writter(self, writter):
        self.writter = writter

    ## Возвращает год, в котором книга была написана
    def get_data(self):
        return self.data

    ## Меняет год
    def set_data(self, data):
        self.data = data

    ## Возвращает издателя
    def get_circulation(self):
        return self.circulation

    ## Меняет издателя
    def set_circulation(self, circulation):
        self.circulation = circulation

    ## Возвращает описание
    def get_decript(self):
        return self.decript

    ## Меняет описание
    def set_decript(self, decript):
        self.decript = decript
        
def get_field(help_str, old_val):
        a = input(help_str).strip()
        if a != '':
            
            return a
        return old_val

def save(libra):
  f = open('library.txt', 'w', encoding="utf-8")
  for i in libra:
    f.write(str(i.books)+'.'+str(i.writter)+'.'+str(i.data)+'.'+str(i.circulation)+'.'+str(i.decript)+"\n")

## Создаем 1 книгу
Library = []
fLibrary = open('lib.txt', encoding="utf-8")  #library-библиотека(список книг)
for line in fLibrary:
  Library.append(Book(line.split(".")[0], line.split(".")[1], line.split(".")[2], line.split(".")[3], line.split(".")[4]))
## "Рабочий" цикл. Здесь выбираем действия, которые нужно будет произвести
while True:
    print(f"Введите числа от 1 до 6, чтобы:\n"
          f"1 - Список всех книг\n"
          f"2 - Добавить книгу\n"
          f"3-  Изменить книгу\n"
          f"4 - Поиск\n"
          f"5 - Удалить книгу\n"
          f"6 - Выход")
    n = input()
    if n == "1":
        print(f"СПИСОК КНИГ:")
        ## Вывод списка книг
        for i in range(len(Library)):
            print(f"КНИГА №{i+1}")
            Library[i].print()
    elif n == "2":
        print(f"Введите даные новой книги:")
        books = input("Название Книги: ")
        writter = input("Автор Произведения: ")
        data = input("Год издания: ")
        circulation = input("Издательство: ")
        decript = input("Описание: ")
        ## Добавление новой книги в список книг
        Library.append(Book(books, writter, data, circulation, decript))
        save(Library)
    elif n == "3":
        print(f"Введите данные измененной книги:\n")
        book_num = int(input("Изменение книги №"))
        if book_num > len(Library):
          print("Неверная цифра")
          continue
        books = get_field("Название Книги("+Library[book_num-1].books+'): ', Library[book_num-1].get_books())
        writter = get_field("Автор("+Library[book_num-1].writter+'): ', Library[book_num-1].get_writter())
        data = get_field("Год Публикации("+Library[book_num-1].data+'): ', Library[book_num-1].get_data())
        circulation = get_field("Издатель( )"+Library[book_num-1].circulation+'): ', Library[book_num-1].get_circulation())
        decript = get_field("Описание( )"+Library[book_num-1].decript+'): ', Library[book_num-1].get_decript())
        Library[book_num-1] = Book(books, writter, data, circulation, decript)
        save(Library)
    elif n == "5":
        ## Удаляем книгу
        book_num = int(input("Удаление книги №"))
        if book_num > len(Library):
          print("Неверная цифра")
          continue

        del Library[book_num-1] 
        save(Library)
    elif n == "4":
        poisk = input("Введите название книги: ")
        result = filter(lambda book: poisk.lower() in book.books.lower(),Library)
        for i, book in enumerate(result, 1):
            print(f"КНИГА №{i}")
            book.print()
    elif n == "6":
        ## Завершение работы
        break
    else:
        print("ERROR!")
print("Выход!")