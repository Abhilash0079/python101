################################### Find the largest number in the list ################################################
""" Run any program after 
commenting all the others program
"""


list1 = []
while(True):
    choice = input("Do you want to add number in list? Press Y for yes and N for No ")
    if choice == 'Y' or choice == 'y':
        x = int(input("Please enter the number "))
        list1.append(x)
    elif choice == 'N' or choice == 'n':
        break
    else:
        print("Please enter the correct input.")

if (len(list1)>0):
    print("Largest number is : ", max(list1))


############################## Find the second largest number in the list ##########################################

list1 = []
while(True):
    choice = input("Do you want to add number in list? Press Y for yes and N for No ")
    if choice == 'Y' or choice == 'y':
        x = int(input("Please enter the number "))
        list1.append(x)
    elif choice == 'N' or choice == 'n':
        break
    else:
        print("Please enter the correct input.")
list1.sort()
if (len(list1)>1):
    print("Second Largest number is : ", list1[-2])
else:
    print("Enter at least two number.")


############################## Merge and sort two  list ##########################################

list1 = [4,5,15,8,6]
list2 = [1,9,7,0]
print(list1)
print(list2)
list3 = list1 + list2
list3.sort()
print(list3)

############################## Swap first and last element in the  list ##########################################

list1 = [4,5,6,7,2,9,0]
list1[0], list1[-1] = list1[-1], list1[0]
print(list1)
