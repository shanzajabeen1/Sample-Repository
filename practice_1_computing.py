# -*- coding: utf-8 -*-
"""Practice 1 computing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EX_gN2nF_ZEHrgTKTYDbwuCZFyj8-CSP
"""

print("Twinkle, twinkle, little star, \n \t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are")

my_name = "Shanza"
my_age = 22
my_address = "Ahmed Heights, H-13, Islamabad"

print("Name:", my_name)
print("Age:", my_age)
print("Address:", my_address)

import sys
print(sys.version)
print(sys.version_info)

feet=float(input("Enter distance in feet: "))
inches=feet
inches=feet/12
yards=0.33*feet
miles=0.000189*feet
print("inches:", inches)
print("yards:", yards)
print("miles:", miles)

seconds = int(input("Enter number of seconds: "))
days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))

total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + (seconds * 1)
print(f"The total time in seconds is: {total_seconds} seconds.")

R=int(input("Enter the radius: "))
Area=3.14*R*R
print(Area)

name_1=input("Enter name_1: ")
name_2=input("Enter name_2: ")
name_reversed=name_2 +  " "  + name_1
print("Reversed Name:", name_reversed)

day = input("Enter the day: ")
month = input("Enter the month: ")
year = input("Enter the year: ")
date = f"{day}/{month}/{year}"
print("Formatted Date:", date)

n=int(input("Enter the value of n: "))
result=(n)+(n*10+n)+(n*100+n*10+n)
print(result)

r=int(input("Enter the value of r:"))
V=4/3*3.14*r*r
print("V=",V)

b=int(input("b="))
h=int(input("H="))
A = 1/2*b*h
print("A=",A)

import math
x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))

Distance= math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance=", Distance)

import multiprocessing
print(multiprocessing.cpu_count())

n = int(input("Enter a positive integer (n): "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_up_to_n = (n * (n + 1)) / 2
    print("sum_up_to_n=", sum_up_to_n)

import math
#base=b,perperdicular=a,hypotenuse=c
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c=math.sqrt(b**2+a**2)
print("c=",c)

x=int(input("x="))
y=int(input("y="))
result= (x + y) * (x + y)
print("result=",result)

kpa=float(input("Input kpa="))
psi = kpa / 6.89475729;
mmHg = (kpa * 760) / 101.325
atm = kpa / 101.325
print("psi=",psi)
print("mmHg=",mmHg)
print("atm=",atm)

x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))
x_mid = (x1 + x2) / 2
y_mid = (y1 + y2) / 2
print("x_mid",x_mid)
print("y_mid",y_mid)