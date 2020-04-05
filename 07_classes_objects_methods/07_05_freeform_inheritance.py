'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Book:
    def __init__(self, title, num_pages, current_page = 1):
        self.title = title
        self.num_pages = num_pages
        self.current_page = current_page

    def __str__(self):
        return f"You are on page {self.current_page} of {self.title}"

    def turnPage(self, page = None):
        """ Go to a specific page in the book.  Goes to the next page if no argument passed.  Returns page number """
        if page == None:
            self.current_page += 1
        elif (page > self.num_pages) or (page < 1):
            print(f"There is no page {page} in {self.title}")
            return
        else:
            self.current_page = page
        print(f"You turned to page {self.current_page} in {self.title}")
        return self.current_page

    def progress(self):
        """ Returns progress of how far in the book you are, in percentage """
        return 100 * self.current_page // self.num_pages

class TextBook(Book):
    def __init__(self, subject, title, num_pages, current_page = 1):
        self.subject = subject
        super().__init__(title, num_pages, current_page)

class Computer:
    def __init__(self, brand, is_on = True):
        """ initalizes computer brand, and is on or not """
        self.brand = brand
        self.is_on = is_on

    def __str__(self):
        if self.is_on:
            return f"Your {self.brand} is currently on"
        else:
            return f"Your {self.brand} is currently off"

    def Power(self):
        if self.is_on:
            print(f"You turned off your {self.brand} computer")
        else:
            print(f"You turned on your {self.brand} computer")
        self.is_on = not self.is_on

class AppleComputer(Computer):
    def __init__(self, is_on = True):
        super().__init__(is_on)
        self.brand = "Apple"

class iPad(AppleComputer):
    def __init__(self, screen_size, is_on = True):
        super().__init__(is_on)
        self.os = "iPad OS"
        self.isPortable = True
        self.screen_size = screen_size

class iMac(AppleComputer):
    def __init__(self, screen_size, is_on = True):
        super().__init__(is_on)
        self.os = "OS X"
        self.isPortable = False
        self.screen_size = screen_size

book1 = TextBook("Math", "Algebra II", 1000)
print(book1)
print(book1.subject)
book1.turnPage()
book1.turnPage(48324)

print("\n")

comp1 = iPad(11)
print(comp1)
print(comp1.screen_size, comp1.os)
comp1.Power()

comp2 = iMac(27)
print(comp2, comp2.os)