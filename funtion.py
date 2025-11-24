
# x = int(input("Enter the number: "))
# def Add(n):
#     if n == 1:
#         return 1
#     elif n<1:
#         return "Undefined"
#     else:
#         return n*Add(n-1)
# print("Factorial: ",Add(x))
# def calc(a,b):
#     return a+b 
# sum = calc(1,5)
# print(sum)
# sum = calc(1,9)
# print(sum)
    
# def print_hello():
#     print("hello")



# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()


# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
# calc_avg(98,97,95)

# print("apnacollege")

# heroes=["thor ", "ironman", "spiderman"]
# cities=["delhi","lucknow","noida"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)
# print_list(cities)


# def clac_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# clac_fact(6)

# def converter(usd_val):
#     inr_val =usd_val*83
    
#     print(inr_val)


# converter(9)


# def tell_no(n):
#     if n%2==0:
#         print("even")
#     else :
#         print("ODD")


# tell_no(5)
# tell_no(8)
# tell_no (1305304)

# RECURSION
# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)



# show(5)
# show(7)

# def show (n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)
#     print("END")

# show (8)

#factorial
# def fact(n):
#     if (n==1):
#         return 1
#     return fact(n-1)*n

# print(fact(4))
# sum of natural number
# def sum_natural(n):
#     if n==1:
#         return 1
#     return sum_natural(n-1)+n

# print(sum_natural(89))
          

def print_list(list,idx):
   if (idx ==len(list)):
      return 
   print(list(idx))
   print_list(list,idx+1)

fruits =["mango","banana","apple","orange"]
print_list(fruits,)