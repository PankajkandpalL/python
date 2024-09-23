# # # # # # # # # # # # If the given sides form a valid triangle.

# # # # # # # # # # # side1 = int(input("Enter side 1 : "))
# # # # # # # # # # # side2 = int(input("Enter side 2 : "))
# # # # # # # # # # # side3 = int(input("Enter side 3 : "))

# # # # # # # # # # # if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2 :
# # # # # # # # # # #     print("Forms a valid triangle")
# # # # # # # # # # # else :
# # # # # # # # # # #     print("Not a valid triangle")
    
# # # # # # # # # # # # Loops

# # # # # # # # # # # print(0)
# # # # # # # # # # # print(1)
# # # # # # # # # # # print(2)
# # # # # # # # # # # print(3)
# # # # # # # # # # # print(4)
# # # # # # # # # # # print(5)
# # # # # # # # # # # print(6)
# # # # # # # # # # # print(7)


# # # # # # # # # # # mylist = [1,2,3,4,5]
# # # # # # # # # # # print(mylist[0])
# # # # # # # # # # # print(mylist[1])
# # # # # # # # # # # print(mylist[2])
# # # # # # # # # # # print(mylist[3])
# # # # # # # # # # # print(mylist[4])

# # # # # # # # # # # Print numbers from 1-10.

# # # # # # # # # # # num -> variable
# # # # # # # # # # # range -> shows the limit
# # # # # # # # # # # range(0,11,2) -> 
# # # # # # # # # # #           0 is the starting point
# # # # # # # # # # #           11 is the ending point
# # # # # # # # # # #           2 is the postcondition, incre/decre

# # # # # # # # # # # for num in range(10,21,1):
# # # # # # # # # # #     print(num)
    
# # # # # # # # # # # Print all the number from 1-20 using for loop.

# # # # # # # # # # # for num in range(1,21,1):
# # # # # # # # # # #     print(num)
    
# # # # # # # # # # # Print all the number from 1-100 with a difference of 5
# # # # # # # # # # # . 0->5->10->15......100

# # # # # # # # # # # for num in range(0,101,5):
# # # # # # # # # # #     print(num)
    
# # # # # # # # # # # Print all the even numbers between 1-10

# # # # # # # # # # # for num in range(1,11,1):
# # # # # # # # # # #     if num % 2 == 0:
# # # # # # # # # # #         print(num)


# # # # # # # # # # # for num in range(1,100): 
# # # # # # # # # # #     if num % 7==0 and num % 3 == 0:
# # # # # # # # # # #         print(num)
        
# # # # # # # # # # # You need to print first 10 natural numbers

# # # # # # # # # # # num = 1

# # # # # # # # # # # while num <= 10:
# # # # # # # # # # #     print(num)
# # # # # # # # # # #     num = num + 1
    
# # # # # # # # # # # Print the even numbers between 1-10 using while loop.

# # # # # # # # # # num = 0

# # # # # # # # # # while num <= 10:
# # # # # # # # # #     if num % 2 == 0:
# # # # # # # # # #         print(num)
# # # # # # # # # #     num = num + 1
    
# # # # # # # # # # # Print all the numbers divisible by 5 between 1-100
# # # # # # # # # # # using while loop.


# # # # # # # # # # # Print the table of 2.


# # # # # # # # # # tableOf = 2

# # # # # # # # # # # for num in range(1,11):
# # # # # # # # # # #     table = num * tableOf
# # # # # # # # # # #     print(table)
    
# # # # # # # # # # num = 1
# # # # # # # # # # while num <= 10 :
# # # # # # # # # #     table = num * tableOf
# # # # # # # # # #     print(table)
# # # # # # # # # #     num = num + 1
    
    
# # # # # # # # # # # Print the square of first 10 natural numbers.

# # # # # # # # # # num = 1

