###
# Function that returns the full name of a day of the week
# based on its number
#


def day_name(day_number):
    days={
        1:"monday",
        2:"tuesday",
        3:"wednesday",
        4:"thursday",
        5:"friday",
        6:"saturday",
        7:"sunday"
    }
    result=days[day_number]
    return result

# Function usage
print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))