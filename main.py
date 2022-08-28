#   SPECIAL SYMBOLS
# . - any single symbol

# .. - 2 any symbols

# [] - any one symbol inside of brackets -
# [Ii] - search for I or i
# [a-d] - range of symbols to search
# [a-d]. - range of symbols to search symbol + one any symbol "."

# [^s] - find all except 's'
# [^sw] - find all except 's' or 'w'

# $ - end of string

# \ - screening - \. - search for '.' but not for any symbol

# ^ - beginning of string

# \n - new line string (line break)

# \d - any singe digit
# \d\d - two any singe digits

# \D - everything, except digits

# \s - search for blanc space

# \S - everything except spaces

# \w - any letter or figure

# \W - everything except letter and figures

# \b - border (limits: start-end) of words
# \b\w\w\w\b - any 3 letter word

# \B - everything except word border

# Quantification
# \b\w{3}\b - any 3 letter word

# {4} - quantity to repeat
# n{4-6} - search for 4 to 6 symbols 'n'
# * - 0 and more
# + - 1 and more

# ? - 0 or 1 times (be?) - b or be

# (\s | -) - "space" or "-" (ex: \d{4}(\s|-)\d{4}

import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'

res = re.match('AC', s)  # search in the beginning of string
print(1, res)

print()

res = re.match('DC', s)
print(2, res)

print()

res = re.search('DC', s)
print(3, res)
print(res[0])

print()

res = re.split('/', s)
print(4, res)

print()

res = re.split('/', s, maxsplit=3)
print(4.1, res)

print()

res = re.findall('DC', s)
print(5, res)

print()

res = re.sub('DC', 'SEX', s)
print(6, res)

print()

res = re.fullmatch('SEX', s)
print(7, res)

print()

s = 'SEX'
res = re.fullmatch('SEX', s)
print(7, res)
