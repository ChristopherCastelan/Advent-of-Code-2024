import sys
from collections import defaultdict, Counter
import numpy as np
args = sys.argv[1] if len(sys.argv) >= 2 else 'input4.txt'
File = open(args).read().strip()

L = []
for line in File.split('\n'):
    x = list(line)
    L.append(x)

def FindXMAS(L: list, r: int, c: int) -> int:
    Total = 0
    #Find X and check all directions
    if L[r][c] == 'X':
        for x, y in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
            try:
                #Prevent dropping off the grid by checking if index is not negative
                if L[r + x][c + y] == "M" and r + x >= 0 and c + y >= 0:
                    if L[r+ x + x][c + y + y] == 'A' and r + x + x >= 0 and c + y + y >= 0:
                        if L[r+ x + x + x][c + y + y + y] == 'S' and r + x + x + x >= 0 and c + y + y + y >= 0:
                            Total += 1
            #If Index out of range, pass and check next Direction
            except IndexError:
                pass
    return Total
    
def FindXMASP2(L, r, c):
    Total = 0
    if L[r][c] == 'A':
        Good = False
        for x, y in [(-1, -1)]:
            try: 
                if L[r + x][c + y] == 'M' and r + x >= 0 and c + y >= 0:
                    if L[r + 1][c + 1] == 'S' and r + 1 >= 0 and c + 1 >= 0: 
                        if L[r - 1][c + 1] == 'M' and r - 1 >= 0 and c + 1 >= 0:
                            if L[r + 1][c - 1] == 'S' and r + 1 >= 0 and c - 1 >= 0:
                                Good = True
                        elif L[r - 1][c + 1] == 'S' and r - 1 >= 0 and c + 1 >= 0:
                            if L[r + 1][c - 1] == 'M' and r + 1 >= 0 and c - 1 >= 0:
                                Good = True
                elif L[r + x][c + y] == 'S' and r + x >= 0 and c + y >= 0:
                    if L[r + 1][c + 1] == 'M' and r + 1 >= 0 and c + 1 >= 0:
                        if L[r - 1][c + 1] == 'S' and r - 1 >= 0 and c + 1 >= 0:
                            if L[r + 1][c - 1] == 'M' and r + 1 >= 0 and c - 1 >= 0:
                                Good = True
                        elif L[r - 1][c + 1] == 'M' and r - 1 >= 0 and c + 1 >= 0:
                            if L[r + 1][c - 1] == 'S' and r + 1 >= 0 and c - 1 >= 0:
                                Good = True
                else: 
                    Good = False
            except IndexError:
                break
        if Good: 
            Total += 1
    return Total
        
    
P1_Count = 0
P2_Count = 0
for r, rows in enumerate(L):
    for c, cols in enumerate(rows):
        P1_Count += FindXMAS(L, r, c)
        P2_Count += FindXMASP2(L, r, c)
      
print(P1_Count)        
print(P2_Count)           
