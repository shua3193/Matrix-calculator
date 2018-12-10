#-------------------
# Matrix calculator
#-------------------

from MatrixFuncs import *


# Functions
#-----------------------------------------------------------------------------
# PrintMat(matrix)                     # Prints matrix
# InputA(mat, n, m)                    # Gets input for A matrix
# InputB(mat, n)                       # Gets input for b matrix
# MakeAug(matrix, answer, n)           # Makes Augmented matrix
# MakeRed(matrix, identity, n)         # Makes Reduction matrix
# GetInvFromRed(matrix, inverse, n)    # Extracts Inverse matrix from reduced matrix
# GetAnsFromAug(matrix, XMat, n)       # Extracts Variable matrix from Augmented matrix 
# MakeAnsMat(inverse, bMat, XMat, n)   # Gets Variable (X) matrix using X=(A^-1)b
# AskMethod()                          # returns method of choice
# AskSize()                            # returns size of matrix
# ValidMethod()                        # returns valid method for matrix
# ValidSize()                          # returns valid size for matrix
# GaussianElim(matrix, way, n, m)      # performs Gaussian Elim on matrix
# MatrixCleaner(matrix, way, n, m)     # cleans matrix. abs of 0. Rounds to 8 digits
# MatrixSort(Mat)                      # ensures Mat(i=j) not zeros
# Transpose(matrix, transpose, n, m)   # transposes and saves matrix
# RowChecker(matrix, matrixT, n)       # returns T/F. checks if any row/column all zero
# RemoveRed(matrix, n)                 # removes reduction from matrix
# MatrixCreator(matrix,n)              # creates matrix with proper amount of i
# MatrixFill(mat,n,m,isI)              # creates matrix with proper amount of zeros and ones
# FreePivAns(mat, matrixT)             # works witl A and AT to find free vars and piv vars
#
#
#-----------------------------------------------------------------------------
#### UNTESTED ValidResp(func, gVal1, gVal2)   # ensures valid input
## above code is in Code Holder file.



# hold = AskSize()
# n = hold #int(input("How many rows (equations)?"))
# m = hold #int(input("How many columns (variables)?"))
# if n == m:
#     method = ValidMethod()
# else:
#     method = 1
# MethodsList = ["Gaussian", "Reduction"]
# print(f'Matrix is {n}x{m}')
# print(f'Using {MethodsList[method-1]} method')





# A = []
# b = []

# # setting the matrices
# MatrixCreator(A,n)
# MatrixCreator(b,n)

# print(" ")
# InputA(A, n, m)
# InputB(b, n)


A = [\
   [2,2,-1,0,1],\
   [-1,-1,2,-3,1],\
   [1,1,-2,0,-1],\
   [0,0,1,1,1]]
b = [[0],[0],[0],[0]]
n = 4
m = 5

method  = 1

if method == 1:
    aug = 1
    MakeAug(A, b, n)
    MatrixSort(A)
    print("A Matrix:")
    PrintMat(A)
    GaussianElim(A, aug, n, m)
    MatrixCleaner(A, aug, n, m)
    if n == m:
        X = []
        MatrixFill(X,n,1,False)
        GetAnsFromAug(A, X, n)
        print("reduced A:")
        PrintMat(A)
        print("b Matrix:")
        PrintMat(b)
        print("X Matrix:")
        PrintMat(X)
    else:
        PrintMat(A)
        AT = []
        MatrixFill(AT,m+1,n,False)
        Transpose(A, AT, n, m)
        print(FreePivAns(A, AT))
elif method == 2:
    red = n
    inv = []
    I = []
    AT = []
    MatrixCreator(inv,n)
    MatrixFill(I,n,m,True)
    MakeRed(A, I, n)
    MatrixSort(A)
    print("A Matrix:")
    PrintMat(A)
    GaussianElim(A, red, n, m)
    MatrixCleaner(A, red, n, m)
    GetInvFromRed(A, inv, n)
    RemoveRed(A, n)
    Transpose(A, AT, n, m)
    invertable = RowChecker(A, AT, n)
    if invertable == False:
        print("Inverse does not exist.")
        print("Here are the existing matrices.")
    else:
        X = []
        MatrixFill(X,n,1,False)
        MakeAnsMat(inv, b, X, n)
        print("inv Matrix:")
        PrintMat(inv)
        print("b Matrix:")
        PrintMat(b)
        print("X Matrix:")
        PrintMat(X)
    print("reduced A:")
    PrintMat(A)
else:
    print("No method was chosen. Please restart")




