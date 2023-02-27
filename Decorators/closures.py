def outer():
    name = "ali"

    def inner():
        print(f"my name is {name}")

    return inner


outer()()
func = outer()
func()
print(func.__name__)

print('==1' * 30)


def outer(name):
    name_ = name

    def inner():
        print(f"my name is {name_}")

    return inner


new_func_1 = outer('mazen')
new_func_2 = outer('kareem')
new_func_1()
new_func_2()

print('==2' * 30)


def tagging(tag):
    def content(text):
        return f"<{tag}>{text}<{tag}/>"

    return content


p = tagging('p')
paragraph_1 = p('test')
print(paragraph_1)
heading = tagging('h1')
head_1 = heading('my title')
print(head_1)

print('==3' * 30)


def function(func_):
    def do_it(*args):
        return func_(*args)
    return do_it


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


adding = function(add)
print(adding(2, 3))
multiplication = function(mul)
print(multiplication(4, 4))
