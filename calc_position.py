import re
import sys

def get_number_at_pos(text, pos):
    return text[pos]

def get_numbers_at_pos(text, pos, length = 5):
    return text[pos:pos + 5]


with open("pi_million", "r") as f:
    text = f.read()

try:
    if len(sys.argv) > 1:
        number = sys.argv[1]
    else:
        number = input("Search for: ")
    _ = int(number)
except ValueError:
    print("Input has to be a number")
    exit()

match = re.search(rf"{number}", text)

if match:
    found_pos = int(match.start(0)) + 1
    i = found_pos
    print("Number found at position " + str(i), end=", ")
else:
    print("Number could not be found")
    exit()

num_rows = 46
num_cols = 52

first_line = 36
first_page = 40 * 52

if i <= first_line:
    print("which is on Page 3, Line 1, Position " + str(i) + ".")
    exit(0)

i -= first_line

if i <= first_page:
    line = i // num_cols + 2
    col = i % num_cols
    print("which is on Page 3, Line " + str(line) + ", Position " + str(col) + ".")
    print("Line begins with " + get_numbers_at_pos(text, found_pos - col) + ".")
    exit(0)

i -= first_page

page = i // (num_rows * num_cols) + 2
i -= (page - 2) * num_rows * num_cols

line = i // num_cols
col = i % num_cols

print("which is on Page " + str(page + 2) + ", Line " + str(line) + ", Position " + str(col) + ".")
print("Line begins with " + get_numbers_at_pos(text, found_pos - col) + ".")
