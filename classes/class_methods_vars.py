names = [
    'aganyo', 'eunice', 'hillary',' kendal'
]
for name in names:
    print(name.title().strip())

numbers =list(range(1,7)) 
print(numbers)


#when we introduce a third argument in range it acts a skipping value
even_numbers = list(range(2,21,2))
print(f'The even numbers are:',even_numbers)

# the below code fragment prints odd numbers in form of lists

odd_numbers = list(range(1,21,2))
print(f'The odd numbers are:',odd_numbers)