# tup = (85,83,86,89)
# print(tup)
# print(type(tup)) #type

# print(tup[1]) #indexing
# print(tup[2])

# print(len(tup)) #length



#****************empty tuple*****************


# tup = ()
# print(tup)
# print(type(tup))

# tup = (1,)
# print(tup)
# print(type(tup))

# tup = (1)
# print(tup)
# print(type(tup))


#**************slicing in tuple****************


# tup = (85,83,86,89)
# print(tup[1:3])


#methods in tuple*******************


#index method**********************

# tup = (85,83,86,89)
# print(tup.index(85))


#count***********************

# tup = (85,83,86,89)
# print(tup.count(85)) # tells that howmany times that a element present in the tuple



#**************practice question1*******************


# movies = []
# mov1 = input("enter 1st movie :")
# mov2 = input("enter 2nd movie :")
# mov3 = input("enter 3rd movie :")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)


#**************or******************


# movies = []
# movies.append(input("enter 1st movie :"))
# movies.append(input("enter 2nd movie :"))
# movies.append(input("enter 3rd movie :"))

# print(movies)



#***************practicequestion 2********************



# list1 =[1,2,1]
# list2 = [1,2,3]

# copy_list1 = list1.copy()
# copy_list1.reverse

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")


#********************extra*******************



# list1 = [1,2,3,4]
# list2 = [1,2,3,2,1]

# new_list = list1.copy()
# new_list.reverse()

# if(list1 == new_list):
#     print("palindrome")
# else:
#     print("not palindrome")



#******************practice question***************


# grade = ("A" , "C" , "D" ,"A" ,"A" , "B")
# print(grade.count("A"))



#******************************practice qus 4***************




grade = ["A" , "C" , "D" ,"A" ,"A" , "B","B"]
grade.sort()
print(grade)