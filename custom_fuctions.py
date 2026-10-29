def greet():
    print("hello")


def greeting(name):
    print(f"Hello {name}")


# greet()  #call == use no arguments/ params == data

# greeting("Alice")
# greeting("Bob")
# greeting("Charlie")
# greeting("Maggie")

def volume_cylinder(radius, height):
    v = 22 / 7 * radius ** 2 * height
    print(round(v, 2))


volume_cylinder(5, 5)
volume_cylinder(20, 45)


def volume_cylinder_better(radius, height):
    v = 22 / 7 * radius ** 2 * height
    return v


result = volume_cylinder_better(5, 10)
print(round(result, 2))

with open("volume.txt", "w") as file:
    file.write(str(result))


def volume_surface(radius, height):
    v = 22 / 7 * radius ** 2 * height
    a = 22 / 7 * radius ** 2 * 2 + 22 / 7 * radius * 2 * height
    return v, a


volume, area = volume_surface(5, 25)
print(f"Volume is {volume}, area is {area}")

# named parameters
v, a = volume_surface(5, 10)
print(f"Volume is {v}, area is {a}")


def divide(x, y, should_round=False):
    # return x/y
    res = x / y
    if should_round == True:
        return round(x, y)
    else:
        return res


print(divide(4, 2, should_round=True))
