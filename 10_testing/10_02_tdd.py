'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''

# Function that divides two numbers, takes 2 args, numerator and denominator
def test_DivisionResult():
    assert Division(10, 5) == 2

def test_Division_InvalidArguments():
    assert Division(10, "5") == None

def test_Division_DivideByZero():
    assert Division(10, 0) == "Cannot divide by Zero"