# # # # # # # # # # while num <= 10:
# # # # # # # # # #     square = num*num
# # # # # # # # # #     square2 = num**2 
# # # # # # # # # #     print(square, square2)
# # # # # # # # # #     num = num + 1
    
    
# # # # # # # # # # for num in range(1,11):
# # # # # # # # # #     square = num*num
# # # # # # # # # #     square2 = num**2 
# # # # # # # # # #     print(square, square2)


# # # # # # # # # # Print the sum of first 10 natural numbers.

# # # # # # # # # #  1+2+3+4+5+6+7+8+9+10

# # # # # # # # # #  print(1+2+3+4+5+6+7+8+9+10)
# # # # # # # # # # 1+2 = "3" + 3 = "6" + 4 = "10" + 5 = "15"


# # # # # # # # # # for num in range(1,11):
# # # # # # # # # #     sum = sum + num
# # # # # # # # # #     print(sum)
    
# # # # # # # # # sum = 0
# # # # # # # # # num = 1
# # # # # # # # # while num <= 10:
# # # # # # # # #     sum = sum + num
# # # # # # # # #     print(sum)
# # # # # # # # #     num = num + 1


# # # # # # # # # # Print the count of all the even &
# # # # # # # # # # odd numbers betweeen 1-100.

# # # # # # # # # #  1-100 -> count even and odd numbers


# # # # # # # # # countOfEven = 0
# # # # # # # # # countOfOdd = 0

# # # # # # # # # for num in range(1,101):
# # # # # # # # #     if num % 2 == 0:
# # # # # # # # #         countOfEven = countOfEven + 1
# # # # # # # # #     else:
# # # # # # # # #         countOfOdd = countOfOdd + 1
        
# # # # # # # # # print("Count of Even", countOfEven, "Count of Odd", countOfOdd)




# # # # # # # # # Print the factorial of 5.

# # # # # # # # # 5 * 4 * 3 * 2 * 1

# # # # # # # # #  Value decrement
# # # # # # # # #  multiply
# # # # # # # # #  endPoint -> 1

# # # # # # # # # num = 5
# # # # # # # # # factorial = 1

# # # # # # # # # while num>=1:
# # # # # # # # #     factorial = num * factorial
# # # # # # # # #     num = num - 1
    
# # # # # # # # # print(factorial)


# # # # # # # # # Print the first four numbers divisible by 4.


# # # # # # # # # 1 
# # # # # # # # # 2 
# # # # # # # # # 3 
# # # # # # # # # 4 -> count - 1
# # # # # # # # # 5
# # # # # # # # # 6
# # # # # # # # # 7
# # # # # # # # # 8 -> count - 2
# # # # # # # # # 9  
# # # # # # # # # 10 
# # # # # # # # # 11 
# # # # # # # # # 12 -> count - 3
# # # # # # # # # 13
# # # # # # # # # 14
# # # # # # # # # 15 
# # # # # # # # # 16 -> count - 4


    
# # # # # # # # # count = 0
# # # # # # # # # num = 1

# # # # # # # # # while count < 4:
# # # # # # # # #     if num % 4 == 0:
# # # # # # # # #         count = count + 1
# # # # # # # # #         print(num)
# # # # # # # # #     num = num + 1

# # # # # # # # # # Break

# # # # # # # # # for i in range(1,10):
# # # # # # # # #     if i == 5:
# # # # # # # # #         break
# # # # # # # # #     print(i)
    
# # # # # # # # # Break the loop at the point you 
# # # # # # # # # get the number divisible by 9 
# # # # # # # # # between 50-100


# # # # # # # # # for i in range(50,100):
# # # # # # # # #     if i%9==0:
# # # # # # # # #         break
# # # # # # # # #     print(i)


# # # # # # # # # Continue

# # # # # # # # # for i in range(50,100):
# # # # # # # # #     if i%9==0:
# # # # # # # # #         continue
# # # # # # # # #     print(i)




# # # # # # # # # PRINT NUMBERS BUT SKIP ALL THE NUMBERS
# # # # # # # # # DIVISIBLE BY 3 BETWEEN 1-100.


