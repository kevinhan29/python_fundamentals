'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
result = {}

# add keys from dict_1 to result and pair them with the sum of respective values from dict_1 and dict_2
for k in dict_1:
    result[k] = dict_1[k] + dict_2.get(k, 0)
    # print(result)

# add keys from dict_2 that don't overlap with dict_1 to result and their respective values
for k in dict_2:
    if result.get(k) == None:
        result[k] = dict_2[k]
        #print(result)

# print final dictionary
print(result)