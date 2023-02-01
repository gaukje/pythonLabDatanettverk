"""
Read the throughput values from a file and then use your jainsall function to calculate a JFI.
The text file contains:
7 Mbps
12 Mbps
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

with open("task3.txt") as file:
    for line in file:
        throughputs = line.split()
        print(throughputs)
        liste.append(int(throughputs[0]))

print(jainsall(liste))
