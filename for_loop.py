# # Print the first 10 natural numbers using for loop.
# for i in range(1, 11):
#     print(i)

# Python program to print all the even numbers within the given range.
# for i in range(2, 20, 2):
#     print(i)

# Python program to calculate the sum of all numbers from 1 to a given number.
# num=int(input("Enter a number"))
# sum=0
# for i in range(1, num+1):
#     sum+=i
# print(sum)

# Python program to calculate the sum of all the odd numbers within the given range.
# given_range=int(input("enter a number \n"))
# sum=0
# for i in range(given_range+1):
#     if i%2!=0:
#         sum+=i
# print(sum)    

# Python program to print a multiplication table of a given number
# num=int(input("Enter a number"))

# i=1
# for i in range(1,11):
#     print(num,"*",i, "=", num*i)
#     i+=1

# Python program to display numbers from a list using a for loop
# list=[1,2,3,4,5]
# for i in list:
#     print(i)

# Python program to count the total number of digits in a number.
count=int(input("enter a number"))
count_digit=0
for i in str(count):
    count_digit+=1

print(count_digit)    
