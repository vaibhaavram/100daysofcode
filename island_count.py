string = input().split()
print(string)
R = string[0]
C = string[1]


# initializing an empty matrix
matrix = []
# taking 2x2 matrix from the user
for i in range(R):
   # taking row input from the user
   row = list(map(int, input().split()))
   # appending the 'row' to the 'matrix'
   matrix.append(row)
# printing the matrix
print(matrix)
