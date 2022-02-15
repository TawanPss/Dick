"""เขียนฟังก์ชัน ordinalDate(d, m, y) ซึ่งรับค่าจำนวนเต็มบวกเป็นวันที่ d เดือน m และปีพ.ศ. y และส่งคืนค่าเป็นวันของปี 
โดยนับวันที่ 1 มกราคม เป็นวันที่ 1 และวันที่ 31 ธันวาคม เป็นวันที่ 365 (หรือ 366 สำหรับปีอธิกสุรทิน)

โดยปีอธิกสุรทินคือปีค.ศ.ที่หารด้วย 4 ลงตัวแต่หารด้วย 100 ไม่ลงตัว หรือปีค.ศ.ที่หารด้วย 400 ลงตัว

ตัวอย่าง

ordinalDate(1,1,2564) = 1

ordinalDate(1,2,2564) = 32 (1 กุมภาพันธ์ นับเป็นวันที่ 32 ของปี)

ordinalDate(31,12,2564) = 365

ordinalDate(31,12,2563) = 366 (ปีพ.ศ. 2563 หรือปีค.ศ. 2020 มี 366 วัน)"""

def ordinalDate (d, m, y):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totalDay = d
    
    if (y-543)%4 == 0 and (y-543)%100 != 0 or (y-543)%400 == 0:
        month_days[1] = 29

    for i in range(m-1):
        totalDay += month_days[i]
    
    return totalDay

""""
def ordinalDate(d, m, y):
    total_day = 0
    # leap year
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y%400 == 0 ) or (y%4 == 0) and (y%100 != 0):
        month_days[1] = 28
    for i in range(m - 1):
        total_day += month_days[i]
    total_day += d
    print(total_day)
"""
ordinalDate(1,1,2564)

ordinalDate(1,2,2564) 

ordinalDate(31,12,2564)

ordinalDate(31,12,2563)

    
