import re

text = 'good 123 mor4nin56g'

x = re.findall(r'\d', text)
y = re.findall('\d+', text)

print(x, y)
