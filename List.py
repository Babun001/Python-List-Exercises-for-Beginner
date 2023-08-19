'''# Python program to interchange first and last elements in a list






list1 = [10,20,30,40,50]
temp = list1[0]
list1[0] = list1[len(list1)-1]
list1[len(list1)-1] = temp

print(list1)





# Python program to swap two elements in a list
list2 = [20,50,80]
temp1 = list2[0]
list2[0] = list2[len(list2)-1]
list2[len(list2)-1] = temp1

print(list2)
#same as the privious question




# Python  Swap elements in String list
S_list = ['Babun', 'Pritam', 'Bunny','Thakur']
temp3 = S_list[0]
S_list[0] = S_list[len(S_list)-1]
S_list[len(S_list)-1] = temp3

print(S_list)





# Python | Ways to find length of list
# The essayist question ever

list4 = [12,87,64,96,651,87,65.25, 78, 'Bunny','Babun']
temp4 = len(list4)
print(temp4)





# Maximum of two numbers in Python
First = int(input("Enter First Number :"))
Second = int(input("Enter Second Number :"))

if First > Second:
    print(f"{First} is the Max Number between them..")   
elif First == Second:
    print(f"{First} and {Second} both are same..")
else:
    print(f"{Second} is the Max Number between them..")

# Minimum of two numbers in Python

Third = int(input("Enter First Number :"))
Forth   = int(input("Enter Second Number :"))

if Third > Forth:
    print(f"{Forth} is the Min Number between them..")   
elif Third == Forth:
    print(f"{Forth} and {Third} both are same..")
else:
    print(f"{Third} is the min Number between them..")'''





# Python | Ways to check if element exists in list

'''def FindElement(lst,element):    
    try:
        lst.index(element)
        return True
    except: return False

list17 = [56,78,54,754,6,2,85]  # Initializing a list
element17 = int(input("Enter Element to be searched--->"))  # taking input from user to search element

result17 = FindElement(list17,element17)    #result17 stores the value of FindElement's function

if result17 == True :
    print(f"The Element {element17} is in the list.")
else:

    print(f"The element {element17} is not in the list")
    
# ANOTHER WAY TO SEARCH ELEMENT FROM A LIST

def FindElement2(lst, item):
    for i in lst:
        if (i == item):
            return 1
            
        
        

list18 = [56,78,54,754,6,2,85]
item = int(input("Enter element to be searched-->"))

result18 = FindElement2(list18, item)
if (result18 == 1):
    print(f"The Element {item} is in the array")
else:
    print(f"The Element {item} is not in the array")'''
    
    






# Different ways to clear a list in Python


'''# There are two clear method to clear a list in python
# 1. clear() - method    2. del - keyword

list27 = [56,78,54,754,6,2,85]
print("The Initial list -->", list27)

#using clear method
#   clear method does'not takes any parameter and return nothing
list27.clear()

print("The Final list -->", list27)

print("----------------------------------")

#using del keyword
list28 = [654,984,65,54,3,654,54,]

print("The Initial list -->", list28)

del list28[:]

print("The Final list -->", list28)'''






# Python | Reversing a List

'''list19 = [12,45,78,89,56,23]    #initializing a list
length19 = len(list19)          # length19 stores the length of that list
print("The Initial list -->",list19)

list20 = list19[::-1]   # here i use the slicing method  || [start : end : jump]
                        # [::-1] means jump next index from the end of the list
print(list20)'''









# Python | Count occurrences of an element in a list



'''list25 = [12,45,78,89,56,23,45,89,12,89,89]

# code to find out the occurrence of elements form a list..
def Occurrence(lst,item):
    count25 = 0
    for ele in lst:
        if (ele == item):
            count25 += 1
    return count25

# Taking integer input from the user!  
x = int(input("Enter Number to be searched : "))

#   Drive code
result25 = Occurrence(list25,x)

# The format() method formats the specified value(s) and insert them inside the string's placeholder
print("{} has occured {} time(s) in the list".format(x,result25))'''



# Python Program to find sum and average of List in Python

