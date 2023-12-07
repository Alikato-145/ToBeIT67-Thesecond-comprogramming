x = int(input())
list_book = []
for i in range(x):
    book = str(input())
    if book[::-1] == book:
        list_book.append(book)
print(len(list_book))
print(list_book)