# # # # # # # # # for num in range(1,101):
# # # # # # # # #     if num % 3 == 0:
# # # # # # # # #         continue
# # # # # # # # #     print(num)


# # # # # # # # # num = 1
# # # # # # # # # while num <= 100 :
# # # # # # # # #     if num % 3 == 0:
# # # # # # # # #         num = num + 1
# # # # # # # # #         continue
# # # # # # # # #     print(num)
# # # # # # # # #     num = num + 1


# # # # # # # # # for else

# # # # # # # # for num in range(1,10):
# # # # # # # #     if num % 3 == 0:
# # # # # # # #         continue
# # # # # # # #     print(num)
# # # # # # # # else:
# # # # # # # #     print("Task completed!")
    
    
# # # # # # # # # Guess the number -> 
# # # # # # # # # Ask the user to guess the number between 1- -> input
# # # # # # # # # If the guess is wrong, provide hint to the user.
# # # # # # # # # If the number is less than the correct number, say
# # # # # # # # # something like "number is less", if the guess is greater
# # # # # # # # # than the actual number say, "number is greater".
# # # # # # # # # Program should run till user guess the correct number.


# # # # # # # # # correct_number = 4
# # # # # # # # # while True:
# # # # # # # # #     # Need to take the input 
# # # # # # # # #     num = int(input("Enter the number between 1-10"))
# # # # # # # # #     # the number is less than the correct number 
# # # # # # # # #     # "number is less"
# # # # # # # # #     if num < correct_number:
# # # # # # # # #         print("Number is smaller")
# # # # # # # # #     # if the guess is greater
# # # # # # # # #     # than the actual number say, "number is greater".
# # # # # # # # #     elif num > correct_number:
# # # # # # # # #         print("Number is greater")
# # # # # # # # #     else:
# # # # # # # # #         print("Correct guess")
# # # # # # # # #         break
    
# # # # # # # # # NESTED LOOPS


# # # # # # # # for people in range(1,5):
# # # # # # # #     for golgappas in range(1,6):
# # # # # # # #         print(people, "having golgappa", golgappas)
        
        
# # # # # # # # # Print the time in mins and seconds.
# # # # # # # # # 1 min 1 sec
# # # # # # # # # 1 min 2 sec
# # # # # # # # # 1 min 3 sec
# # # # # # # # # 1 min 4 sec
# # # # # # # # # ......
# # # # # # # # # 60 min 60 sec

# # # # # # # # #  min sec
# # # # # # # # #  mins sec
# # # # # # # # #  min secs
# # # # # # # # #  mins secs

# # # # # # # # # for mins in range(1,61):
# # # # # # # # #     for secs in range(1,61):
# # # # # # # # #         if min == 1 and secs == 1:
# # # # # # # # #             print(mins, "min", secs,"sec")
# # # # # # # # #         elif min!=1 and secs == 1:
# # # # # # # # #             print(mins, "mins", secs,"sec")
# # # # # # # # #         elif secs!=1 and min == 1:
# # # # # # # # #             print(mins, "min", secs,"secs")
# # # # # # # # #         else:
# # # # # # # # #             print(mins, "mins", secs,"secs")
            
            
# # # # # # # # # Print this pattern
# # # # # # # # # 1 2 3 4 5
# # # # # # # # # 1 2 3 4 5
# # # # # # # # # 1 2 3 4 5
# # # # # # # # # 1 2 3 4 5
# # # # # # # # # 1 2 3 4 5


# # # # # # # # for line in range(1,6):
# # # # # # # #     for num in range(1,6):
# # # # # # # #         print(num, end=" ")
# # # # # # # #     print()
    
    
    
# # # # # # # # # Print this pattern

# # # # # # # # # 1 
# # # # # # # # # 1 2
# # # # # # # # # 1 2 3
# # # # # # # # # 1 2 3 4
# # # # # # # # # 1 2 3 4 5

