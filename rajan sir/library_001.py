#write a menu driven program in that shows the working of libarary.The menu option should be
#add Book information
#Display Book of Given Author
#List all book of given author
#List the count of book in the libarary
#exit
book=[]
while True:
    print(".....option from 1 to 5.......")
    print("1. Add book information")
    print("2. Display book information")
    print("3. List book of given author")
    print("4. List the count of book in the Libarary")
    print("5. Exit")
    choice=int(input("please enter your choice"))
    if choice==1:
        book_info=[]
        book_name=input("enter the book name")
        book_info.append(book_name)
        book_author=input("enter the author name of book")
        book_info.append(book_author)
        book_price=int(input("enter the price of book"))
        book_info.append(book_price)
        book_copy=int(input("enter number of book"))
        book_info.append(book_copy)
        book.append(book_info)
    elif choice==2:
        author=input("enter the name of author to display book name")
        length=len(book)
        for i in range(length):
            if book[i][1]==author:
                print("the book name written by ",author,"is : ",book[i][0])
    elif choice==3:
        length=len(book)
        for i in range(length):
            print("book name is : ",book[1][0]," and the author of this book is : ",book[i][1])
    elif choice==4:
        book_name=input("enter the book name")
        print("the count of book available in libarary is : ",book.count(book_name))
    elif choice==5:
        break
    else:
        print("enter choice is incorrect, please enter your choice again")
        
