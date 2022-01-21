import re

patterns = ["term1", "term2"]


text = "This is a string with term1, not not the other!"

split_term = "@"
email = "user@gmail.com"

# search
match = re.search("term1", text)
print(match)
print(match.start())

# split
match1 = re.split(split_term, email)
print(match1)

# instances
print(re.findall("match", "test phrase match in middle"))
