# students = []
# for i in range(2):
#     name : str = input("Enter Your Name: ")
#     regID : int  = int(input("Enter Your ID: "))
#     sub1 : int =  int(input("Enter Math's maks:"))
#     sub2 : int =  int(input("Enter English's maks:"))
#     sub3 : int =  int(input("Enter Urdu's maks: "))
#     print()
#     result = [name, regID, sub1, sub2, sub3]
#     students.append(result)

# for i in range(2):
#     percent = students[i][2] + students[i][3] + students[i][4] * 100 / 300
#     if percent >= 90:
#         grade = "A+"
#     elif percent >= 80 and percent < 90:
#         grade = "A"
#     elif percent >= 70 and percent < 80:
#         grade = "B"
#     elif percent >= 60 and percent < 70:
#         grade = "C"
#     elif percent >= 50 and percent < 60:
#         grade = "D"
#     else :
#         grade = "F"

#     print("\n----------------  Result ------------------------\n")
#     print(f"Student No : {i}")
#     print("\nName : {} ".format(students[i][0]))
#     print("\nRegID : {} ".format(students[i][1]))
#     print("\nSubject 1 : {} ".format(students[i][2]))
#     print("\nSubject 2 : {} ".format(students[i][3]))
#     print("\nSubject 3 : {} ".format(students[i][4]))
#     print("\nGrade : {} ".format(grade))
#     print("\n-------------------------------------------------\n")