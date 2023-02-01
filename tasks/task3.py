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
