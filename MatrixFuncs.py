


#------------------------------------------------------
# Use line to import all functions from this library
#from MartixFuncs import *
#------------------------------------------------------


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




#--------------------------
# printing matrices to show
#--------------------------
def PrintMat(matrix):
  for i in range(len(matrix)): # prints all the rows for formating
    print(matrix[i])

# -----------------------------------------------------------------------------------------------------------------
#----------------------------
# Creating secondary matrices
#----------------------------

#Getting INVERSE matrix from reduction method
def RemoveRed(matrix, n):
  for i in range(n):
    for j in range(n):   # removes n last elements out of end of matrix one at a time
      del matrix[i][-1]

#create agumented matrix
def MakeAug(matrix, answer, n):
  for i in range(n):
    matrix[i] += answer[i]   # adds element of answer row i into row i of matrix

#create reduction matrix for inverse finding
def MakeRed(matrix, identity, n):
  for i in range(n):
    matrix[i] += identity[i]     # adds row i of identity to row i of matrix

#Getting INVERSE matrix from reduction method
def GetInvFromRed(matrix, inverse, n): # inv only works with square thus n
  for i in range(n):
    for j in range(n):
      inverse[i].append(matrix[i][j+n])

# Extracts Variable matrix from Augmented matrix
def GetAnsFromAug(matrix, XMat, n): 
  for i in range(n):
    XMat[i][0] = (matrix[i][-1])
# [-1] counts from right. meaning last element [-2] is second to last

# transposes matrix
def Transpose(matrix, transpose, n, m):
  for i in range(n):
    for j in range(m):
      transpose[j][i] = matrix[i][j] #swaps sub i and j for transpose

# matrix multiplication of inv n by n and b
def MakeAnsMat(inverse, bMat, XMat, n): # invs only works with square matrices
  for i in range(n):
    for j in range(n):
      XMat[i][0] += (inverse[i][j])*(bMat[j][0])

#-----------------------------------------
# Creating and geting inputs for matrices
#-----------------------------------------
      
# input for A maxtix
def InputA(mat, n, m):
  for i in range(n):
    for j in range(m):
      mat[i].append(int(input(f'number for {i+1},{j+1}: ')))

# input for b matrix
def InputB(mat, n):
  for i in range(n):
    mat[i].append(int(input(f'number for {i+1},1: ')))

# creates matrix with proper amount of i
def MatrixCreator(matrix,n):
  for i in range(n):
    matrix.append([])   # fills mats with proper amount of i (rows)

# creates matrix with proper amount of zeros and ones
def MatrixFill(mat,n,m,isI):
  for i in range(n):
    mat.append([0]*m)   # fills mat with zeros
  if isI == True:           # is it an I mat? if yes give 1's in i=j pos
    for i in range(n):
      mat[i][i] = 1

# -----------------------------------------------------------------------------------------------------------------
 


# gets size of matrix
def AskSize():
  a = int(input("What is the square of the matrix? "))
  return a

# returns method of choice
def AskMethod():
  print("What method would you like to use?")
  print("(Gaussian = 1, Reduction = 2)")
  a = int(input("Type 1 or 2 here: "))
  return a

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


# -----------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------
# funcs that perform operations on Matrices. Editing matrices
#------------------------------------------------------------

# performs Gaussian Elim on matrix
def GaussianElim(matrix, way, n, m):
  for z in range(n):
    iRange = []                   # a range so it wont do op on its own row
    for l in range(n):            # adding all rows to oped on 
      iRange.append(l)              
    iRange.remove(z)              # removes current row to not op on self
    aii = (matrix[z][z])          # saves a[i][i] value
    if aii == 0:                  # if aii is zero move to next j elm
      shift = 0                   # use this as j elm shifter
      while aii == 0:  
        shift += 1           
        aii = matrix[z][z+shift]  # moves aii to next elm
      # print(f'Using m {z+shift}')    # if a[i][i] is 0 then cannot operate on row. returns errors
      # print("Your cutoff A is here:")
      # PrintMat(matrix)
      # print("")
      # break
    for y in range(m + way):      # for all [j] elms
      matrix[z][y] /= aii         # divide to change row to leading 1
    for i in iRange:              # which rows to perform ops on (i row)
      opElm = matrix[i][z]        # saves value of leading elm on row to be oped on
      for j in range(m + way):    # remove z row from i row at each j elm
        matrix[i][j] -= (matrix[z][j]*opElm)
    #PrintMat(matrix)
    #print("")

