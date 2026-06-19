
import copy

def add_matrices(matrix1,matrix2):

    new_matrix1 = copy.deepcopy(matrix1)
    

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("different size of matrics can't be added")
        return -1
    

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):

            new_matrix1[i][j] += matrix2[i][j]

    return new_matrix1


def sub_matrices(matrix1,matrix2):

    new_matrix1 = copy.deepcopy(matrix1)
    

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("different size of matrics can't be added")
        return -1
    

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):

            new_matrix1[i][j] -= matrix2[i][j]

    return new_matrix1

def transpose_matrix(matrix):
    new_matrix = copy.deepcopy(matrix)

    
    transposed = [list(rows) for rows in zip(*new_matrix)]

    return transposed


def sum_of_diagonal(matrix1,matrix2):
    new_matrix1 = copy.deepcopy(matrix1)
    sum = 0
    
    
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("different size of matrics can't be added")
        return -1

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):

            if i == j:
                sum = sum + new_matrix1[i][j] + matrix2[i][j]

    return sum

    

try:
    array_rows = int(input("Enter rows of array : "))
    array_column = int(input("Enter column of array : "))
    arr = []
    arr2 = []
    

    if array_rows <= 0 or array_column <= 0:
        print("please input a number greater than 0.")
        exit()

    for i in range(array_rows):
        row = []
        for j in range(array_column):
            row.append(int(input("Enter a number : ")))

        arr.append(row)

    for i in range(array_rows):
        row = []
        for j in range(array_column):
            row.append(int(input("Enter a number : ")))

        arr2.append(row)

    print(f"first matrix :\n{arr}\n")

    print(f"second matrix :\n{arr2}")

    print(f"Addition of matrices :\n {add_matrices(arr,arr2)}\n")

    print(f"Subtraction of matrices :\n {sub_matrices(arr,arr2)}")

    print(f"transpose of matrix1 :\n{transpose_matrix(arr)}")

    print(f"transpose of matrix 2 :\n{transpose_matrix(arr2)}")

    print(f"Diagonal sum : {sum_of_diagonal(arr,arr2)}")




except ValueError:
    print("invalid input")

