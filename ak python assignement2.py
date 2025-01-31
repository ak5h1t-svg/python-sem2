"""a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if (a>b):
    print(a,"is largest value")
else:
    print(b,"is largest value")


a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
if (a>b & a>c):
    print(a,"is largest number")
elif(b>a & b>c):
    print(b,"is largest while")
else: 
    print(c,"is largest value")



a=int(input("Enter the first number"))
if (a%2==0):
    print(a,"is even")
else:
    print(a,"is odd")



a=int(input("Enter the first number"))
if (a%10==0):
    print(a,"is divisible by 10")
else:
    print(a,"is not divisible by 10")


age=int(input("Enter age:"))
if age>=18:
    print("major")
else:
    print("Minor")


a=input("Enter the number")
b=len(a)
print("The length is",b)


a=int(input("Enter the year:"))
if a%4==0:
    print(a,"is a leap year")
else:
    print(a,"is not a leap year")


a=int(input("Enter the first angle"))
b=int(input("Enter the second angle"))
c=int(input("Enter the third angle"))
if(a+b+c==180):
    print("The triangle is valid")
else:
    print("The triangle is not valid")


a=int(input("Enter the first number"))
if a<0:
    b=a*(-1)
    print("The absolute value is",b)
else:
    print("The absolute value is",a)"


l=int(input("Enter the lengt of rectangle"))
b=int(input("Enter the breadth of rectangle"))
a=l*b
p=2*(l+b)
if a>p:
    print("The area of rect is larger")
else :
    print("Thee perimeter of rect is larger")



'''x1=int(input("Enter Number:"))
y1=int(input("Enter Number:"))
x2=int(input("Enter Number:"))
y2=int(input("Enter Number:"))
x3=int(input("Enter Number:"))
y3=int(input("Enter Number:"))

def are_points_collinear(x1, y1, x2, y2, x3, y3):
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)==0)

if are_points_collinear(x1,y1,x2,y2,x3,y3):
    print("The points are collinear.")
else:'
    print("The points are not collinear.")

'''def numbertowords(n):
   
    number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
        "eighteen", "nineteen" ]
    
  
    if 0 <= n <= 19:
        return number_words[n]
    else:
        return "Number out of range"'''

def get_grade(marks):
    if marks <= 39:
        return 'F'
    elif marks <= 44:
        return 'P'
    elif marks <= 49:
        return 'C'
    elif marks <= 54:
        return 'B'
    elif marks <= 59:
        return 'B+'
    elif marks <= 69:
        return 'A'
    elif marks <= 79:
        return 'A+'
    else:
        return 'O'

def main():
    
    marks1 = int(input("Enter marks for subject 1 (0-100): "))
    marks2 = int(input("Enter marks for subject 2 (0-100): "))
    marks3 = int(input("Enter marks for subject 3 (0-100): "))

    if marks1 <= 39 or marks2 <= 39 or marks3 <= 39:
        result = "Fail"
    else:
        result = "Pass"

    total = marks1 + marks2 + marks3
    average = total / 3

    print("\nTotal Marks:", total)
    print("Average Marks:", average)
    print("Result:", result)

    
    print("\nSubject 1 Grade:", get_grade(marks1))
    print("Subject 2 Grade:", get_grade(marks2))
    print("Subject 3 Grade:", get_grade(marks3))


main()
"""




