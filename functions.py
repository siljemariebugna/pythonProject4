def greet(name):
    """
    simple greet function, print hello
    :return: none
    """
    print(f"Hello, {name}")

# greet("Bogdan")
# greet("Silje")
#greet("Pie")

def special_op(x, y, z) :
    """
    some special operation
    :param x: int or float
    :param y: int or float
    :param z: int or float
    :return: the result of the operation
    """
    return x * y + z

result = special_op(2, 3, 4)
print(result)

greet(special_op(2, 3, 4))
# function calling another function
