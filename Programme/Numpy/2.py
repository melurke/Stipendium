z = 0.5

def X(z):
    if z > 3:
        x = 27
        x += 4 * (z - 3)
    elif z > 1:
        x = 15
        x += 6 * (z - 1)
    elif z == 1:
        x = 15
    else:
        x = 0
    return x

print(X(z))