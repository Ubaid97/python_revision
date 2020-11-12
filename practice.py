# declare a list with numbers 1 to 5 and add 6 at the end of list
num_list = [1, 2, 3, 4, 5]
print(num_list)
num_list.append(6)
print(num_list)

# create a tuple with values 1-5
num_tuple = (1, 2, 3, 4, 5)
# tuples are immutable, you cannot add or remove items from them
print(type(num_tuple))

# declare a set with values 1-5, and print the values up to 3
num_set = {1, 2, 3, 4, 5}
for num in num_set:
    if num <= 3:
        print(num)