# # # # # # # # for lines in range(1,6):
# # # # # # # #     for num in range(1,lines+1):
# # # # # # # #         print(num, end=" ")
# # # # # # # #     print()
    
# # # # # # # # # Print the multiplication table from 1-100.

# # # # # # # # for table in range(1,101):
# # # # # # # #     for num in range(1,11):
# # # # # # # #         print(table * num)
# # # # # # # #     print()


# # # # # # # # # Print this pattern

# # # # # # # # # 1 2 3 4 5
# # # # # # # # # 1 2 3 4
# # # # # # # # # 1 2 3
# # # # # # # # # 1 2
# # # # # # # # # 1 


# # # # # # # # for lines in range(5,0,-1): # 5 4 
# # # # # # # #     for num in range(1, lines+1): # 1, 5
# # # # # # # #         print(num, end=" ") # 1 2 3 4 
# # # # # # # #     print()
    
# # # # # # # # # Print this pattern
# # # # # # # # # * * * *
# # # # # # # # # * * * *
# # # # # # # # # * * * *
# # # # # # # # # * * * *

# # # # # # # # for lines in range(1,5):
# # # # # # # #     for num in range(1,5):
# # # # # # # #         print("*", end=" ")
# # # # # # # #     print()

# # # # # # # # # Print this pattern
# # # # # # # # # * * * *
# # # # # # # # # * * * 
# # # # # # # # # * * 
# # # # # # # # # *     

# # # # # # # # for lines in range(5,0,-1): # 5 4 
# # # # # # # #     for num in range(1, lines+1): # 1, 5
# # # # # # # #         print("*", end=" ") # 1 2 3 4 
# # # # # # # #     print()
    

# # # # # # # # # Write a program to check whether a 
# # # # # # # # # number is prime or not between 1-100.
# # # # # # # # # If its prime print like -
# # # # # # # # # 2 - Number is prime
# # # # # # # # # 3 - Number is prime
# # # # # # # # # 4 - Number is not prime.
# # # # # # # # # 5 - Number is prime.
# # # # # # # # # 6 - Number is not prime.
# # # # # # # # # 7 - Number is prime.
# # # # # # # # # 8 - Number is not prime.



# # # # # # # # Prime Number


# # # # # # # # 5 -> prime number

# # # # # # # # 5 % 1 == 0 
# # # # # # # # 5 % 2 == 0 
# # # # # # # # 5 % 3 == 0 
# # # # # # # # 5 % 4 == 0 
# # # # # # # # 5 % 5 == 0 


# # # # # # # # num % i == 0

# # # # # # # # for num in range(1,101):
# # # # # # # #     factors = 0
# # # # # # # #     for i in range(1,num+1):
# # # # # # # #         if num % i == 0:
# # # # # # # #             factors = factors + 1
# # # # # # # #     if factors == 2:
# # # # # # # #         print(num, "Number is prime")
# # # # # # # #     else:
# # # # # # # #         print(num, "Number is not prime")
    


# # # # # # # # # Print the pattern

# # # # # # # # # ****
# # # # # # # # # *  *
# # # # # # # # # *  *
# # # # # # # # # ****

# # # # # # # stars = 8

# # # # # # # for line in range(1,stars+1):
# # # # # # #     for num in range(1,stars+1):
# # # # # # #         if line == 1 or line == stars or num == 1 or num == stars:
# # # # # # #             print("*", end="")
# # # # # # #         else:
# # # # # # #             print(" ", end="")
# # # # # # #     print()


# # # # # # # # Print this pattern
# # # # # # # # 1
# # # # # # # # 10
# # # # # # # # 101
# # # # # # # # 1010
# # # # # # # # 10101

# # # # # # # totalLines = 10
# # # # # # # for line in range(1,totalLines):
# # # # # # #     for num in range(1,line+1):
# # # # # # #         if num % 2 == 0:
# # # # # # #             print(0, end="")
# # # # # # #         else:
# # # # # # #             print(1, end="")
# # # # # # #     print()


# # # # # # # # Print this pattern


