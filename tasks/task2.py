# Task 2
# Write a new function jainsall function that takes a list of throughput values (integers and/or float)
# and returns a JFI

# Decided to solve the task using user input

throughputsAmount = int(input("Amount of throughputs: "))   # Asking user for amounts of throughputs.

throughputs = []                # Empty list
for num in range(throughputsAmount):        # For each throughput:
    throughput = float(input("Value of throughput: "))      # Define it's value
    throughputs.append(throughput)                      # Insert value into list


def jainsall(throughputs):
    jfi = (sum([x for x in throughputs])) ** 2 / (throughputsAmount * sum(x ** 2 for x in throughputs))
    jfi = round(jfi, 4)
    return jfi

"""
Similarly to task1, calculate the fairness using the formula from the introduction and returning 
the result with 4 decimals. However, in this casewe used "throughputsAmount" as the "N" in 
the formula, as the amount varies from input.

"""

print(jainsall(throughputs))
