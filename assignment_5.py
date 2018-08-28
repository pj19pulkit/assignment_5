#Q1) Take an input year from user and decide whether it is a leap year or not.

year=int(input("Enter The Year :- "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("%d is a leap year\n" %(year))
       else:
           print("%d is not a leap year\n" %(year))
   else:
       print("%d is a leap year\n" %(year))
else:
   print("%d is not a leap year\n" %(year))


#Q2)Take length and breadth input from user and check whether the dimensions are of square or rectangle.

l=int(input("Enter Length :- "))
b=int(input("Enter Breadt :- "))

if (l==b):
    print("The Dimensions are of Square\n")
else:
    print("The Dimensions are of rectangle\n")

#Q3)Take the input age of 3 people and determine oldest and youngest among them.


x= int(input("Enter First Age :- "))
y=int(input("Enter Second Age :- "))
z=int(input("Enter Third Age :- "))

if (x>y and x>z):
    print(" \nX is the Oldest\n")
else:
    print(" X is the Youngest\n")
if (y>x and y>z):
    print(" Y is the Oldest\n")
else:
    print(" Y is the Youngest\n")
if (z>x and z>y):
    print(" Z is the Oldest\n")
else:
    print(" Z is the Youngest\n")
    
#Q4) Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

age=(input("Enter Age :- "))
gen=input("Enter Gender :- ")
stat=input("Enter Marital Status :- ")

if(age.isnumeric()==1):
    age=int(age)
    if( gen=='F' or gen=='f'):
        print("Employment in the Urban Areas")
    elif(gen=='M' or gen=='m' and age>=20 and age<=40):
        print("Emplyment can be anywhere")
    elif(gen=='M' or gen=='m' and age>=40 and age<=60):
        print("Employment in the Urban Areas\n")
else:
    print("ERROR\n")


#Q5) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.


qty=int(input("Enter The Quantity of the Item"))

if(qty>1000):
        cost=qty*100
        dis=cost*0.1
        tcost=cost-dis
        print("The Total Cost is :- %d" %(tcost))



#<-----LOOPS----->

# Q.1- Take 10 integers from user and print it on screen.
for i in range (1,11):
   num= (int(input("Enter Integers :- ")))
   print(num)
   


#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
    
i=1
while(i>0):
    print(i)
    i=i+1
    
#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

list=[]
list_sq=[]
for i in range (1,6):
    num=int(input("Enter Integers :- "))
    list.append(i)
    list_sq.append(i*i)
print(list)
print(list_sq)


#Q.4- From a list containing ints, strings and floats, make three lists to store them separately

list=[1,2,"python",12,"code",3,4,55,1.23,0.112,98.8976]
list_int=[]
list_str=[]
list_float=[]
for i in list:
    if(isinstance(i,int)):
        list_int.append(i)
    elif(isinstance(i,str)):
         list_str.append(i)
    elif(isinstance(i,float)):
         list_float.append(i)
print(list_int)
print(list_str)
print(list_float)

#Q.5- Using range(1,101), make a list containing only prime numbers.

print("Prime Numbers Between 1 and 101 are\n")
for num in range(1,101):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

   
#Q.6- Print the following patterns:
           

for i in range (0,4):
      for j in range (0,i+1):
          print("*" , end="")
      print()


#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
      
list=[]

for i in range (1,11):
    num=int(input("Enter Elements :- "))
    list.append(num)
print("List Before Deletion\n",list)
x=int(input("Enter Element to be Searched and deleted :- "))
for i in list:
    if(x==i):
        list.remove(i)
else:
    print("List after Deletion\n",list)
