# # # # # # # # 1
# # # # # # # # 12
# # # # # # # # 123
# # # # # # # # 1234
# # # # # # # # 123
# # # # # # # # 12
# # # # # # # # 1


# # # # # # # num = 4
# # # # # # # lines = 7

# # # # # # # num = 3 
# # # # # # # lines = 5

# # # # # # # num = 2
# # # # # # # lines = 3

# # # # # # # # 1
# # # # # # # # 12
# # # # # # # # 123
# # # # # # # # 12
# # # # # # # # 1

# # # # # # # # Print V.
# # # # # # # #  num = 3
# # # # # # # # \    /
# # # # # # # #  \  /
# # # # # # # #   \/



# # # # # # # # 1
# # # # # # # # 12
# # # # # # # # 1





# # # # # # # # # num = 5 - Prime or not
# # # # # # # # # factors - 2 (1,that number itself)
# # # # # # # # # "1" 2 3 4 "5" -> range(1,num+1) 



# # # # # # # # Iterators



# # # # # # # my_string = "hello"
# # # # # # # print(my_string)
# # # # # # # iter_string = iter(my_string)

# # # # # # # print(next(iter_string))
# # # # # # # print(next(iter_string))
# # # # # # # print(next(iter_string))
# # # # # # # print(next(iter_string))
# # # # # # # print(next(iter_string))
# # # # # # # print(next(iter_string))

# # # # # # # my_string = "hello"

# # # # # # # for char in my_string:
# # # # # # #     print(char)
    

# # # # # # # Print hello in the single line.

# # # # # # my_string = "hello"
# # # # # # a = ""

# # # # # # for char in my_string: # o
# # # # # #     a=a+char # a = "hell" + "o"
    
# # # # # # print(a)

# # # # # # # # # Create a list and use for loop to iterate 
# # # # # # # # # over it.

# # # # # # my_list = [1,3,4,5,6]

# # # # # # for el in my_list:
# # # # # #     print(el)
    
# # # # # # # Reverse a string.

# # # # # # for char in reversed(my_string):
# # # # # #     print(char)

# # # # # # for char in my_string[::-1]:
# # # # # #     print(char)


# # # # # # # Reverse the string and print it 
# # # # # # # in the single line.


# # # # # # # Check if a string is palindrome or not.

# # # # # # # Reverse the string
# # # # # # # Compare reversed and original string

# # # # # # my_string = "heelo"
# # # # # # a = ""

# # # # # # for char in my_string[::-1]:
# # # # # #     a = a+char


# # # # # # if a == my_string:
# # # # # #     print("Palindrome")
# # # # # # else:
# # # # # #     print("Not palindrome")



# # # # # # # # Your task is to find if the string 420 is present
# # # # # # # # in it or not.

# # # # # # # # Print "Caught" if 420 is present in it.
# # # # # # # # Otherwise "Escaped" if 420 is not present in it.

# # # # # # for ex - masai420 -> Caught
# # # # # # for ex - masai8330 -> Escaped
# # # # # # for ex - ma4sw20ai -> Escaped


# # # # # jstring = "hello"


# # # # # if "8" in jstring:
# # # # #     print("Caught")
# # # # # else:
# # # # #     print("Escaped")
    
    
# # # # # # List

# # # # # # Create a list and print all the elements using for loop.

# # # # # mylist = [1,3,3,5,4]

# # # # # # for el in mylist:
# # # # # #     print(el)  
    
# # # # # # mylist = [1,3,3,5,4] -> 1+3 - 4 
# # # # # # Print the total sum.

# # # # # sum = 0
# # # # # for el in mylist:
# # # # #     sum = sum + el
    
# # # # # print(sum)

# # # # # mylist = [1,3,3,5,4] 
# # # # # # Find the average of the list.

# # # # # sum = 0
# # # # # count = 0

# # # # # for el in mylist:
# # # # #     sum = sum + el
# # # # #     count = count + 1
    
# # # # # print(sum/count)


