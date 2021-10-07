# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:50:16 2021

@author: olsiv
"""
import numpy as np

def edit_distance(s,t):
    #edit = np.zeros((len(s) + 1, len(t) + 1))
    edit = [[0 for x in range(len(t) + 1)] for x in range(len(s) + 1)]
    #edit[:, 0] = list(range(len(s) + 1))
    #edit[0, :] = list(range(len(t) + 1))
    
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i == 0:
                edit[i][j] = j
            elif j == 0:
                edit[i][j] = i
                
            elif s[i-1] == t[j-1]:
                edit[i][j] = edit[i-1][j-1]
            else:
                insert = edit[i][j-1] + 1
                delete = edit[i-1][j] + 1
                replace = edit[i-1][j-1] + 1 
                edit[i][j] = min(insert,delete,replace)
    return int(edit[len(s)][len(t)])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
                    
            






