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

list1.pop(3)
print(list1) # pop() is used to remove an element from a list at a specific index and return the removed element

#PRACTICE SET 


#wap to enter 5 fruits name in a list enterd by user 

fruits = []
inputf1 = input("enter first fruit name:") 
fruits.append(inputf1)
inputf2 = input("enter second fruit name:")
fruits.append(inputf2)
inputf3 = input("enter third fruit name:")
fruits.append(inputf3)
inputf4 = input("enter fourth fruit name:")
fruits.append(inputf4)
inputf5 = input("enter fifth fruit name:")
fruits.append(inputf5)
print(fruits)


marks = []
student1 = int(input("enter marks:"))
marks.append(student1)
student2 = int(input("enter marks:"))
marks.append(student2)
student3 = int(input("enter marks:"))
marks.append(student3)
student4 = int(input("enter marks:"))
marks.append(student4)

marks.sort()
print(marks)


#wap to sum 4 elements in a list
list2= [ 5 , 6 , 7 , 8]
print(sum(list2))
