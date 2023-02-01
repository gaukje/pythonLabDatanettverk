# Task 1
# Write a function named jains that takes two throughput values (int and/or float) as arguments and
# returns a JFI


def jains():
    throughput1 = float(input("Enter throughput1: "))   # Asks user for throughput that will be used to calculate fairness
    throughput2 = float(input("Enter throughput2: "))   # Could include error handling, but decided not to

    jfi = (throughput1 ** 2) / (2 * (throughput1 + throughput2))
    # Using the formula in the intro-section but with two throughputs.
    return round(jfi, 4)            # Returning the result with 4 decimals


print("The Jains Fairness Index is: ", jains())         # Printing the function
