set1 =set()
print(type(set1))

set2 = {'Monday' : "Hello"}
print(type(set2))

list1 =[1,2,3,4,5,6,7,7,6,5,4,3,2,1,1,2,3]

set3 = list (set(list1))
print(set3)

set6 = set()
set6.add(1)
set6.add(6)
set6.add(9)
set6.add(1)

#print(set6)

# use of update method
lst = [1,2,3,4,5,6,7,7,6,5,4,3,3,4,1]
set6.update(lst)
print(set6)
for num in set6:
    print(num)
