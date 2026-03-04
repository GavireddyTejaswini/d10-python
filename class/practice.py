#a=10
#b=10
#print(a)
#print(id(a))
#print(id(b))
#a=10
#b=25
#c=30
#print(id(b))
#print(id(c))
#x="hello world"
#print(x)
#print(id(x))
#y="hi"
#print(id(y))
#x,y,z="teju","haseena","srujana"
#print(x)
#print(z)
#ip1=10
#ip2=120.34
#ip3="hello"
#print(type(ip2))
#print(type(type(ip1)))
#print(type(print("hello")))
#print(type(id(ip3)))
#x="hello"
#print(type(id(x)))
#x=123
#y=id(x)
#print(y)

#name=input("enter name: ")
#city=input("enter city name: ")
#institute=input("enter institute name: ")
#print(f"i am {name},came to {city} and joined in{institute}")

#z=3+5j
#print(id(z))
#print(type(z))

#str1="data science"
#print(str1)
#print(type(str1))
#print(len(str1))
#print(str1[5])
#print(str1[-5])

#list=[1,2,"hello",12.5,"hi",78,"hey",[15,"teju",5.0,9]]
#print(list)
#print(len(list))
#print(type(list[3]))
#print(list[-3])
#print(list)
#print(list[-1][-2])
#print(list[4][1])
#print(list)
#print(list[-3])
#print(list[-1][-3])#
#print(list[-1][-3][2])

#list=[1,2,"hello",12.5,"hi",78,"hey",[15,"teju",5.0,9]]
#list[2]="welcome"
#print(list)
#del list[7]
#print(list)

#tup=(1,2.5,"hello",5,26,"hey")
#print(tup)
#print(len(tup))
#print(tup)

#list1=[1,2,3]
#tup1=(1,2,3,4,5,6,8.9,"hello")
#print(list1.__sizeof__())
#print(tup1.__sizeof__())


#set={1,2,"hello",12.4,"hi",58}
#print(set)
#print(set)
#print(hash("hello"))


# apple_info={
#             "name":"apple",
#             "colour":"red",
#             "quality":"good",
#             "price":75
#             }
# print(apple_info)
# print(apple_info["price"])
# print(apple_info["quality"])
# apple_info["origin"]="shimla"




# a=123
# a/=3
# print(a)

# print(6>>3)
# print(5>>3)

# num=int(input("enter a number: "))
# op='positive' if num>0 else 'negative'
# print(op)

# num=int(input("enter a number: "))
# # if num%2==0:
# #     print("even")
# # else:
# #     print("odd")    
# op='even' if num & 1==0 else 'odd'
# print(op)

# print('stmt1')
# print('stmt2')
# if True:
#     print('stmt3')

# frontend=True
# backend=False
# db=True
# if frontend and backend and db:
#     print('become a fsd')
# elif frontend and backend:
#     print('become frontend and backend') 
# elif frontend and db:
#     print('become frontend and backend')
# elif frontend:
#     print('frontend')
# elif backend:
#     print('backend')
# elif db:
#     print('become db')
# else:
#     print('join 10000 coders')                       

# are_frnd=True
# account=True
# if are_frnd:
#     print("msg to each other")
#     if account:
#         print("piblic send msg")
#     else:
#         print("not send a msg")    
# else:
#     print("they beacome frnds")    

# list1=['hi','hello','heyy','byee']
# for x in list1:
#     print(x[0])

# dict1={'name':'teju','city':'hyd','age':20}
# for x in dict1:
#     #print(x)
#     # print(dict1[x])
#     print(f"{x} : {dict1[x]}")


# names1={'name':'yash','city':'hyd','gender':'male','age':21}
# for i in names1:
#    # print(i)
#     # print(names1[i])
#     print(f"{i} : {names1[i]}")

# for i in range(1,11):
#     print(i)

# for i in range(20,31):
#     print(i)
# --->total count of even number
# count=0
# for i in range(1,21):
#     if i%2==0:
#         count+=1
# print("total even count:", count)

#  ---> sum of odd numbers  
    
# sum=0
# for i in range(1,21):
#     if i%2!=0:
#         sum+=i
# print("sum of odd numbers:",sum)   

# ---->factorial of given number

# num=5
# fact=1
# for i in range(1,6):
#     fact=fact*i
# print("factorial of given number:",fact)    

#--->print 1 to 10
#for i in range(1,11):
#     print(i)
 #---->even numbers
# for i in range(1,21):
#     if i%2==0:
#         print("even:",i)
#--->print reverse 10   to 1
# for i in range(10,0,-1):
#     print(i)

#---->print square numbers of 1 to 5
# for i in range(1,6):
#     squ=i*i
#     print(squ)
        
