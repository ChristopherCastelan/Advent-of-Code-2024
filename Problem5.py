import sys
from collections import defaultdict, Counter, deque
args = sys.argv[1] if len(sys.argv) >= 2 else 'input5.txt'
File = open(args).read().strip() 

Page = defaultdict(set)
Updates = defaultdict(set)

Total_P1 = 0
Pages, Lines = File.split('\n\n')
for L in Pages.split('\n'): 
    P,U = L.split('|')
    P,U = int(P), int(U)
    Page[U].add(P)
    Updates[P].add(U)

Total_P2 = 0
for t in Lines.split('\n'): 
    query = [int(n) for n in t.split(',')]
    check = True
    for x, a in enumerate(query):
        for y, b in enumerate(query):
            if x<y and b in Page[a]:
                 check = False
    if check:
        Total_P1 += query[len(query)//2]
    #After reviewing online discussions, trying topological sorting - recursively
    else: 
        #List of nodes as they are processed
        visited = []
        #Double-ended queue used to manage the nodes to be processed
        Sorting_nums = deque([])
        #Dictionary mapping each element in t to a count. Count represents how many elements from a set Page[v] intersect with the set t. 
        Nums = {t: len(Page[t] & set(query)) for t in query}
        #This loop iterates over each node t in list query. If the corresponding value in Nums[t] is 0, meaning there are no elements in query that intersect with Pages[t], then t is added to the deque Sorting_nums.
        for t in query:
            if Nums[t] == 0:
                Sorting_nums.append(t)
        #This begins a loop that continues until Q is empty. The node s is popped from the lest side of the deque Sorting_nums. The node s is added to the list visited.
        while Sorting_nums:
            s = Sorting_nums.popleft()
            visited.append(s)
            #If node v in Updates[s], if v is still in Sorting_nums, reduce by 1 until 0. 
            for v in Updates[s]:
                if v in Nums:
                    Nums[v] -= 1
                    if Nums[v] == 0:
                        Sorting_nums.append(v)
        Total_P2 += visited[len(visited)//2]


print(Total_P1)
print(Total_P2)