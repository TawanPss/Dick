"""Write a function named even_sum that prompts the user for many integers and 
print the total even sum and maximum of the even numbers. 
You may assume that the user types at least one non-negative even integer.

how many integers? 4
next integer? 2
next integer? 9
next integer? 18
next integer? 4
even sum = 24
even max = 18"""

n = int(input("how many integers? "))
total = 0
round = 0
max = 0

for i in range(n):
    num = int(input("next integer? "))
    if num%2 == 0:
        total+=num
        if num > max:
            max = num

print("even sum =" ,total)
print("even max =",max)
