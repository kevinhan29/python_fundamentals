'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''
import random

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

class Dog:
    def __init__(self, gender, age, name = "Dog", breed = "mixed", in_heat = False):
        self.name = name
        self.breed = breed
        self.gender = gender.lower()
        self.age = age
        self.in_heat = in_heat

    def __str__(self):
        return f"{self.name} is a {self.age} yr old {self.gender} {self.breed}"

    def __add__(self, other_dog):
        """ Attempts to breed 2 dogs together.  If successful, returns a new Dog object """
        if (self.gender == other_dog.gender) or (not self.in_heat) or (not other_dog.in_heat):  # checks whether breeding conditions are right
            print(f"Sorry, {self.name} and {other_dog.name} are incompatible right now :(")
            return None
        # A new Dog object can be created! Randomly determine gender first
        print("Congrats, you got a new puppy!")
        temp = random.randint(0,1)
        if temp == 0:
            puppy_gender = "male"
        else:
            puppy_gender = "female"
        # Determine breed of new Dog and create new Dog object
        if self.breed == other_dog.breed:
            return Dog(puppy_gender, 0, "Puppy", self.breed)
        else:
            return Dog(puppy_gender,0, "Puppy")

    def Bark(self):
        print(f"{self.name}: Woof Woof!")

class Computer:
    def __init__(self, brand, type, os, is_on = True):
        """ initalizes computer brand, type (laptop/desktop/tablet), operating system, and is on or not """
        self.brand = brand
        self.type = type
        self.os = os
        self.is_on = is_on

    def __str__(self):
        if self.is_on:
            return f"Your {self.brand} {self.type} is currently on"
        else:
            return f"Your {self.brand} {self.type} is currently off"

    def Power(self):
        if self.is_on:
            print(f"You turned off your {self.brand} {self.type}")
        else:
            print(f"You turned on your {self.brand} {self.type}")
        self.is_on = not self.is_on

book1 = Book("To Kill a Mockingbird", 300)
book2 = Book("The Da Vinci Code", 500, 24)
print(book1)
book1.turnPage(40)
print(f"You are {book1.progress()}% done with {book1.title}\n")
print(book2)
for i in range(20):
    book2.turnPage()

print("\n")

dog1 = Dog("male", 3, "Warren", "English Retriever", True)
dog2 = Dog("female", 2, "Toaster", "Golden Retriever", True)
dog3 = Dog("female", 4, "Andie", "Border Collie")
print(dog1)
print(dog2)
print(dog3)
dog4 = dog1 + dog2
print(dog4)
dog4.Bark()
dog5 = dog2 + dog3
print(dog5)

print("\n")

comp1 = Computer("Apple", "laptop", "OS X")
comp2 = Computer("Google", "tablet", "Chrome OS", False)
print(comp1)
comp1.Power()
print(comp1, "\n")
print(comp2)
comp2.Power()