# # # # list = ["apple", "pineapple", "orange"]

# # # # # # Modify elements:
# # # # # # Change the second element of the fruits list to "mango".

# # # # list[1] = "mango"
# # # # print(list)
# # # # # # Add elements:
# # # # # # Add "kiwi" to the end of the fruits list.
# # # # list.append("kiwi")
# # # # print(list)

# # # # # # Insert "7" at the beginning of the list.
# # # # list.insert(0,7)
# # # # print(list)

# # # # # # Remove elements:
# # # # # # Remove the last element from the fruits list.

# # # # list.pop()
# # # # print(list)


# # # # # my_list = [4,3,1,7,8,6,8]

# # # # # Find the sum of all the numbers at the 
# # # # # even indices.

# # # # sum = 0
# # # # mylist = [4,3,1,7,8,6,8]

# # # # for el in mylist:
# # # #     sum = sum + el
    
    
# # # # print(len(mylist))
# # # # print(sum/count)


# # # # # my_list = [4,3,1,7,8,6,8]
# # # #              0,1,2,3,4,5,6
# # # # # Find the sum of all the numbers at the 
# # # # # even indices.

# # # # indices

# # # # mylist = [4,3,1,7,8,6,8]
# # # # sum = 0
# # # # for indexes in range(len(mylist)):
# # # #     if indexes % 2 == 0:
# # # #        sum = sum + mylist[indexes]
       
# # # # print(sum)     


# # # # mylist = [4,3,1,7,3,6,8]
# # # # Replace all the occurences of 
# # # # elements at even indices to 0
# # # # and even elements to "*" in the list.


# # # # mylist = [4,3,1,7,8,6,8]

# # # # for indexes in range(len(mylist)): 
# # # #     if indexes % 2 == 0: 
# # # #         mylist[indexes] = 0  
# # # #     elif mylist[indexes]%2 == 0: 
# # # #         mylist[indexes] = "*"
        
# # # # print(mylist)


# # # # mylist = [4,3,1,7,3,6,8]

# # # # Replace all the occurences of 
# # # # odd elements  to "odd"
# # # # and even elements to "even" in the list.


# # # # mylist = [4,3,1,7,8,6,8]

# # # # for indexes in range(len(mylist)): 
# # # #     if mylist[indexes] % 2 == 0: 
# # # #         mylist[indexes] = "even"  
# # # #     elif mylist[indexes]%2 != 0: 
# # # #         mylist[indexes] = "odd"
        
# # # # print(mylist)


# # # # Print the numbers from 2nd index up to 5th index

# # # # mylist = [4,3,1,7,8,6,8]

# # # # print(mylist[2:5])

# # # # https://github.com/PankajkandpalL/python



# # # # 
# # # # Now you need to compare if these two 
# # # # lists are same or not.


# # # # if x==y:
# # # #     print("Y")
# # # # else:
# # # #     print("N")
    
# # # # Identity Operators

# # # # is, is not

# # # x = [1,3,4] 
# # # y = [1,3,4] 
# # # z = x

# # # if x is y:
# # #     print("Y")
# # # else:
# # #     print("N")

# # # if x is z:
# # #     print("Y")
# # # else:
# # #     print("N")
    
# mylist = [11,3,4,55,4,7]
# maximum = max(mylist)
# print(maximum)

# # # Find the maximum number in the list.
# # max = mylist[0] # 55

# # for el in mylist: # 7
# #     if el > max: # 7 > 55
# #         max = el
        
# # print(max)


# x = True
# y = False

# if not x or not y and x and y:
#     print("Yes")
# else:
#     print("No")
    
# # Modules

# # Write a program which will generate 
# # random numbers everytime between 1-10.

# Step 1 - import Module Name

import math
import random

# dir -> you can check what are the available fns
# present in a module.

print(dir(random))

# sqrtSixteen = math.sqrt(17)
# print(sqrtSixteen)

# Random int
randomi = random.randint(1,10)
print(randomi)