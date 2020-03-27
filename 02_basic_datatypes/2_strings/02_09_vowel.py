'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

sentence = input("Please enter a sentence: ")

# finding number occurrences of each vowel
a = sentence.count("a")
A = sentence.count("A")
e = sentence.count("e")
E = sentence.count("E")
i = sentence.count("i")
I = sentence.count("I")
o = sentence.count("o")
O = sentence.count("O")
u = sentence.count("u")
U = sentence.count("U")

total = a + e + i + o + u + A + E + I + O + U      # total number of vowels
print("there are ", total, " vowels in your sentence")

# CHALLENGE: Print occurrences of each vowel that occurs
# First combine upper and lower case occurrences
a_total = a + A
e_total = e + E
i_total = i + I
o_total = o + O
u_total = u + U

# only prints vowels that actually occur
if a_total != 0:
    print("the letter 'a' appears ", a_total, " times")
if e_total != 0:
    print("the letter 'e' appears ", e_total, " times")
if i_total != 0:
    print("the letter 'i' appears ", i_total, " times")
if o_total != 0:
    print("the letter 'o' appears ", o_total, " times")
if u_total != 0:
    print("the letter 'u' appears ", u_total, " times")