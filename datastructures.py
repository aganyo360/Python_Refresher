# 1) Check if a list contains an element.
def contains_element(lst, element):
    return element in lst

# 2) How to iterate over 2+ lists at the same time
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item1, item2 in zip(list1, list2):
    print(item1, item2)

# 3) Is a list mutable?
# Yes, a list is mutable.

# 4) What is the difference between append and extend?
# append(): Adds its argument as a single element to the end of a list.
# extend(): Iterates over its argument adding each element to the list, extending the list.
# Example:
my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list)  # Output: [1, 2, 3, [4, 5]]
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

# 5) What does “del” do?
# “del” removes an item from a list given its index or slices a list.
# Example:
my_list = [1, 2, 3, 4, 5]
del my_list[2]
print(my_list)  # Output: [1, 2, 4, 5]

# 6) What is the difference between “remove” and “pop”?
# remove(): Removes the first occurrence of a value in a list.
# pop(): Removes the item at the given index from the list and returns it.
# Example:
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]
my_list = [1, 2, 3, 4, 5]
popped_item = my_list.pop(2)
print(popped_item)  # Output: 3

# 7) Write a program to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# 8) Find the index of the 1st matching element
def find_first_index(lst, element):
    return lst.index(element)

# 9) Remove all elements from a list
def remove_all_elements(lst):
    lst.clear()

# 10) Iterate over both the values in a list and their indices
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(index, value)

# 11) How to concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2

# 12) How to manipulate every element in a list by adding value
my_list = [1, 2, 3, 4, 5]
value = 5
manipulated_list = [x + value for x in my_list]

# 13) Count the occurrence of a specific object in a list
def count_occurrence(lst, element):
    return lst.count(element)

# 14) What is the difference between a list and a tuple?
# List is mutable while tuple is immutable.

# 15) Return the length of a list
def get_length(lst):
    return len(lst)

# 16) What is the difference between a list and a set?
# List is an ordered collection with duplicate elements while set is an unordered collection with unique elements.

# 17) How to check if an element is not in a list?
def element_not_in_list(lst, element):
    return element not in lst

# 18) Multiply every element in a list by 5
my_list = [1, 2, 3, 4, 5]
multiplied_list = [x * 5 for x in my_list]

# 19) Combine 2 lists into a list of tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = list(zip(list1, list2))

# 20) Insert a value at a specific index in an existing list
my_list = [1, 2, 3, 5]
value = 4
index = 3
my_list.insert(index, value)

# 21) Remove negative values from a list
my_list = [1, -2, 3, -4, 5]
positive_values = [x for x in my_list if x >= 0]

# 22) Convert a list into a dictionary where list elements are keys
my_list = ['a', 'b', 'c']
dictionary = {key: index for index, key in enumerate(my_list)}

# 23) Remove elements in a list after a specific index
my_list = [1, 2, 3, 4, 5]
index = 2
del my_list[index + 1:]

# 24) Remove elements in a list before a specific index
my_list = [1, 2, 3, 4, 5]
index = 2
del my_list[:index]

# 25) Remove elements in a list between 2 indices
my_list = [1, 2, 3, 4, 5]
start_index = 1
end_index = 3
del my_list[start_index:end_index+1]

# 26) Return every 2nd element in a list between 2 indices
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
start_index = 1
end_index = 5
every_second_element = my_list[start_index:end_index+1:2]

# 27) Write a program to sort a list in ascending and descending order as well
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_ascending = sorted(my_list)
sorted_descending = sorted(my_list, reverse=True)

# 28) Write a program to print even numbers
def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

# 29) Get the first element from each nested list in a list
nested_list = [[1, 2], [3, 4], [5, 6]]
first_elements = [sublist[0] for sublist in nested_list]

# 30) What’s the affect of multiplying a list by an integer?
# Multiplying a list by an integer duplicates the elements of the list that many times.
my_list = [1, 2, 3]
multiplied_list = my_list * 3  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 31) Reverse the order of a list
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]

# 32) What is the difference between reverse and reversed?
# reverse() reverses the elements of a list in place while reversed() returns an iterator that yields the elements of the list in reverse order.
# Example:
my_list = [1, 2, 3, 4, 5]
my_list.reverse()  # In-place reversal
reversed_list = list(reversed(my_list))  # Reversed iterator

# 33) What is the difference between sort and sorted?
# sort() sorts the list in place while sorted() returns a new sorted list without modifying the original list.
# Example:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_list = sorted(my_list)  # Returns sorted list
my_list.sort()  # Sorts the list in place

# 34) Return the minimum value in a list
def get_min_value(lst):
    return min(lst)

# 35) Return the sum of values in a list
def get_sum(lst):
    return sum(lst)
