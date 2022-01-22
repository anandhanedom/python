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


test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"

# test_phrase = "This is a string! But has punctuation. How can we remove it?"
# test_phrase = "sdsd..sssddd..sdddsddd...dsds...dsds...dssssss...sddddd"

# test_patterns = ["sd*"]  # s followed by 0 or more d's
# test_patterns = ["sd+"]  # s followed by 1 or more d's
# test_patterns = ["sd?"]  # s followed by 0 or 1 d
# test_patterns = ["sd{3}"]  # s followed by 3 d's
# test_patterns = ["sd{2,3}"]  # s followed by 2 or 3 d's
# test_patterns = ["s[sd]+"]  # s followed by 1 or more s's or d's

# test_patterns = ["[^!.?]+"]  # excluding symbols
# test_patterns = ["[a-z]+"]
# test_patterns = ["[A-Z]+"]

# test_patterns = [r"\d+"]
# test_patterns = [r"\D+"]
# test_patterns = [r"\s+"]
# test_patterns = [r"\S+"]
# test_patterns = [r"\w+"]
test_patterns = [r"\W+"]


multi_re_find(test_patterns, test_phrase)
