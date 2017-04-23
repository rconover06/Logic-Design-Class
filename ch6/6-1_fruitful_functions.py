# Raul Conover

biggest =  max(3, 7, 2, 5)
x = abs(3 - 11) + 10

def area(radius):
    b = 3.14159 * radius**2
    return

def area(radius):
    return 3.14159 * radius * radius

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
print(x)
# The above can be  rewritten with out the else statement.
def absolute_value(x):
    if x < 0:
        return -x
    return x

print(x)

def bad_absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x

print(bad_absolute_value(0))
