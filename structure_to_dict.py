# Convert list of tuples to dict
print(dict([("a", 1), ("b", 2), ("c", 3)]))

# Convert two lists to dict via zip
print(dict(zip(["x", "y", "z"], [10, 20, 30])))

# Convert Student object to dict via vars
class Student:
    def __init__(self, name, age):
        self.name, self.age = name, age

print(vars(Student("Ada", 20)))
