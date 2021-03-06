'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''

list_ = ["hello world!"]

try:
    print(list_[1])
except IndexError as err:
    print(err)
except:
    print("Something else went wrong")
finally:
    print("finished executing code...")
