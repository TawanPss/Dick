"""
เขียนฟังก์ชัน firstDigit(s) ซึ่งรับค่าเป็นสตริงและส่งคืนตัวเลขตัวแรกในสตริง หรือส่งคืน 0 ถ้าไม่มีตัวเลขในสตริง

ตัวอย่าง

firstDigit("No. 1") = 1

firstDigit("By 30 years") = 3

firstDigit("") = 0"""

def firstDigit(s):
    default = 0
    if s == "":
        print(default)
    
    for char in s:
        if char in "0123456789":
            print(char)

    
firstDigit("No. 1")

firstDigit("By 30999 years") 

firstDigit("") 