# cleans matrix. Gets abs of 0. Rounds elements to 8 digits
def MatrixCleaner(matrix, way, n, m):
  for i in range(n):
    for j in range(m + way):
      if matrix[i][j]==0:                    #if the elm is 0 get abs
        matrix[i][j]=abs(matrix[i][j])
      else:                                  # if not 0 then round to 8 digits
        matrix[i][j]=round(matrix[i][j], 8)

# sorts matrix to not have zeros in i=j spots
def MatrixSort(Mat):
  for twice in range(3):        # happens 2 times
    i = len(Mat)-1              # ensures last a[i][i] elm not 0
    if Mat[i][i] == 0:
      swap = Mat[i]
      Mat[i] = Mat[0]
      Mat[0] = swap
    for i in range(len(Mat)):   # ranges through a[i][i] to ensure no 0
      if Mat[i][i] == 0:
        Mat.append(Mat.pop(i))  # if it is then throw it to end

def RowChecker(matrix, matrixT, n):
  check = True                   # claims true until otherwise shown
  for i in range(n):             # to check rows
    if any(matrix[i])== False:   # if any() = false then row has only zeros
      check = False              # if all zeros then check is set to false
      break
  if check == True:              # if check is still True since all rows in A are True check the AT
    for i in range(n):  
      if any(matrixT[i])== False:
        check = False
        break
  return check                   # if check is False A not invertable but if True A is Invertable


# changes all elements into fractions
def Frac(mat):
  from fractions import Fraction
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      mat[i][j] = Fraction(mat[i][j])

# -----------------------------------------------------------------------------------------------------------------

# works will AT to find free vars and piv vars
def FreePivAns(mat, matrixT):
  VarsLoc = []
  PivVars = set()                        # change to an int if data is not needed
  for i in range(len(matrixT)-1):
    for j in range(len(matrixT[i])):
      if matrixT[i][j] != 0:                # elms == 0 are disregarded since they hold no info
        VarsLoc.append(f'{j}{i}{j}')   # [a][0] = x num, [a][1] = j, [a][2] = i
        # VarsLoc.append('%s%s%s' % (j,i,j))  # [a][0] = x num, [a][1] = j, [a][2] = i
        PivVars.add(j)
  PivVars = list(PivVars)
  VarsLoc.sort()
  FVars = (len(matrixT) - len(PivVars) - 1)  # amount of free vars
  if FVars > 0:                             # choose letters for free vars
    string = 'strmnpqghkldf'
    FreeVars = [string[z] for z in range(FVars)]
    VSoln = []
    for l in range(FVars):
      # VSoln = [[[0]*(len(matrixT)-1)]*FVars]
      VSoln.append([0]*(len(matrixT)-1))
    for i in PivVars:
      VSoln.insert(i, None)
      FreeVars.insert(i,None)
  for Var in VarsLoc:
    if Var[0] != Var[1] or Var[1] != Var[0]:
      VSoln[int(Var[1])][int(Var[0])] = -mat[int(Var[2])][int(Var[1])]
  FreeVarX = [x for x in range(len(mat[0])-1)]
  h = 0
  while h < len(FreeVarX):
    if FreeVarX[h] in PivVars:
      FreeVarX.remove(FreeVarX[h])
      h =-1
    h+=1
  for i in FreeVarX:
    VSoln[i][i] = 1
  AnswerString = "X = "
  for i in range(len(FreeVars)):
    if FreeVars[i] != None:
      AnswerString += f'+{FreeVars[i]} * {VSoln[i]}'
      # AnswerString += "%s * %s " % (FreeVars[i],VSoln[i])
  return AnswerString


# -----------------------------------------------------------------------------------------------------------------