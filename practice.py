# declare a list with numbers 1 to 5 and add 6 at the end of list
num_list = [1, 2, 3, 4, 5]
print(num_list)
num_list.append(6)
print(num_list)

# create a tuple with values 1-5
num_tuple = (1, 2, 3, 4, 5)
# tuples are immutable, you cannot add or remove items from them
print(num_tuple[0:3]) # prints first 3 items
print(type(num_tuple))

# declare a set with values 1-5, and print the values up to 3
num_set = {1, 2, 3, 4, 5}
# print(num_set[0:3]) - will not work
for num in num_set:
    if num <= 3:
        print(num)

# declare a dictionary of a shopping list with 3 items
shopping_dict = {"eggs": "£1.24", "bread": "£2.00", "milk": "£1.50"}
# print the price of bread
print(shopping_dict["bread"])
# add an item to the dictionary
shopping_dict["soup"] = "£3.50"
print(shopping_dict["soup"])


write a function that takes two arguments and adds them together
def add(arg1, arg2):
    return arg1 + arg2
print(add(2, 4))


# create a class called person with name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_1 = Person("John", 24)
print(person_1.name)
print(person_1.age)

# create a class Student that inherits from Person class and has a student id and course
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

student_1 = Student("John", "24", "12454", "DevOps")
print(student_1.name)
print(person_1.age)
print(student_1.student_id)
print(student_1.course)

# create a dictionary with int values and create a function to return the sum of ia dictionary's values
some_dict = {
    "eggs": 1.00,
    "bread": 2.00,
    "books": 3.50,
    "milk": 2.85
}

def dict_sum(dict):
    return sum(dict.values())
print(dict_sum(some_dict))

