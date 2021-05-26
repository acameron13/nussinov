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

#traceback to fill pair list
def traceback(mat, rna):
  i = 0
  j = len(mat) - 1
  P = traceback_helper(i, j, mat, rna)
  return P

def traceback_helper(i, j, mat, rna):
  P = []
  if (i > -1):
    while j>i:
      if mat[i][j] == mat[i][j-1]:
        j = j - 1
      else:
        for k in range(i, j):
          if (score(rna[k],rna[j]) == 1):
            if (mat[i][j] == mat[i][k-1] + mat[k+1][j-1] +1):
                P.append([k,j])
                P1 = traceback_helper(i, k -1, mat, rna)
                P2 = traceback_helper(k+1, j-1, mat, rna)
                P = P + P1 + P2
  return P

def main():
  rna = read_input("input.txt")
  opt_score = create_matrix(len(rna))
  opt_score = populate_matrix(opt_score, rna)
  print_matrix(opt_score)
  our_pairs = traceback(opt_score, rna)
  print(our_pairs)

main()
