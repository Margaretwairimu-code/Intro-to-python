def add(a, b, c):
    result = a + b + c
    return result


def addition(*numbers):
    """
    Returns the sum of numbers passed as arguments
    Parameters:
       integers or floats or a mix of integers and floats
    Return:
       Integer or float
    """
    total = sum(numbers)
    return total


# call function
# print(add(1,2,3))

print(addition(10, 20, 15))
print(addition(1, 2, 3))
print(addition(1, 2, 3, 4))


def build_profile(**kwargs):
    for k, w in kwargs.items():
        print(f"{k}: {w}")


build_profile(experience=100, name="jane", age="24")


def fancy_function(name, *nums, **kwargs):
    print(f"{name}: {nums} {kwargs}")


# anonymous = lambda
def square(num):
    return num * num


result = square(5)
print(result)

square = lambda num: num * num
result = square(13)
print(result)

surface_area_cylinder = lambda r, h: 22 / 7 * r ** 2 * 2 + 22 / 7 * 2 * r * h
print(surface_area_cylinder(4, 20))

people = [
    {"name": "Maggie", "age": 18, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "France"},
    {"name": "Ethan", "age": 16, "city": "Germany"},
]

sorted_by_age = sorted(people, key=lambda x: x["name"], reverse=True)
print(sorted_by_age)
