'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def math_operator(*args, **kwargs):
    temp = args[0]
    for i in range(1, len(args)):
        if kwargs["operator"] == "+":
            temp = temp + args[i]
        elif kwargs["operator"] == "-":
            temp = temp - args[i]
        elif kwargs["operator"].lower() == "x":
            temp = temp * args[i]
        elif kwargs["operator"] == "/":
            temp = temp / args[i]
        else:
            return "Invalid Operator"
    return temp

print(math_operator(1, 2, 3, operator = "+"))
print(math_operator(1, 2, 3, operator = "-"))
print(math_operator(1, 2, 3, operator = "X"))
print(math_operator(1, 2, 3, operator = "/"))
print(math_operator(1, 2, 3, operator = "hi"))
