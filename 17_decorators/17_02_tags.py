'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''

def html_tagger(func):
    def wrapper(*args):
        return(f"<{args[1]}>{args[0]}</{args[1]}>")
    return wrapper

@html_tagger
def some_text(text, tag):
    pass

print(some_text("CodingNomads", "html"))