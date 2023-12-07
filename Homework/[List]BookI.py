x = int(input())
books = []
y =0
for i in range(x):
    name = str(input())
    if len(books) <2:
      books.append(name)
    else:
      count = books.count(name)
      if(count ==2):
        pass
      else:
        for i in range (len(books)):
          if(books[i] == name):
            books.insert(i,name)
            y = 1
            break
        if y == 0 :
          books.append(name)
        else:
          y = 0

print("ชั้นวางหนังสือ", books)
