from collections import namedtuple

user = namedtuple("user", "f_name l_name age gender", defaults=None)
amal = user('amal', 'ali', 50, 'female')
print(user)
print(amal)  # user(f_name='amal', l_name='ali', age=50, gender='female')
print(amal[0])

print("---" * 20)
# use defaults
user = namedtuple("user", "f_name l_name age gender", defaults=["no data", "no data", "no data", "male"])
# NOTE: it starts putting default values from the right
akram = user("")
print(akram)
# check default values
print(user._field_defaults)

print("== 1 " * 20)
# ._replace()
# replace values of tuple objects
employ = namedtuple("Employ", "name age")
ahmed = employ("ahmed", 27)
print("original: ", ahmed)
print("after replace: ", ahmed._replace(age="37"))
print("the original still the same: ", ahmed)
print("== 2 " * 20)

# ._asdict()
print(ahmed._asdict())
print("== 3 " * 20)

# ._make(iterable)
# Class method that makes a new instance from an existing sequence or iterable.
lis = ["mazen", 45]
print(employ._make(lis))
print("== 4 " * 20)

print(ahmed._fields)
print(user._field_defaults)
print("== 5 " * 20)

# convert dict to namedtuple

point = namedtuple("Point", "x y z", defaults=[0, 0, 0])
start_point_dict = {"x": 14, "y": 20}
start_point_ntuple = point(**start_point_dict)
print(start_point_ntuple)
