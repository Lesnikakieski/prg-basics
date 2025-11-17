###
# Sums numbers entered by user
#
total_sum = 0

div=0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    div+=1

print(f"The total sum of the numbers is: {total_sum} and the arithmetic mean is {total_sum/div}")