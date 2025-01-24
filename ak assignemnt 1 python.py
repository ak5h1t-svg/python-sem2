"""#a=int(input("Enter first number"))
#b=int(input("Enter second number"))
#c=a+b
#print("sum is ",c)


#a=int(input("Enter first number"))
#b=int(input("Enter second number"))
#c=a-b
#print("diff is",c)


#a=int(input("Enter first number"))
#b=int(input("Enter second number"))
#c=a*b
#print("product is",c)


a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a/b
print("division is",c)


a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a+b
print("sum is",c)
d=a-b
print("diff is",d)
e=a*b
print("product is",e)
f=a/b
print("division is",f)


a=int(input("Enter no of hours :"))
b=a*60
print("minutes are ",b)


a=int(input("Enter no of minutes :"))
b=a/60
print("hours are ",b)

a=int(input("Enter dollars amount:"))
b=a*48
print("rupees is ",b)

a=int(input("Enter rupees amount:"))
b=a/48
print("dollars is ",b)

a=int(input("Enter dollar amount:"))
b=a/1.45
print("amount in pound is:",b)

a=int(input("Enter weight in grams:"))
b=a/1000
print("weight in kilo is:",b)


a=int(input("Enter weight in kilo:"))
b=a*1000
print("weight in grams is:",b)


a=int(input("Enter storage in bytes:"))
b=a/1000
print("storage in KB is:",b)
c=b/1000
print("storage in MB is:",c)
d=c/1000
print("storage in GB is:",d)


a=int(input("enter  temperature in celsius:"))
b=(9/5*a)+32
print("temperature in farenheit",b);


a=int(input("enter  temperature in farenheit:"))
b=5/9*(a-32)
print("temperature in celsius",b);


p=int(input("Enter Principle amount:"))
r=int(input("Enter roi :"))
t=int(input("Enter time period of loan :"))
i=(p*r*t)/100
print("total interest on amount is:",i)


l=int(input("Enter the length of side:"))
a=l*l
print("The area of square is:",a);
p=4*l
print("The perimeter of square is:",p);


l=int(input("Enter the lemgth of rect:"))
b=int(input("Enter the breadth of rect:"))
a=l*b
print("The area of rectangle is:",a)
p=2*(l+b);
print("The perimeter of rectangle is:",p)

r=int(input("Enter the radius of circle:"))
a=22/7*r*r
print("The area is :",a);


l=int(input("Enter the length of triangle:"))
h=int(input("Enter the height of triangle:"))
a=(h*l)/2
print("The area of triangle is:",a)


def calculate_net_salary(gross_salary):
    allowance = 0.10 * gross_salary
    
    
    deduction = 0.03 * gross_salary
    
    net_salary = gross_salary + allowance - deduction
    
    return net_salary
gross_salary = float(input("Enter the gross salary: "))
net_salary = calculate_net_salary(gross_salary)
print(f"The net salary is: {net_salary:.2f}")"""

















