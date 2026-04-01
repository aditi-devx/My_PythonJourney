friends =  [ "Priyanka " , "Vishu" , "pratik" , "ravi" , "astha"]
print(friends[0]) # indexing lists
friends[0] =  "lovely"
print(friends[0])   
print(friends [0:3]) # slicing lists
#  unlike strings lists are mutable which means we can change the value of an element in a list but we cannot change the value of a character in a string




#METHODS OF LISTS 

friends =  [ "Priyanka " , "Vishu" , "pratik" , "ravi" , "astha"]
friends.append("adi")
print(friends) # append() is used to add an element at the end of a list

#method 2 i.e SORT()

list1 = [ 5 , 2 , 9 , 1 , 3]
#list1.sort()  # sort() is used to sort the elements of a list in ascending order
#list1.reverse()
list1.insert(3,34) #insert() is used to insert an element at a specific index in a list
print(list1) 