# Implementation of TSP : Travelling Salesman Problem in Python.
# By: Darpit Makwana

# Import tsp library
# If you didn't install install using " pip install tsp " command.
import tsp

# Get some inputs from user
matrixSize = int(input("\nEnter The Number Of Vertices : "))

# Initialize empty matrix
matrix = []

# matrix = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

print("Enetr ",matrixSize,"X",matrixSize," Cost Matrix :")
for i in range(matrixSize):
   row = list(map(int, input().split()))
   matrix.append(row)

R = range(len(matrix))

print("\nCost Matrix :")
for i in R:
    print(matrix[i])

# find ShortestPath using tsp module
ShortestPath = {(i,j):matrix[i][j] for i in R for j in R}
maxCost, path = tsp.tsp(R,ShortestPath)

# Printing values
path.append(path[0])
print("\nMaximum Cost : ",maxCost)
print("\nPath : ",end='')
print(*path, sep=" -> ")