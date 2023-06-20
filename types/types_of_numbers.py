# there can be 3 types of numbers int, float and complex
number1, number2, number3 = 0, 0.1, 1j

print(number1)
print(number2)
print(number3)

type_of_number1 = type(number1)
type_of_number2 = type(number2)
type_of_number3 = type(number3)

print(type_of_number1)
print(type_of_number2)
print(type_of_number3)
# we are able to convert integer numbers into floats and complex values
number1_1 = float(number1)
number1_2 = complex(number1)

# we are able to convert complex and float numbers into integers
number2_1 = int(number2)
number2_2 = complex(number2)

# we can't convert complex numbers into float or int values
# number3_1 = float(number3)
# number3_2 = int(number3)

print()
# print(*[number1_1, number1_2, number2_1, number2_2])
