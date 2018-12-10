#-----------------------------------------------------------
# holds unnecessary code. might be useful at a later time. 
#-----------------------------------------------------------



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

n=0


if n == 3:
    A = [[],[],[]]
    b = [[],[],[]]
    I = [[1,0,0],[0,1,0],[0,0,1]]
    AT = [[0,0,0],[0,0,0],[0,0,0]]
    X = [[0],[0],[0]]
    inv = [[],[],[]]
elif n == 4:
    A = [[],[],[],[]]
    b = [[],[],[],[]]
    I = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    AT = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    X = [[0],[0],[0],[0]]
    inv = [[],[],[],[]]
else:
    print("This is not a supported matrix size")


#create reduction matrix for inverse finding
def MakeRed(matrix, identity, n):
  for i in range(n):
    matrix[i] += identity[i]     # adds row i of identity to row i of matrix
    #for j in range(n):
      #matrix[i].append(identity[i][j])     #adds 1 element at a time

#create agumented matrix
def MakeAug(matrix, answer, n):
  for i in range(n):
    matrix[i] += answer[i]   # adds element of answer row i into row i of matrix
    #matrix[i].append(answer[i][0])  # adds element in b to end of row i of matrix


# <<<<-------------------------------->>>>
# Removed due to better code being written
# <<<<-------------------------------->>>>

# checks if a row in A == zero returns T/F
def RowChecker(matrix, matrixT, n):
  find = []
  for i in range(n):              # adds all rows of A and AT to find list
    find.append(any(matrix[i]))   # adds true if any elms not zero.
    find.append(any(matrixT[i]))  # adds false if all zeros
  for i in range(len(find)):
    find[i] = not find[i]         # inverts all trues and falses. if anything in find is True then there was a zero row
  return not any(find)            # returns false if a row was zero (anyfind is true) true if no zero rows









    
