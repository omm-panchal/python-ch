n = int(input("Enter number: "))

# Print the top border
print("*" * n)

# Print the middle rows
for i in range(1, n - 1):
    print("*" + " " * (n - 2) + "*")

# Print the bottom border
if n > 1:  # Ensure there's more than one row to print the bottom border
    print("*" * n)
