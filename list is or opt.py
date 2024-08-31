# Is OR  ISnOt Identity operators
# a= [1,2,3]
# b=a
# print(a is b )
# c= b
# print (c is  b)


# freinds = [ "Wasif ","Kashif ","Zain "]
# lenght = "123456789"
#ZIP function is used to added to list together
# name = ["Wasif ", "zain ","Ali"]
# age = [19,21,18]
# place =["ISl","Taxila","PMO"]
# for name,age,place in zip(name,age,place):
#     print(f"Hi My name is {name} and age is {age} from {place}")

# values=[
#     [1,2,3],
#     [11,22,33],
#     [7,8,9]


# ]
# for value in values:
#     for sub_value in value:
#         print(f"Inner Loop {sub_value}")
#     print(f"Outer Loop {value}")
# print("Loop finished")


# for a in range(2,10):
#     for b in range(1,11):
#         if((a ==5) and (b <6)):
#             print(f"{a}*{b} = {a*b}")
#     print()

#while loop---------
# condition = ""
# while condition !="exit":
#     user_in= input("Enter the cmd :")
#     if user_in != "exit":
#         print(user_in)
#     elif user_in == "exit":
#         condition = user_in

number = [ 2,4,5]

# for i in number:
#     print(i*i)
#--------------------------------333#

#list comprehension

# square = [ number+2 for number in number]
# print(square)

# for i in range(1,11):
#     if i%2==0:
#         print(i**2)

# square using list comprehension 
square = [i**2 for i in range(1,11) if i%2==0]
print(square)
