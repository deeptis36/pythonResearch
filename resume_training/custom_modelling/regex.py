import re

s = 'geeks.for.geeks'

# without using \
match = re.search(r'.', s)
print(match)

# using \
match = re.search(r'\.', s)
print(match)



string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)

print(result)


regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')

string = "Hello World!"
pattern = r"World!$"
print(string)
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""
regex = '\d+'

match = re.findall(regex, string)
print(string)
print(match)

p = re.compile('[a-e]')
string = "Aye, said Mr. Gibenson Stark"
print(string)
print(p.findall(string))