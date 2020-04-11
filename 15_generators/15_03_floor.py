'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
x = [5, 1111, 9, 0, 8888, 983, 50938239, 192838, 9301, 9999]

gen = (i // 1111 for i in x)

for num in gen:
    print(num)