#Initializing a list
'''list23 = [10,20,30,40,50,60,70,80,90,100,140,100]       
#Function with a lst parameter
def SumOfElement(lst):   
    #let's take a sum variable...                       
    sum=0   

    #for loop to traverce the list   
    for i in lst: 

        # sum variable stores the sum of the elements
        sum += i    # we can also write 'sum = sum + i'
    return sum

#
def AvgOfElement(lst):
    sum = 0
    for i in lst:
        sum += i

    # 'len(lst)' means the number of elements in the list
    avg = sum/(len(lst))
    return avg


list24 = [5,10,15,20,25]

print("The sum of the elements is -->",SumOfElement(list23))
print("The Average of the elements is -->",AvgOfElement(list24))'''









# Python program to find smallest number & largest number in a list


'''# initializing a list with some elements..
list25 = [10,20,30,40,50,60,70,80,90,100,140,100,6535]

#   min() and max is the in-build functions in python
print("The Smallest Number is -->",min(list25))
print("The Smallest Number is -->", max(list25))'''








# Python program to find second largest number in a list


'''#   Initializing a list 
list29 = [7,5,8,9,6,4,2,88,89,456]

#   sort the list using sort method
list29.sort()
print("The sorted list -->", list29)

#   -2 define the second last element from the list
SecondLargestNum = list29[-2]
print("The Second Largest Number is -->",SecondLargestNum)

print("-----------------------------------")

#another way to find a second largest number

#By removing the largest number form the list .
list29.remove(max(list29))

maxNumber = max(list29)
print("The Second Largest Number is -->", maxNumber)'''








# Python program to count Even and Odd numbers in a List

'''list11 = [7,5,8,9,6,4,2,88,89,456]  # initializing a list
print(list11)                           
length = len(list11)                # length stores the length of the list using len function
print("Length of that List is ->",length)
count5 = 0                          # initialze count5 and count6 to 0
count6 = 0
def evenNumber(a,count5):   # a parameterised function
    for i in range(0,length):
        if(a[i]%2 == 0):    # if the remainder is 0 by dividing the elements by 2
            count5 += 1     # then it is a even number otherwise not.
        else:
            continue
    return count5

def oddNumber(a,count6):
    for i in range(0,length):
        if(a[i]%2 != 0):
            count6 += 1
        else:
            continue
    return count6
evenNumberCount = evenNumber(list11,count5)
oddNumberCount = oddNumber(list11,count6)

print(f"The even Number is --> {evenNumberCount}")
print(f"The odd Number is --> {oddNumberCount}")
    '''





# Python program to print positive & negative numbers in a list

'''list9 = [12,45,-8,-87,65,-832, -899]
print(list9)
list10 = []
def listapp(a):
    # self.list10 = list10
    list10.append(a)
    print(list10)

def countnegnumber(list9):
    for i in range(0,len(list9)):
        if (list9[i]<0):
            print(list9[i])
            listapp(list9[i])
    
result10 = countnegnumber(list9)
print(result10)'''






# Python program to count positive and negative numbers in a list


'''list8 = [12,45,-8,-87,65,-832, -899]
count1 = 0
count2 = 0
print(list8)
def negtive(list8,count1):
    for i in range(0, len(list8)):
        if (list8[i]<0):
            count1 +=1
    return count1
def positive(list8,count2):
    for i in range(0, len(list8)):
        if (list8[i]>0):
            count2 +=1
    return count2

resultneg = negtive(list8,count1)
resultpos = positive(list8,count2)

print (f"{resultneg} are the number of negative number & {resultpos} are the positive number in this List")'''





# Remove multiple elements from a list in Python


'''list30 = [12,45,-8,-87,65,-832, -899]

del list30[1:5]

print(list30)'''




# Python | Remove empty tuples from a list


'''
# a list with different data type
list31 = [12,45,(),'babun', (), 'bunny',(), 'bangaon']
print(list31)

for i in list31:
    if i == ():
        list31.remove(i)

print(list31)'''


# Python | Program to print duplicates from a list of integers


'''list32 = [20,80,50,40,0,20,50,0]
 
uniqueList = []
duplicateList = []
 
for i in list32:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(duplicateList)
'''





