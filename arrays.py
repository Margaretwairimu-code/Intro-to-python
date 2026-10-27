# #store many items
ages = [21, 72, 43, 76, 23, 78, 88, 90, 15]  # list

names = ["Zack", "Jane", "Margaret", "Alice"]

# functions
ages.append(31)
# ages.clear
# ages.sort()
# ages.reverse()
print(ages)

# names.sort()
print(names)

jack_count = names.count("Jack")
print(jack_count)

print(len(names))
print(len(ages))

print(sum(ages) / len(ages))

# retrieve an element
print(ages[0])
print(ages[5])

print(names[0])
print(names[-1])
print(names[-2])
print(names[-3:])  # slicing a list

print(ages[3:])
print(ages[3:5])  # slicing
print(ages[:3])

# set
scores = {88, 78, 88, 65, 77, 78}
print(scores)

# tuple immutable
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays[0])

# dictionary
person = {"name": "Jason", "age": 22, "weight": 60, "height": 159}
print(person["name"])

people = [{"name": "Zuri", "age": 29}, {"name": "Lenny", "age": 20}, {"name": "John", "age": 16},
          {"name": "Ann", "age": 39}]
print(people[0]["name"])
