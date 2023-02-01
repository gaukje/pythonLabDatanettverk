# Task 2
# Write a new function jainsall function that takes a list of throughput values (integers and/or float)
# and returns a JFI

throughputsAmount = int(input("Amount of throughputs: "))

throughputs = []
for num in range(throughputsAmount):
    throughput = float(input("Value of throughput: "))
    throughputs.append(throughput)


def jainsall(throughputs):
    jfi = (sum([x for x in throughputs])) ** 2 / (throughputsAmount * sum(x ** 2 for x in throughputs))
    jfi = round(jfi, 4)
    return jfi


print(jainsall(throughputs))
