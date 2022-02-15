"""
Write a Python program that prompts the user for nonzero integers, 
and then prints the average of all even numbers typed. 
(When the user types 0, stop asking for input.) 
You may assume that the user types at least one even integer. 
The following is an example output from one run of your code:

Integer? 1
Integer? 3
Integer? 2
Integer? 6
Integer? 4
Integer? 10
Integer? 9
Integer? 0
Average: 5.5

"""

total = 0
round = 0
while True:
    num = int(input("Integer? "))
    if num == 0:
        break

    elif num != 0:
        total+=num
        round+=1

ave = total/round
print("Average: ",ave)