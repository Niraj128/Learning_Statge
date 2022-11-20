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

#Convert all strings into upper case in given list

list_b = ['hi', 'hello', 'bye','nice']

result = [x.upper() for x in list_b ]
print(result)

#Put all negative numbers after positive numbers from given list

lst = [1,-1,2,-5,9,-10]

result1 = [x for x in lst if x > 0 ]
result2 = [x for x in lst if x < 0 ]

result = result1 + result2
print(result)
