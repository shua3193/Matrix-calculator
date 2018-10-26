#-------------------
# Matrix calculator
#-------------------

from MatrixFuncs import *



# Functions
#-----------------------------------------------------------------------------
# AskSize()                              # returns size of matrix
# PrintMat(matrix)                       # Prints matrix
# InputA(mat, nxn)                       # Gets input for A matrix
# InputB(mat, nxn)                       # Gets input for b matrix
# MakeAug(matrix, answer, nxn)           # Makes Augmented matrix
# MakeRed(matrix, identity, nxn)         # Makes Reduction matrix
# GetInvFromRed(matrix, inverse, nxn)    # Extracts Inverse matrix from reduced matrix
# GetAnsFromAug(matrix, XMat, nxn)       # Extracts Variable matrix from Augmented matrix 
# MakeAnsMat(inverse, bMat, XMat, nxn)   # Gets Variable (X) matrix using X=(A^-1)b
# AskMethod()                            # returns method of choice
# ValidMethod()                          # returns valid method for matrix
# ValidSize()                            # returns valid size for matrix
# GaussianElim(matrix, way, nxn)         # performs Gaussian Elim on matrix
# MatrixCleaner(matrix, way, nxn)        # cleans matrix. abs of 0. Rounds to 8 digits
# MatrixSort(Mat)                        # ensures Mat(i=j) not zeros
# Transpose(matrix, transpose, nxn)      # transposes and saves matrix
# RowChecker(matrix, matrixT, find, nxn) # returns T/F. checks if any row/column all zero
# RemoveRed(matrix, nxn)                 # removes reduction from matrix
#
#
#-----------------------------------------------------------------------------
#### UNTESTED ValidResp(func, gVal1, gVal2)   # ensures valid input




nxn = ValidSize()
method = ValidMethod()
MethodsList = ["Gaussian", "Reduction"]
print(f'Matrix is {nxn}x{nxn}')
print(f'Using {MethodsList[method-1]} method')

rowIsZero = []
aug = 1

if nxn == 3:
    A = [[],[],[]]
    b = [[],[],[]]
    I = [[1,0,0],[0,1,0],[0,0,1]]
    AT = [[0,0,0],[0,0,0],[0,0,0]]
    X = [[0],[0],[0]]
    inv = [[],[],[]]
    red = nxn
elif nxn == 4:
    A = [[],[],[],[]]
    b = [[],[],[],[]]
    I = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    AT = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    X = [[0],[0],[0],[0]]
    inv = [[],[],[],[]]
    red = nxn
else:
    print("This is not a supported matrix size")
print(" ")
print("Insert an invertable matrix")
InputA(A, nxn)
InputB(b, nxn)

if method == 1:
    MakeAug(A, b, nxn)
    MatrixSort(A)
    print("A Matrix:")
    PrintMat(A)
    GaussianElim(A, aug, nxn)
    MatrixCleaner(A, aug, nxn)
    GetAnsFromAug(A, X, nxn)
    print("reduced A:")
    PrintMat(A)
    print("b Matrix:")
    PrintMat(b)
    print("X Matrix:")
    PrintMat(X)
elif method == 2:
    MakeRed(A, I, nxn)
    MatrixSort(A)
    print("A Matrix:")
    PrintMat(A)
    GaussianElim(A, red, nxn)
    MatrixCleaner(A, red, nxn)
    GetInvFromRed(A, inv, nxn)
    RemoveRed(A, nxn)
    Transpose(A, AT, nxn)
    invertable = RowChecker(A, AT, rowIsZero, nxn)
    if invertable == False:
        print("Inverse does not exist.")
        print("Here are your matrices.")
    elif invertable == True:
        MakeAnsMat(inv, b, X, nxn)
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




