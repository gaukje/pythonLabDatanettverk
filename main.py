# Task 1
# Write a function named jains that takes two throughput values (int and/or float) as arguments and
# returns a JFI

"""
def jains():
    throughput1 = float(input("Enter throughput1: "))
    throughput2 = float(input("Enter throughput2: "))

    jfi = (throughput1 ** 2) / (2 * (throughput1 + throughput2))
    # Using the formula in the intro-section but with two throughputs.
    return round(jfi, 4)


print("The Jains Fairness Index is: ", jains())

"""
# Task 2
# Write a new function jainsall function that takes a list of throughput values (integers and/or float)
# and returns a JFI

throughputsAmount = int(input("Amount of throughputs: "))

throughputs = []
for num in range(throughputsAmount):
    throughput = float(input("Value of throughput: "))
    throughputs.append(throughput)


def jainsall(throughputs):
    jfi = (sum([x ** 2 for x in throughputs])) / (throughputsAmount * sum(throughputs))
    jfi = round(jfi, 4)
    return jfi


print(jainsall(throughputs))
