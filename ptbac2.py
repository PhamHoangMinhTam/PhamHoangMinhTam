# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:27:18 2024

@author: Student
"""
import math

a= float(input("Nhap a(a<>0): "))
b= float(input("Nhập b: "))
c= float(input("Nhập c: "))
delta = b**2-4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1=x2," , -b/(2*a))
elif delta > 0:
    print("Phương trình có nghiệm x1=," , -b + math.sqrt(delta)/(2*a))
    print("Phuong trinh có nghiệm x2=," , -b - math.sqrt(delta)/(2*a))

    
    
    
     