#An empty list called my_list
my_list =[]

#adding elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert an element
my_list.insert(1, 15)

#extend my_list with another list
my_list.extend([50, 60, 70])

#remove the last element from my list
my_list.pop(-1)

#sort my_list in an ascending order
my_list.sort()

#find and print the index of an element
index_of_30=my_list.index(30)
print("The index of 30 in my_list is:", index_of_30)




