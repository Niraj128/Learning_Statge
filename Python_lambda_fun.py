# How to create lambda functions?

#normal user defined function
def add_five (num):
    result = num + 5
    return result

x = 7
print(add_five(x))


#lambda fuction (same as above)

lambda_add_5 = lambda x : x+5

y = 10
print(lambda_add_5(y))

# 1.write lambda function to add two numbers

lamda_add_two_num = lambda x,y : x+y
a = 9
b = 10
print(lamda_add_two_num(a,b))

#2. Write a lamdsa function of concetanate two input strings

lambda_concetanate = lambda x,y : x +" "+y

a = 'Niraj'
b = 'Kumar'

print(lambda_concetanate(a,b))

#4. calculate max of two numbers

#How to work with map(), reduce() and filter() ???

# Implementing map function
 
list1 = [1,2,3,4,5,6,7,8,9,10]

Square_num = lambda x :x*x
Sqaure_list = list(map (Square_num,list1))
print(Sqaure_list)

# Add sequential respective elements in two given lists

list_a = [1,2,3,4,5]
list_b = [5,4,3,2,1] #-----> reslut required [6,6,6,6,6,]

sum_two_list = lambda x, y : x+y
result = list(map(sum_two_list, list_a,list_b))
print(result)

lambda_max_two_nums =lambda x,y : x if x > y else y

a = 11
b = 7

print(lambda_max_two_nums(a,b))