# --->Print multiplication tables from 1 to 5, each from 1 to 10
# for num in range(1,6):
#     print(num)
#     for i in range(1,11):
#         print(f"{num} x {i}={num*i}")
#         i+=1
#     print()

# plan=30
# current_day=1
# while current_day<=plan:
#     print(" watch netflix")
#     current_day+=1

# str1='tejaswini'
# x=0
# while x<len(str1):
#     print(str1[x])
#     x+=1

# str1='tejaswini'
# x=0
# while x<len(str1):
#     if str1[x] in 'aeiou':
#          print(str1[x])
#     x+=1

# num=123547
# str1=str(num)
# x=0
# while x<=len(str1)-1:
#     print(len(str1[x]))
#     x+=1

# num=123
# rev=0
# while num>0:
#     ld=num%10
#     rev=rev*10+ld
#     num=num//10
# print(rev)    

# num=9070
# rev=0
# while num>0:
#     ld=num%10
#     rev=rev*10+ld
#     num=num//10
# print(rev)    

# ---->Positive, Negative or Zero
# num=int(input("enter a number: "))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")
    

# --->even or odd
# num=int(input("enter a number:"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# --->Take two numbersPrint which number is greaterIf both are equal, print "Both numbers are equal"
# x=int(input("enter a number 1: "))
# y=int(input("enter a number2: "))
# if x>y:
#     print("x is greater")
# elif y>x:
#     print("y is greater")
# elif x==y:
#     print("both equal")
# else:
#     print("invalid")

# --->Take:

# Account balance,Withdrawal amount
# Conditions:If withdrawal > balance → Print "Insufficient Balance" Else → Print "Transaction Successful

# account_balance=int(input("enter a account_balance: "))
# withdrawl_amount=int(input("enter a withdrawl_amount: "))
# if withdrawl_amount>account_balance:
#     print("not inefficient")
# else:
#     print("transaction sucess")
    
# --->alphabet,digit,specialcharcater to check

# num=(input("enter a character:"))
# if num.isalpha():
#     print("alphabet")
# elif num.isdigit():
#     print("digit")
# else:
#     print("special character")

# --->Takes marks from the user,Prints grade based on marks:
# 90 to 100 → Grade A,75 to 89 → Grade B,50 to 74 → Grade C,Below 50 → Fail

# If marks < 0 or > 100 → Print "Invalid Marks"
# num=int(input("enter a marks: "))
# if num<0 or num>100:
#     print("invalid marks")
# elif num>=90 and num<=100:
#      print("grade A")
# elif num>=75 and num<=89:
#     print("grade B")
# elif num>=50 and num<=74:
#     print("grade c")
# else:
#     print ("fail")
    
# ---->find vowels given string using for loop
# name='tejaswini'
# vowels='aeiou'
# for i in name:
#     if i in vowels:
#         print(i)    

# ---->find constants given string using for loop

# name='tejaswini'
# vowels='aeiou'
# for i in name:
#     if i not in vowels:
#         print(i)    

# num=739
# large=0
# while(num>0):
#     digit=num%10
#     if digit>large:
#         large=digit
#         num=num//10
#         print(large)


# num = 53829
# largest = 0
# while num > 0:
#     digit = num % 10
#     if digit > largest:
#         largest = digit
#     num = num // 10
# print("Largest digit =", largest)


# --->multiple of list given output is 0,5,14,24,8,20,36,70
# nums=[3,5,7,8,2,4,6,10]
# multi=0
# for i in nums:
#     print(i*multi)
#     multi+=1

# --->given output is so om om....
# str1='something is fishy'
# x=1
# for i in str1:
#     print(i,str1[x])
#     x+=1

# -->given output eachh character to print hello
# str1="data"
# for i in str1:
#     print(f"{i}-hello")

# --->square of list of numbers
# list1=[1,4,5,6,7,9,3,2,8,1]
# for i in list1:
#     print(f" square of {i} is {i**2}")

# --->given list we find out the length of each string
# list1=['teju','dinesh','prasanth','bunty']
# for i in list1:
#     print(f"length of {i} is {len(i)}")

# -->we find out the lenghth of list and to find it is odd or even
# names1=['teju','dinesh','prasanth','bunty']
# for i in names1:
#     if len(i)%2==0:
#         print(f"{i}---even")
#     else:
#         print(f"{i}---odd")    

# --->given list and multiply
# list1=[1,2,3,4,6,9,8]
# x=0
# for i in list1:
#     print(i*x)
#     x+=1

# # --->reverse number
# num=int(input("enter a number: "))
# rev=0
# while(num>0):
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)   

# ----->palindrome or not
# num=int(input("enter number: "))
# original=num
# rev=0
# while(num>0):
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)
# if rev==original:
#     print("palindrome")
# else:
#     print("not")        

str1="tejaswini"
dict1={}
for char in str1:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1    
print(dict1)        