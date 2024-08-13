# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:34:35 2024

@author: TAM PC
"""

GPA = float (input("nhap diem trung binh (GPA):"))
if GPA < 3.5:
    print ("hoc luc kem")
elif 3.5 <= GPA < 5.0 :
    print ("hoc luc yeu")
elif 5.0 <= GPA < 7.0 :
    print ("hoc luc trung binh")
elif 7.0 <= GPA < 8.0 :
    print ("hoc luc kha")
elif 8.0 <= GPA < 9.0 :
    print ("hoc luc gioi")
elif 9.0 <= GPA < 10 :
    print ("hoc luc xuat sac")
    