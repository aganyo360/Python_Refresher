import re
#  the Regular has so many inbuild expresions

# 1. Match Function  re.match(pattern, string)  check pattern at the beginning of the targeted string
string = 'I am learning fundamental of data engineering'
matching = re.match('I', string)
print(matching)