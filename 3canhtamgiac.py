# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:18:30 2024

@author: Student
"""

a = float(input("Nhập vào cạnh a: "))
b = float(input("Nhập vào cạnh b: "))
c = float(input("Nhập vào cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    print("a, b, c có thể là ba cạnh của một tam giác")
else:
    print("a, b, c không thể là ba cạnh của một tam giác")