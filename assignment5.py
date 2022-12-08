r = str(input("enter your file name:"))
while True :
    a = str(input("enter your option weather you want to (edit) the file or you want to (read) the file:"))
    if a == 'read':
        a = "r+"
        book = open(r,a)
        print(book.read())
    elif a == "edit":
        a ="r+"
        book = open(r,a)
        line = book.read()
        a ="w+" 
        book = open(r,a)
        lines = str(input("edit:"))
        line += "\n"
        line += lines 
        book.write(line)
        book.close()
        print("you save this file")
        a = "r+"
        book = open(r,a)
        print(book.read())
    else:
       break
