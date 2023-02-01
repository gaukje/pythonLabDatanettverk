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
    N = len(liste)

    numerator = sum(liste)
    denominator = sum(x ** 2 for x in liste)
    jfi = (numerator ** 2) / (N * denominator)
    return round(jfi, 4)


liste = []  # empty list

with open("task4.txt") as file:
    for line in file:
        value = int(line.split()[0])
        unit = line.split()[1]
        if unit == "Mbps":
            liste.append(value)
        elif unit == "Kbps":
            liste.append(value / 1000)

print(jainsall(liste))
