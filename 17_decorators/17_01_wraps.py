'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''

def html_tag(func):
    def wrapper(func):
        return(f"<p>{func}</p>")
    return wrapper

@html_tag
def some_text(m):
    return m

print(some_text("CodingNomads"))