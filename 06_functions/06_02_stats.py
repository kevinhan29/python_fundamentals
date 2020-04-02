'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(numbers: list):
  min_ = numbers[0]
  max_ = numbers[0]
  sum_ = 0
  for x in numbers:
    if x < min_:    # finding minimum value
      min_ = x
    if x > max_:    # finding maximum value
      max_ = x
    sum_ += x       # summing all numbers

  avg_ = sum_/len(numbers)  # calculating average value

  # printing all results
  print(f"""The minimum value is {min_}
The maximum value is {max_}\n\
The average is {avg_}\n\
The sum of all numbers is {sum_}""")
  pass

# call the function below here
stats(example_list)