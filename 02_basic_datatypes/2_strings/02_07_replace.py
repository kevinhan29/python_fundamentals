'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# asks for user inputs
sentence = input("Type in any sentence: ")
symbol = input("Enter in a symbol: ")

sentence = sentence.replace(sentence[0], symbol)       # replace all occurrences of the first letter with the symbol
print(sentence)