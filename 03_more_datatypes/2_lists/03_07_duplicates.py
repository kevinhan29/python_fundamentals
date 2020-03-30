'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

for x in list_:                                  # read through list
    for y in range(list_.count(x) - 1):         # remove all counts of current list item  if it appears more than once
        list_.remove(x)
        #print(list_)

print(list_)