'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''

def Triple(val):
    try:
        temp = val
        float(temp)
    except ValueError:
        print("That's not a number")
        return None
    else:
        return val*3

def test_Triple_Multiply():
    assert Triple(2) == 6

def test_Triple_IncorrectTypeCatch():
    assert Triple("hello") == None