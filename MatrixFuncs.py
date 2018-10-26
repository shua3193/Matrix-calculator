


#------------------------------------------------------
# Use line to import all functions from this library
#from MartixFuncs import *
#------------------------------------------------------


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




#--------------------------
# printing matrices to show
#--------------------------
def PrintMat(matrix):
  for i in range(len(matrix)):
    print(matrix[i])

#--------------------------------------
#matrix multiplication of inv nxn and b
#--------------------------------------
def MakeAnsMat(inverse, bMat, XMat, nxn):
  for i in range(nxn):
    for j in range(nxn):
      XMat[i][0] += (inverse[i][j])*(bMat[j][0])
#-------------------------------------------------------------------
#----------------------------
# Creating secondary matrices
#----------------------------

#Getting INVERSE matrix from reduction method
def RemoveRed(matrix, nxn):
  for i in range(nxn):
    for j in range(nxn):
      del matrix[i][-1]

#create agumented matrix
def MakeAug(matrix, answer, nxn):
  for i in range(nxn):
    matrix[i].append(answer[i][0])

#create reduction matrix for inverse finding
def MakeRed(matrix, identity, nxn):
  for i in range(nxn):
    for j in range(nxn):
      matrix[i].append(identity[i][j])

#Getting INVERSE matrix from reduction method
def GetInvFromRed(matrix, inverse, nxn):
  for i in range(nxn):
    for j in range(nxn):
      inverse[i].append(matrix[i][j+nxn])

# Extracts Variable matrix from Augmented matrix
def GetAnsFromAug(matrix, XMat, nxn):
  for i in range(nxn):
    XMat[i][0] = (matrix[i][-1])
# [-1] counts from right. meaning last element [-2] is second to last

# transposes matrix
def Transpose(matrix, transpose, nxn):
  for i in range(nxn):
    for j in range(nxn):
      transpose[i][j] = matrix[j][i]


#-------------------------------------------------------------------
# input for A maxtix
def InputA(mat, nxn):
  for i in range(nxn):
    for j in range(nxn):
      mat[i].append(int(input(f'number for {i+1},{j+1}: ')))

# input for b matrix
def InputB(mat, nxn):
  for i in range(nxn):
    mat[i].append(int(input(f'number for {i+1},1: ')))

#-------------------------------------------------------------------

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#setting matrix sizes so no append func

#if nxn == 3:
#    A = [[],[],[]]
#    b = [[],[],[]]
#    I = [[1,0,0],[0,1,0],[0,0,1]]
#    x = [[0],[0],[0]]
#    inv = [[],[],[]]
#elif nxn == 4:
#    A = [[],[],[],[]]
#    b = [[],[],[],[]]
#    I = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
#    x = [[0],[0],[0],[0]]
#    inv = [[],[],[],[]]
#else:
#    print("This is not a supported matrix size")
#    quit()

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------

# gets size of matrix
def AskSize():
  a = int(input("What is the square of the matrix? (3 or 4) "))
  return a

# returns method of choice
def AskMethod():
  print("What method would you like to use?")
  print("(Gaussian = 1, Reduction = 2)")
  a = int(input("Type 1 or 2 here: "))
  return a



# NOT WORKING --- NOT WORKING --- NOT WORKING --- NOT WORKING
# NOT WORKING --- NOT WORKING --- NOT WORKING --- NOT WORKING
# NOT WORKING --- NOT WORKING --- NOT WORKING --- NOT WORKING
# NOT WORKING --- NOT WORKING --- NOT WORKING --- NOT WORKING

# ensures valid response
def ValidResp(function, valid1, valid2):
  var = 2000
  while var != valid1 and var != valid2:
    var = function
    if var == valid1 or var == valid2:
      break
    else:
      print("You entered an invalid response.")
      print("Please try again.")
  return var

# NOT WORKING --- NOT WORKING --- NOT WORKING --- NOT WORKING
# NOT WORKING --- NOT WORKING --- NOT WORKING --- NOT WORKING
# NOT WORKING --- NOT WORKING --- NOT WORKING --- NOT WORKING
# NOT WORKING --- NOT WORKING --- NOT WORKING --- NOT WORKING

# gets valid method
def ValidMethod():
  m = 1000
  while m != 1 and m != 2:
    m = AskMethod()
    if m == 1 or m == 2:
      break
    else:
      print("You entered invalid method. Please input valid method number")
  return m

# gets valid size
def ValidSize():
  m = 1000
  while m != 3 and m != 4:
    m = AskSize()
    if m == 3 or m == 4:
      break
    else:
      print("You entered invalid matrix size. Please input valid size")
  return m

# performs Gaussian Elim on matrix
def GaussianElim(matrix, way, nxn):
  for z in range(nxn):
    iRange = []                   # a range so it wont do op on its own row
    for l in range(nxn):             # l used to be x
      iRange.append(l)               #if something stops working change back.
    iRange.remove(z)
    do = (matrix[z][z])
    if do == 0:
      PrintMat(matrix)
      break
    for y in range(nxn + way):       # y used to be j. 
      matrix[z][y] /= do             #if something stops working change back.
    for i in iRange:              # which rows to perform ops on
      do = matrix[i][z]
      for j in range(nxn + way):
        matrix[i][j] -= (matrix[z][j]*do)
    #PrintMat(matrix)
    #print("")

# cleans matrix. Gets abs of 0. Rounds elements to 8 digits
def MatrixCleaner(matrix, way, nxn):
  for i in range(nxn):
    for j in range(nxn + way):
      if matrix[i][j]==0:
        matrix[i][j]=abs(matrix[i][j])
      matrix[i][j]=round(matrix[i][j], 8)

# sorts matrix to not have zeros in i=j spots
def MatrixSort(Mat):
  for twice in range(3):
    i = len(Mat)-1
    if Mat[i][i] == 0:
      swap = Mat[i]
      Mat[i] = Mat[0]
      Mat[0] = swap
    for i in range(len(Mat)):
      if Mat[i][i] == 0:
        Mat.append(Mat.pop(i))

# checks if a row in A is == to zero returns T/F
def RowChecker(matrix, matrixT, find, nxn):
  for i in range(nxn):
    find.append(any(matrix[i]))
    find.append(any(matrixT[i]))
  for i in range(len(find)):
    find[i] = not find[i]
  return not any(find)

# changes all elements into fractions
def Frac(mat):
  from fractions import Fraction
  for i in range(len(mat)):
    for j in range(len(mat[1])):
      mat[i][j] = fraction(mat[i][j])
