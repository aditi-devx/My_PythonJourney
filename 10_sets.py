empty_set = set()  # how to make an empty set

set1 = { 1, 4,4,4,5,6,6,7,}

set1.add(11)
print(len(set1))
set1.remove(4)
print(set1) # {1, 4, 5, 6, 7} # set will not allow duplicate values
                              #sets are unordered collection of items which means that the items in a set do not have a defined order and cannot be accessed by index. Sets are defined using curly braces {} and the items are separated by commas.


                              #SET UNION AND INTERCETION
                              
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8} # union of two sets will give a new set which will contain all the elements of both the sets
print(s1.intersection(s2)) # {4, 5} # intersection of two sets will give a new set which will contain only the common elements of both the sets
                  

#take input from user of 8 numbers and show the unique one only 

numbers = set() 
n1 = input("enter a number: ")
numbers.add(n1)
n2 = input("enter a number: ")
numbers.add(n2)
n3 = input("enter a number: ")
numbers.add(n3)
n4 = input("enter a number: ")
numbers.add(n4)
print(numbers)