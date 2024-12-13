import sys 
from collections import defaultdict
args = sys.argv[1] if len(sys.argv) >= 2 else 'input6.txt'
File = open(args).read().strip()

Route = []
for Lines in File.split('\n'):
    t = list(Lines)
    Route.append(t)

start_x, start_y = (0, 0)
for x, rows in enumerate(Route):
    for y, cols in enumerate(rows):
        if Route[x][y] == "^":
            start_x, start_y = x, y
            Visited = set()
            Visited.add((x, y))
            Route[x][y] = '.'
            Change = 0
            while x >= 0 and y >= 0 and x < len(Route) and y < len(Route[x]):
                Coordinate = (x, y)
                if Coordinate not in Visited:
                    Visited.add(Coordinate)
                try:
                    Directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    Moving_direction = Directions[Change]   
                    if Route[x + Moving_direction[0]][y + Moving_direction[1]] == '.':
                        x = x + Moving_direction[0]
                        y = y + Moving_direction[1]
                    elif Route[x + Moving_direction[0]][y + Moving_direction[1]] == '#':
                        if Moving_direction == Directions[3]:
                            Change = 0
                        else:
                            Change += 1
                except IndexError:
                    break

P2_Count = 0
for i, t in Visited:
    Route[i][t] = '#'
    Route[start_x][start_y] = "^"
    for nums, rowss in enumerate(Route):
        for lines, cols in enumerate(rowss):
            if Route[nums][lines] == "^":
                Route[nums][lines] = '.'
                Change = 0
                SEEN_Loop = set()
                while nums >= 0 and lines >= 0 and nums < len(Route) and lines < len(Route[nums]):
                    #print(i, t, nums, lines, Change)
                    Coordinate = (nums, lines, Change)
                    if Coordinate not in SEEN_Loop:
                        SEEN_Loop.add(Coordinate)
                    else:
                        P2_Count += 1
                        break
                    try:
                        Directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                        Moving_direction = Directions[Change]   
                        if Route[nums + Moving_direction[0]][lines + Moving_direction[1]] == '.':
                            nums = nums + Moving_direction[0]
                            lines = lines + Moving_direction[1]
                        elif Route[nums + Moving_direction[0]][lines + Moving_direction[1]] == '#':
                            if Moving_direction == Directions[3]:
                                Change = 0
                            else:
                                Change += 1
                    except IndexError:
                        break
    Route[i][t] = "."

print("P1:", len(Visited))        
print("P2:", P2_Count)