import sys
import re 
args = sys.argv[1] if len(sys.argv) >= 2 else 'input3.txt'
File = open(args).read().strip()

numbers = r'\d+,[0-9]+'
pattern_p2 = r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))'
pattern_p1 = r'mul\(\d+,\d+\)'

p1_regex = re.findall(pattern_p1, File)
p2_regex = re.findall(pattern_p2, File)

def Findtotal(L:list) -> int:
    total = 0
    for line in L:
        p = re.findall(numbers, line)
        j = p[0].split(',')
        t = list(map(int, j))
        total += t[0] * t[1]
    return total
    
do = True
nums = []
for line in p2_regex:
    if re.match(r'don\'t\(\)', line):
        do = False
    elif do or re.match(r'do\(\)', line):
        do = True
        if not re.match(r'do\(\)', line):
            nums.append(line) 
            
print("Part 1: ", Findtotal(p1_regex))
print("Part 2: ", Findtotal(nums))
