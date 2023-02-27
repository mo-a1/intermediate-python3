import re

# .math()
dates = ['7/11/1999', '21/jun/2015']
d_string = 'my name is mohamed ali, my birth day is 7/11/1996, day today is 3/11/2022'

for date in dates:
    if re.match(r'\d+/\d+/\d+', date):
        print(date, '---- .match()')

# .compile()
# create a pattern object
d_pattern = re.compile(r'\d+/\d+/\d+')

for date in dates:
    if re.match(d_pattern, date):
        print(date, '---- by create pattern object')

# .findall()
d = re.findall(d_pattern, d_string)
print(d, '----- re.findall')

# using groups in pattern object
g_d_pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
my_date = g_d_pattern.match('7/11/1996')

day = my_date.group(1)
print(day, '---- .group(1)')


day, month, year = my_date.groups()

print(day, month, year)

# .sub()
# NOTE: we must use pattern with groups when using sub()
new_string = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', d_string)
print(new_string, ' ---- re.sub')

# .compile() -> .sup()
new_string = re.sub(g_d_pattern, r'\3-\2-\1', d_string)
print(new_string)
new_string = g_d_pattern.sub(repl=r'\3-\2-\1', string=d_string)
print(new_string)

# ################# Examples ################## #

# ################# Ex 1 ################## #

string_1 = 'Ahmed says "no." ali says "yes."'
print(re.findall(pattern=r'"(\w+.)"', string=string_1))

# ################# Ex 2 ################## #
# (?:   )

string_2 = '"""this is. python multy\nline comment"""'
comment_pattern = re.compile(pattern=r'"+((?:.|\n)*?)"+')
print(re.findall(pattern=comment_pattern, string=string_2))
# or
comment_pattern = re.compile(pattern=r'"+(.*?)"+', flags=re.DOTALL)
print(re.findall(pattern=comment_pattern, string=string_2))
