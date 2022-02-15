"""เขียนฟังก์ชัน undouble(s) ซึ่งรับค่าเป็นสตริงและส่งคืนสตริงโดยตัดตัวอักษรที่ติดกันที่เหมือนกันให้เหลือตัวเดียว

ตัวอย่าง

undouble("mississippi") = "misisipi" (เปลี่ยน ss เป็น s และ pp เป็น p)

undouble("little") = "litle" (ตัด t ออก 1 ตัว)

undouble("") = "" (ไม่เปลี่ยน)

ให้สมมติได้ว่าสตริงไม่มีตัวอักษรเหมือนกันเขียนติดกันเกิน 2 ตัว"""

from os import remove


def undouble(s):
    for n in range(len(s)):
        if s[n-1] == s[n]:
            #print(s.replace(s[n-1] and s[n], s[n]))
            print(s[n])
        
undouble("mississippi")