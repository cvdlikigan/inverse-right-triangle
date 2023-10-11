# Define the number of rows for the pattern
num_rows = 5

# Iterate through rows
for i in range(num_rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()
