
details = ['ahmed', 'a@a.com', 35, '01025465465', '0152146554']
name, mail, age, *phone_numbers = details

print(mail)
print(name)
print(phone_numbers)

# ______________________________________________________________

data = [
    ('male', 10, 12),
    ('female', 5, 7, 12)
]


def males(data):
    return sum(data)


def females(data):
    return sum(data) * 2


for tag, *details_ in data:
    if tag == 'male':
        print(males(details_))
    if tag == 'female':
        print(females(details_))


# ______________________________________________________________

def path_splitter(path: str):
    *root, dirName, fileName = path.split('\\')
    return {"dir name": dirName,
            "file name": fileName}


print(path_splitter(r"/Data_structures_and Algorithmes/useful_astrisk.py"))

