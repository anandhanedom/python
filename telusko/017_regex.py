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

# meta character syntax
def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print(f"Searching for pattern {pattern}")
        print(re.findall(pattern, phrase))
        print("\n")


test_phrase = "sdsd..sssddd..sdddsddd...dsds...dsds...dssssss...sddddd"
# test_patterns = ["sd*"]  # s followed by 0 or more d's
# test_patterns = ["sd+"]  # s followed by 1 or more d's
# test_patterns = ["sd?"]  # s followed by 0 or 1 d
# test_patterns = ["sd{3}"]  # s followed by 3 d's
test_patterns = ["sd{2,3}"]  # s followed by 2 or 3 d's

multi_re_find(test_patterns, test_phrase)
