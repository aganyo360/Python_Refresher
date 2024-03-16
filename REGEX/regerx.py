import re
#  the Regular has so many inbuild expresions

# 1. Match Function  re.match(pattern, string)  check pattern at the beginning of the targeted string else returns none
string = 'I am learning fundamental of data engineering'
matching = re.match('I', string)
print(f'matching',matching)

# 2. Search function
#  if the match is available then it returns the atch 
#  if first occurance it will return not considering the second occurance
searching = re.search('a', string)
print(f'searching', searching)