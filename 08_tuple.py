 #tuple is a immutable datatype in python which is used to store a collection of items. It is similar to a list but it cannot be modified after it is created. Tuples are defined using parentheses () and the items are separated by commas.
a = (12,54, "aditi" , 5.6)
print(type(a)) # <class 'tuple'>


#methods of tuples

#COUNT()
a = (23,55,67,67,89,5,5,)
no_of_times = a.count(5)
print(no_of_times) # count() is used to count the number of times an element appears in a tuple

#INDEX()

index=a.index(5)
print(index) # index() is used to find the index of the first occurrence of an element in a tuple


#wap to count no of zeros in a program in a tuple

tuples = (0, 4, 9 ,0 , 5 ,0)
zero_count = tuples.count(0)

print(zero_count)