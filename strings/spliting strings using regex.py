import re

line = 'name, word; ali name,kareem'
print(re.split(r',\s?|;\s?|\s{1,}', line))