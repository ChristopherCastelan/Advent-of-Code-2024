import sys
args = sys.argv[1] if len(sys.argv)>=2 else 'input2.txt'
file = open(args).read().strip()

def Increasing(x: int, y: int) -> int: 
    if int(x) < int(y): 
        return True

def Decreasing(x: int, y: int) -> int: 
    if int(x) > int(y): 
        return True
    
def Difflevel(x: int, y: int):
    t = abs(x - y)
    if 1 <= t <= 3: 
        return True

def Partone(L: list) -> int: 
    Safe_report = 0
    for line in L:
        print(line)
        if Increasing(int(line[0]), int(line[1])): 
            for n in range(len(line)): 
                if n < len(line) - 1:
                    if Decreasing(int(line[n]), int(line[n + 1])):
                        Safe_report += 1
                        print("Unsafe")
                        break
                    else:
                        if Difflevel(int(line[n]), int(line[n + 1])):
                            pass
                        else: 
                            Safe_report += 1
                            print("Unsafe")
                            break
        elif Decreasing(int(line[0]), int(line[1])): 
            for n in range(len(line)): 
                if n < len(line) - 1:
                    if Increasing(int(line[n]), int(line[n + 1])):
                        Safe_report += 1
                        print("Unsafe")
                        break
                    else:
                        if Difflevel(int(line[n]), int(line[n + 1])):
                            pass
                        else: 
                            Safe_report += 1
                            print("Unsafe")
                            break
        else: 
            Safe_report += 1
            print("Unsafe")
    return abs(Safe_report - len(L))  

#Revisting Part Two after reviewing online discussions and forums
def DirectionDiffLevel(L: list):
    # Check whether list is increasing or decreasing via sort check
    Check_dir = (L==sorted(L) or L==sorted(L, reverse=True))
    # Check whether two adjacent elements follow 1<=x<=3 rule
    Check_valid = True 
    for i in range(len(L) - 1):
        if not Difflevel(L[i], L[i + 1]):
            Check_valid = False
    return Check_dir and Check_valid

F = file.split('\n')
     
def Parttwo(L: list) -> int:
    safe_report = 0
    #Check if unsafe report is safe after removing one occurence of invalid rule
    for line in L:
        numbers = list(map(int, line.split())) 
        safe = False
        for t in range(len(numbers)):
        #Slice list into sublists and concatenate sublists for each element to check if unsafe report is safe
            Con_num = numbers[:t] + numbers[t+1:]
            if DirectionDiffLevel(Con_num):
                safe = True
        if safe:
            safe_report += 1
    return safe_report

    
print(Partone(F))
print(Parttwo(F))
                
                


