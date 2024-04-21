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



#  3. findall function
#  finds all the occurance of the pattern
findall = re.findall('i', string)
print(f'lists all the occurances of the pattern inside the sttring',findall)


#  Sub funciton it replaces the pattern syntax re.sub('i', 'I', string)
string_two = 'artificial intelligence engineer course'
substitute = re.sub('i', 'I', string_two)
print(f'subsitute sub function ',substitute)
print(f'subsitute sub function ',substitute)



# 4. Finditer function
string_1 = 'this is a python regular expression session'
finditer = re.finditer('a-d', string_1)
for i in finditer:
    print(i)
    print(i.start(), i.end(), i.group())