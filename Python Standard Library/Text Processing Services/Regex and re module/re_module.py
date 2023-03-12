import re

# -- Methods :-
# 'match', 'fullmatch', 'search', 'sub', 'subn', 'split', 'findall', 'finditer',
# 'compile', 'purge', 'template', 'escape', 'error', 'Pattern', 'Match'

# -- Flags :-
# 'ASCII', 'IGNORECASE', 'LOCALE', 'MULTILINE', 'DOTALL', 'VERBOSE', 'UNICODE'

text_1 = """Using a regular expression, you can match a variety <tag> of HTML tags and easily
 extract data in the HTML documents. Using the expression ]*>(.*?), regex can easily match
  the pair that # pyhon comment, opens and closes an HTML 4586vb tag. Without adding any additional detail or
   editing any function, you can use <tag> this regular expression."""

pattern_1 = re.compile(r"(\d{4})\w{2}")   # re.Match object
print(re.search(pattern_1, text_1))
print(re.search(pattern_1, text_1).group())
print(re.search(pattern_1, text_1).groups())
print(re.search(pattern_1, text_1).groupdict())

# email pattern
text_2 = "this is my email: mohamed.elnakeb24@gmail.com"
gmail_pattern = re.compile(r"\w+\.?\w+@gmail.com")
result = gmail_pattern.findall(text_2)  # ['mohamed.elnakeb24@gmail.com']
print(result)

text_3 = 'Today is 11/27/2012. PyCon starts 3/13/2015.'
result = re.sub(r"(\d+)/(\d+)/(\d+)", r"\2-\1-\3", text_3)
print(result)
for i in re.finditer(r"\d+", text_3):
    print(i.group())

# different between re.match and re.search and re.fullmatch

# re.match() checks for a match only at the beginning of the string
# re.search() checks for a match anywhere in the string (this is what Perl does by default)
# re.fullmatch() checks for entire string to be a match

print("match => ", re.match(r"(\d+)/(\d+)/(\d+)", text_3))
print("search => ", re.search(r"(\d+)/(\d+)/(\d+)", text_3))  

print(re.__all__)

# different between re.sub and re.subn
print("sub => ", re.sub(r"(\d+)/(\d+)/(\d+)", r"\2-\1-\3", text_3))      # str
print("subn => ", re.subn(r"(\d+)/(\d+)/(\d+)", r"\2-\1-\3", text_3))    # tuple

