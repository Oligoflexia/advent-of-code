from utils.get_input import get_input

input = get_input(2015, 18)

grid = []
scores = [[0] * 100 for _ in range(100)]

def init_grid():
    for line in input.splitlines():
        row = []
        for char in line:
            if char == '#':
                row.append(1)
            else:
                row.append(0)
        grid.append(row)

# for row in grid:
#     print("".join([str(i) for i in row]))

def calculate_scores():
    for r_ind, row in enumerate(grid):
        for e_ind in range(len(row)):
            e_score = 0
            
            coords = [(r_ind - 1, e_ind - 1), (r_ind - 1, e_ind), (r_ind - 1, e_ind + 1),
                      (r_ind, e_ind - 1), (r_ind, e_ind + 1),
                      (r_ind + 1, e_ind - 1), (r_ind + 1, e_ind), (r_ind + 1, e_ind + 1)]
            
            for coord in coords:
                if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(row):
                        e_score += grid[coord[0]][coord[1]]
            
            scores[r_ind][e_ind] = e_score

# for row in scores:
#     print("".join([str(i) for i in row]))

def flip_switches():
    for r_ind, row in enumerate(grid):
        for e_ind, element in enumerate(row):
            if element == 1:
                if scores[r_ind][e_ind] not in (2, 3):
                    grid[r_ind][e_ind] = 0
            else:
                if scores[r_ind][e_ind] == 3:
                    grid[r_ind][e_ind] = 1

def solve(n:int) -> int:
    cumm_sum = 0
    
    init_grid()
    
    for _ in range(n):
        calculate_scores()
        flip_switches()
    
    for row in grid:
        cumm_sum += sum(row)
    
    return cumm_sum

answer = solve(100)

print(f"There are {answer} lights on after 100 iterations.")

grid = []

def broken_solve(n:int) -> int:
    cumm_sum = 0
    
    init_grid()
    
    for _ in range(n):
        grid[0][0] = 1
        grid[0][99] = 1 
        grid[99][0] = 1
        grid[99][99] = 1
        
        calculate_scores()
        flip_switches()
        
        grid[0][0] = 1
        grid[0][99] = 1 
        grid[99][0] = 1
        grid[99][99] = 1
        
    for row in grid:
        cumm_sum += sum(row)
    
    return cumm_sum

new_answer = broken_solve(100)

print(f"There are {new_answer} lights on after 100 iterations using the broken lights.")