# for x in range(1,21):
#     if(x%3==0):
#         print(f"{x}--fizz")
#     elif(x%5==0):
#         print(f"{x}--buzz")    
#     elif(x%3==0 and  x%5==0):
#         print(f"{x}--fizzbuzz")


#check it is armstrong number or not

# n=153
# num=n
# sum1=0
# while n>0:
#     ld=n%10
#     sum1+=ld**3
#     n=n//10
# print(sum1)
# if sum1==num:
#     print("armstrong")
# else:
#     print("not")     

# def movie_ticket(amount):
#     if amount > 2000:
#         return "Gift: Coke + Popcorn"
#     elif amount > 1500:
#         return "Gift: Coke"
#     else:
#         return "Thank you!"
# # print(movie_ticket(1000))
# print(movie_ticket(2500))

# yr=int(input("enter a year: "))
# if ((yr % 400==0) or (yr % 4 ==0 and yr % 100 !=0)):
#     print("it is leap year")
# else:
#     print("it is not leap year")


# num=int(input("enter a number: "))
# if num<=100:
#     bill=num*2
# print("first bill") 
# elif num<=200:
#     bill=num*2 + num*3
# print("second bill")
# elif num>200:
#     bill=num*2 + num*3 + num*5    
# print("above bill")
# else:
#     print("invalid stmts")   

# ecommerce_data = [
#     {
#         "order_id": "O1001",
#         "customer_name": "Ravi Kumar",
#         "city": "Hyderabad",
#         "product": "Wireless Mouse",
#         "category": "Electronics",
#         "price": 799,
#         "quantity": 2,
#         "total_amount": 1598,
#         "payment_method": "UPI",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1002",
#         "customer_name": "Sneha Reddy",
#         "city": "Bangalore",
#         "product": "Bluetooth Headphones",
#         "category": "Electronics",
#         "price": 1999,
#         "quantity": 1,
#         "total_amount": 1999,
#         "payment_method": "Credit Card",
#         "order_status": "Shipped"
#     },
#     {
#         "order_id": "O1003",
#         "customer_name": "Arjun Singh",
#         "city": "Mumbai",
#         "product": "Running Shoes",
#         "category": "Fashion",
#         "price": 2499,
#         "quantity": 1,
#         "total_amount": 2499,
#         "payment_method": "Cash on Delivery",
#         "order_status": "Processing"
#     },
#     {
#         "order_id": "O1004",
#         "customer_name": "Priya Sharma",
#         "city": "Delhi",
#         "product": "Smart Watch",
#         "category": "Electronics",
#         "price": 3499,
#         "quantity": 1,
#         "total_amount": 3499,
#         "payment_method": "Debit Card",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1005",
#         "customer_name": "Kiran Patel",
#         "city": "Chennai",
#         "product": "Laptop Backpack",
#         "category": "Accessories",
#         "price": 1299,
#         "quantity": 3,
#         "total_amount": 3897,
#         "payment_method": "UPI",
#         "order_status": "Shipped"
#     }
# ]

# for i in ecommerce_data:
#     if i["payment_method"] == "UPI":
#         print(i["customer_name"])
# for i in ecommerce_data:
#     if i["quantity"]>1:
#         print(i["customer_name"])  
# for i in ecommerce_data:
#     if i["category"]!="electronics":
#         print(i["customer_name"])              

ratings=[5.0,4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,1.9]
for i in ratings:
    if i>=4.5:
        print("best")
    elif i>=3:
        print("average")
    else:
        print("poor")        