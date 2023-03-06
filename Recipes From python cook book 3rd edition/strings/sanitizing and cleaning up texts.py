import unicodedata

string1 = "ä, ë, ï, ö, ü, ÿ, Ä, Ë, Ï, Ö, Ü, Ÿ"
# resultString = unicodedata.normalize('NFD', string1)
# print(resultString.encode('ascii', 'ignore').decode('ascii'))


def sanitize(string: str) -> str:
    normalized_string = unicodedata.normalize('NFD', string)
    return normalized_string.encode('ascii', 'ignore').decode('ascii')


print(string1)
print(sanitize("ä, ë, ï, ö, ü, ÿ, Ä, Ë, Ï, Ö, Ü, Ÿ"))
