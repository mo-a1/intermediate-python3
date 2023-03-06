import re


def get_ib(file):
    with open(file, mode="r", encoding="utf-8") as ib_file:
        ib_list = []
        pattern = re.compile(r"[\w{2}:]{17}")
        for line in ib_file:
            ib_list.append(pattern.findall(line))
        yield from ib_list


for ib in get_ib("ib.txt"):
    print(ib)

print("== 1 " * 20)

with open("ftb_links.txt", "r", encoding="utf-8") as ftb_links:
    results = []
    pattern = re.compile(r"ftp://ftp\d{0,2}\.\w+(\.\w+)?(\w\.\w+)?(\.\w+)/pub/FreeBSD/", flags=re.M)
    for link in ftb_links:
        a = pattern.search(link)
        if a is not None:
            print(a.group())

print("== 2 " * 20)

# Named groups
my_name = "Mohamed Ali "
pattern = re.compile(r"(?P<first_name>\w+) (?P<last_name>\w+)")
print(pattern.groupindex)
print(pattern.search(my_name).groups())
print(pattern.search(my_name).groupdict()['first_name'])
print(pattern.search(my_name).groupdict()['last_name'])

print("== 3 " * 20)

with open("phone_numbers.txt", "r", encoding="utf-8") as mobiles:
    with open("modified_nums.txt", "w", encoding="utf-8", newline="") as edited:
        pattern_1 = re.compile(r"\(")
        pattern_2 = re.compile(r"[)|-]")
        pattern_3 = re.compile(r"\+\d+\s")
        for mobile in mobiles:
            if re.match(pattern_1, mobile):
                mobile = pattern_1.sub("", mobile)
            mobile = pattern_2.sub(" ", mobile)
            mobile = pattern_3.sub("", mobile)
            edited.write(mobile)
            print(mobile.rstrip("\n"))
