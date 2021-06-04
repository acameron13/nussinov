#Pierce McDonnell, Molly Kammann, and Alison Cameron
#Nussinov's Algorithm
#CS252

import sys
import math
import numpy as np

#Read in the input
def read_input(filename):
  nucleotides = []
  with open(filename, "r") as input_file:
    rna_strand = input_file.readline()

  for ch in rna_strand:
    #Check if input is valid
    if ch in ["A", "C", "G", "U"]:
      nucleotides.append(ch)
    elif ch in ["\n", " "]:
        continue
    else:
      sys.exit("Input is not valid")

  return nucleotides

#Initializing the Matrix
def create_matrix(n):
  opt_score = []
  for i in range(n):
    scores_i = []
    for j in range(n):
      scores_i.append(0)
    opt_score.append(scores_i)

  for i in range(n):
    opt_score[i][i] = 0
    if i >= 1:
      opt_score[i][i-1] = 0

  return opt_score

#Filling in the Matrix
def populate_matrix(mat, rna):
    for j in range(1, len(mat)):
        for i in reversed(range(0, j)):
            fold_nums = []
            for k in range(i, j):
                num = mat[i][k-1] + mat[k+1][j-1] + score(rna[k], rna[j])
                fold_nums.append(num)
            fold_nums.append(mat[i][j-1])
            mat[i][j] = max(fold_nums)
    return mat


#Display Matrix neatly
def print_matrix(mat):
  opt_score_array = np.array(mat)
  print(opt_score_array)

#determine if any two bases are complementary
def score(base1, base2):
    if base1 == "A" and base2 == "U":
        return 1
    elif base1 == "U" and base2 == "A":
        return 1
    elif base1 == "C" and base2 == "G":
        return 1
    elif base1 == "G" and base2 == "C":
        return 1
    else:
        return 0

#Go back through the matrix to identify base pairs
def traceback(opt_score, rna):
   n = len(opt_score) - 1
   stack = [] #temporary working stack
   visited = [] #stores the base pairs that should be matched
   stack.append([0,n]) #start at upper right corner
   while len(stack) > 0:
      current = stack.pop()
      i = current[0]
      j = current[1]
      if i >= j:
         continue
      elif opt_score[i+1][j] == opt_score[i][j]: #down one row
         stack.append([i+1, j])
      elif opt_score[i][j-1] == opt_score[i][j]: #left one column
         stack.append([i, j-1])
      elif (opt_score[i+1][j-1] + score(rna[i],rna[j])) == opt_score[i][j]: #left and down diagonally
         visited.append([i,j]) #save base pair
         stack.append([i+1,j-1])
      else:
         for k in range(i+1,j):
            if (opt_score[i][k] + opt_score[k+1][j]) == opt_score[i][j]:
               stack.append([k+1, j])
               stack.append([i, k])
               break
   return visited

def main():
  rna = read_input("input.txt")
  opt_score = create_matrix(len(rna))
  opt_score = populate_matrix(opt_score, rna)
  print("Given RNA sequence:")
  print(rna)
  print("\nNussinov's dynamic programming matrix:")
  print_matrix(opt_score)
  print("\nList of pairings for given RNA sequence:")
  our_pairs = traceback(opt_score, rna)
  print(our_pairs)

main()