# coding= utf-8
list1 = ["12345"]
list2 = ["append","extend","insert","remove","pop","clear","index","count","sort","reverse","copy"]
list1.append("9") # Add an item to the end of the list.
a = list1.extend(list2) # Extend the list by appending all the items in the given list.
print(a)
list3 = ["count","count","count","extend","append",1,2,2,2]
for i in list3 :
    print(i,list3.count(i))
