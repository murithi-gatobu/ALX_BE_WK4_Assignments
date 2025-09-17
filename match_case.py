# Demonstration of match-case statement in Python
value = input("Enter a value: (Should be a value or a string): ")

try:
    num = int(value)
    value_type = "int"
except ValueError:
    try:
        num = float(value)
        value_type = "float"
    except ValueError:
        value_type = "str"

match value_type:
    case "int":
        print("It's an integer!")
    case "float":
        print("It's a float!")
    case "str":
        print("It's a string!")