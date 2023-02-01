"""
Task 4
Read the throughput values from a file and then use your jainsall function to calculate a JFI. Note:
you must use the same units.
The text file contains:
7 Mbps
1200 Kbps
15 Mbps
32 Mbps
"""


def jainsall(data):
    N = len(liste)  # The amount of elements in the list

    # Decided that it would be easier to define the numerator and the denominator

    numerator = sum(liste)  # Calculating the numerator of the JFI formula by summing the values in the list
    denominator = sum(
        x ** 2 for x in liste)  # Calculating the denominator by summing the squares of the values in the list
    jfi = (numerator ** 2) / (N * denominator)  # Using the formula for JFI, using the variables defined above
    return round(jfi, 4)  # Returning the result with 4 decimals


liste = []  # empty list

with open("task4.txt") as file:   # Open the file "task4.txt"
    for line in file:
        value = int(line.split()[0])        # Separating values and units using .split()[i]
        unit = line.split()[1]
        if unit == "Mbps":              # If the unit is Mbps, add the value to the list as-is
            liste.append(value)
        elif unit == "Kbps":            # If the unit is Kbps, convert it to Mbps by dividing by 1000 and add to list
            liste.append(value / 1000)

print(jainsall(liste))

"""
In this code, the jainsall function takes in a list of values as its input parameter, calculates the Jain's Fairness 
Index (JFI) from the values, and returns the result rounded to 4 decimal places. If the input data is not a list, an 
exception will be raised. The code reads the throughput values and units from a file and adds the values to a list 
after converting them to Mbps if the units are Kbps. The jainsall function is then called with the list of values and
 the result is printed.
"""