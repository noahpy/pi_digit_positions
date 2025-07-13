import re

with open("pi_million", "r") as f:
    text = f.read()

number = int(input("Search for: "))

match = re.search(rf"{number}", text)

if match:
    i = int(match.start(0)) + 1
else:
    print("Number could not be found")

num_rows = 46
num_cols = 52

first_line = 36
first_page = 40 * 52

if i <= first_line:
    print("Page 3, Line 1, Position " + str(i))
    exit(0)

i -= first_line

if i <= first_page:
    line = i // num_cols + 2
    col = i % num_cols
    print("Page 3, Line " + str(line) + ", Position " + str(col))
    exit(0)

i -= first_page

page = i // (num_rows * num_cols) + 2
i -= (page - 2) * num_rows * num_cols

line = i // num_cols
col = i % num_cols

print("Page " + str(page + 2) + ", Line " + str(line) + ", Position " + str(col))
