#Pierce McDonnell, Molly Kammann, and Alison Cameron
#Nussinov's Algorithm
#CS252

import sys
import math
import numpy
import pandas

#Read in the input
def read_input(filename):
  nucleotides = []
  with open(filename, "r") as input_file:
    rna_strand = input_file.readline()
  
  for ch in rna_strand:
    #Check if input is valid
    if ch in ["A", "C", "G", "U"]:
      nucleotides.append(ch)
    else:
      sys.exit("Input is not valid")
      
  return nucleotides

#Initializing the Matrix
def create_matrix(n):
  opt_score = []
  for i in range(n):
    scores_i = []
    for j in range(n):
      scores_i.append(None)
    opt_score.append(scores_i)
  
  for i in range(n):
    opt_score[i][i] = 0
    if i >= 1:
      opt_score[i][i-1] = 0

  return opt_score

#Filling in the Matrix

#Display Matrix neatly
def print_matrix(mat):
  opt_score_array = np.array(mat)
  print(opt_score_array)


def main():
  rna = read_input("input.txt")
  opt_score = create_matrix(len(rna))
  print_matrix(opt_score)
  #print pandas.DataFrame(opt_score)
  
main()
