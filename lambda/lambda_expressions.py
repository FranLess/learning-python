# lambda expression are something like anonymous function calls
# PD: it is more like row functions
# what this function return is another function, so we convert a variable into a function
def increment_lambda(n):
    """"fasdfasdf"""
    return lambda x: x + n


f = increment_lambda(10)
print(f(1))
print(f(123))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'),
         (4, 'four'), (5, 'five'), (6, 'six')]
# here key is passed because sort method doesn't accept positional arguments
numbers = [(2, 'two'), (1, 'one'), (3, 'three')]
numbers.sort(key=lambda x: x[0])
print(numbers)
# what sort does is like an foreach, it recibes the item of the array and it sorts the array by the field we want
# in this case, if we choose field 2 then it will sort the array by the field 2 of the tuples in the array
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# we can documentate the function, well, explain its behavior by writting strings inside the function
# and then, we can print the property of the function __doc__ so we can see the string written in the function
# on the console


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(__doc__)
