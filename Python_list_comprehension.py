#List Comprehension

#Write a program to generate the list of 10 numbers

result = []
for i in range (1, 11):
    result.append(i)
print(result)

#How to do it with list comprehension??

result = [ x for x in range(1, 11)    ]
print(result)

# Get the list of all even numbers between 1 to 50

result =   [ x for x in range (1,51) if x % 2 == 0   ]
print(result)

# Get the list of all even numbers from below list

list_a = [1,2,4,2,6,7,9]

result =   [ x for x in list_a if x % 2 == 0   ]
print(result)
