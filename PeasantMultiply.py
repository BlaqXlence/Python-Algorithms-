def peasant_multiply(x, y):
    prod = 0
    while x > 0:
        if x % 2 == 1:
            prod += y
        x = x // 2
        y = y + y
    return prod


x = 2
y = 2
prod = peasant_multiply(x, y)
print(x, "*", y, "=", prod)
