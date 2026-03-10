#create sets
set1= {1,2,3,4,5}
set2= {4,5,6,7,8}

#Access set elements (iterate through set)
print("Set 1 elements")
for element in set1:
    print(element, end=" ")
    print("\nset2 elements:")
for element in set2:
    print(element,end="")
    print()

#Union of sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

#intersection of sets
intersection_set= set1.intersection(set2)
print("Intersection of set1 and set2:",intersection_set)

#Difference of sets(Set1-Set2)
difference_set= set1.difference(set2)
print("Differnce(Set1-Set2):",difference_set)

#Difference of sets(Set2-Set1)
difference_set2= set2.difference(set1)
print("Difference(Set2-Set1):",difference_set2)