# Python program to calculate Simple Interest

# Input from user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Calculate Total Amount
total_amount = principal + simple_interest

# Display the results
print("\nPrincipal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time:", time, "years")
print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)
