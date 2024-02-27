class Book:
    def __init__(self,bookid,bookname,price,authorname):
        self.bookid=bookid
        self.bookname=bookname
        self.price=price
        self.authorname=authorname
    def CalDiscount(self):
        if self.pages<=400:
            self.price=self.price-0.05*self.price
        elif self.pages>400 and self.pages<1000:
            self.price=self.price-0.1*self.price
        else:
            self.price=self.price-0.15*self.price
        if self.type1=='video':
            self.price=self.price-0.15*self.price
        elif self.type1=='audio':
            self.price=self.price-0.1*self.price
        else:
            self.price=self.price-0.05*self.price
            
        
class PrintedBook(Book):
    def __int__(self,bookid,bookname,price,authorname,publisher,isbn,pages,year):
        super().__init__(bookid,bookname,price,authorname)
        self.publisher=publisher
        self.isbn=isbn
        self.pages=pages
        self.year=year
    def addBook(self):
        l1=[
            self.bookid,
            self.bookname,
            self.price,
            self.authorname,
            self.publisher,
            self.isbn,
            self.pages,
            self.year
        ]
        l2.append(l1)
    def viewBook(self,bid):
        for i in res:
            if bid in i:
                print(res)
        
        
class Ebook(Book):
    def __init__(self,bookid,bookname,price,authorname,type1,size):
        super().__init__(bookid,bookname,price,authorname)
        self.type1=type1
        self.size=size
    def addBook(self):
        l3=[
            self.bookid,
            self.bookname,
            self.price,
            self.authorname,
            self.type,
            self.size,
        ]
        l4.append(l3)
    def viewallBooks(self,btype):
        for i in res:
            if btype in i:
                print(res)
               
            
i=int(input("enter 1 to add Printed books and 2 to add Ebooks-->"))
while(i!=0):
    bookid=int(input("Enter book id-->"))
    bookname=input("Enter book name-->")
    price=int(input("Enter book price-->"))
    authorname=input("Enter author name-->")
    if i==1:
        publisher=input("enter publisher name-->")
        isbn=int(input("Enter isbn num-->"))
        pages=int(input("Enter no of pages-->"))
        year=int(input("Enter year of publishng-->"))
        p=PrintedBook(bookid,bookname,price,authorname,publisher,isbn,pages,year)
        p.addBook()
        p.CalDiscount()
    else:
        type1=input("enter type name-->")
        size=int(input("Enter size-->"))
        e=Ebook(bookid,bookname,price,authorname,type1,size)
        e.addBook()
        e.CalDiscount()
    i=int(input("enter 1 to add Printed books and 2 to add Ebooks-->"))
i=int(input("Enter 1 to search book based on book type and 2 to search book based on book id-->"))
while(i!=0):
    if i==1:
        btype=input("Enter type of book-->")
        for i in l4:
            if btype in i:
                res=l4
                flag=1
                break
    else:
        bid=int(input("Enter book id-->"))
        for i in l4:
            if bid in i:
                res=l4
                break
    if(flag==1):
        Ebook.viewallBooks(btype)
    else:
        PrintedBook.viewBook(bid)
    i=int(input("Enter 1 to search book based on book type and 2 to search book based on book id-->"))
print("Thank you for visiting our store!!!")
        