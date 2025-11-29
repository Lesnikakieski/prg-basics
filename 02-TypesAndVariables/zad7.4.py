'''
A tree may be cut down if its diameter is at least 50 cm.
 Write a program that, based on the circumference of the tree entered from the keyboard, calculates and prints the value True if the tree can be cut down, or
print the value False otherwise. Sample result:

Enter tree circumference in cm: 120 
Tree can be cut down: False
'''

circumference = int(input("circumnference : "))
result = circumference/6.28 >= 50
print(result)