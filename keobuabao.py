
"""
Created on Tue Aug 13 20:08:46 2024

@author: Student
"""
import random
luachon = ("kéo","búa","bao")
nguoichoi = input("lựa chọn(kéo-búa-bao:")
may = random.choice(luachon)
print(f"ban chon: {nguoichoi}")
print(f"maychon: {may}")
if nguoichoi == may:
    print("hoa")
elif may == "bua" and nguoichoi == "keo" or\
     may == "keo" and nguoichoi == "bao" or\
     may == "bao" and nguoichoi == "bua":
            print("may thang")
else:
    print("may thua")
