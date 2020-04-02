'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

Will use 06_02_stats function and break it into 3 separate ones
'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def all_stats(numbers: list):
    return [min_value(numbers), max_value(numbers), summation(numbers), avg_value(numbers)]

def min_value(numbers: list) -> int:
    min_ = numbers[0]
    for x in numbers:
        if x < min_:  # finding minimum value
            min_ = x
    return min_

def max_value(numbers: list) -> int:
    max_ = numbers[0]
    for x in numbers:
        if x > max_:  # finding maximum value
            max_ = x
    return max_

def summation(numbers: list) -> int:
    sum_ = 0
    for x in numbers:
        sum_ += x  # summing all numbers
    return sum_

def avg_value(numbers: list):
    avg_ = summation(numbers)/len(numbers)
    return avg_

# call the function below here
stats = all_stats(example_list)
print("The minimum value is:", stats[0], "\n" \
    "The maximum value is:", stats[1], "\n" \
      "The sum is:", stats[2], "\n" \
      "The average is:", stats[3])

