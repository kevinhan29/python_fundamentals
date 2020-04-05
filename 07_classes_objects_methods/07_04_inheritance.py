'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''

class Movie:
    def __init__(self, title, year):
        self.year = year
        self.title = title

    def __str__(self):
        return f"{self.title} is a movie released in {self.year}"

class RomCom(Movie):
    def __str__(self):
        return f"{self.title} is a romantic comedy movie released in {self.year}"

class ActionMove(Movie):
    def __init__(self, title, year, pg = 13):
        super().__init__(title, year)
        self.pg = pg

    def __str__(self):
        return f"{self.title} is a PG-{self.pg} action movie released in {self.year}"

movie1 = RomCom("Definitely, Maybe", 2008)
movie2 = ActionMove("Avengers: End Game", 2019)
print(movie1)
print(movie2)