from python.utils.input_handler import get_input

input = get_input(2015, 14)

reindeer_stats = {}

for line in input.splitlines():
    data = [line.split(" ")[i] for i in [0, 3, 6, 13]]
    
    reindeer_stats[data[0]] = {
        'rate' : int(data[1]),
        'move_time' : int(data[2]),
        'rest_time' : int(data[3]),
        'total_d' : int(data[1]) * int(data[2]),
        'total_t' : int(data[2]) + int(data[3]),
    }

# for deer in reindeer_stats:
#     total_d = reindeer_stats[deer]['total_d']
#     total_t = reindeer_stats[deer]['total_t']
    
#     print(f"{deer} can travel {total_d}km every {total_t}s (including rest time)!")
    
def calc_d(reindeer:str, time:int) -> int:
    total_d = 0
    total_t = reindeer_stats[reindeer]['total_t']
    cycle_d = reindeer_stats[reindeer]['total_d']
    
    full_cycles = int(time / total_t)
    remaining_s = int(time % total_t)
    
    total_d += full_cycles * cycle_d
    
    if reindeer_stats[reindeer]['move_time'] - remaining_s < 0:
        total_d += cycle_d
    else:
        total_d += remaining_s * reindeer_stats[reindeer]['rate']
    
    return total_d

def fastest_deer(statbook:dict, time:int) -> (str, int):
    max_d = float('-inf')
    best = [None, None]
    
    for deer in reindeer_stats:
        d = calc_d(deer, time)
        
        if d > max_d:
            max_d = d
            best[0], best[1] = deer, d
            
    return tuple(best)

contest_time = 2503
result = fastest_deer(reindeer_stats, contest_time)

print(f"The fastest deer was: {result[0]}, travelling {result[1]}km in {contest_time}s!")
        
def new_fastest_deer(statbook:dict, time:int) -> (str, int):
    distances = [[0] * len(statbook.keys()) for _ in range(time +1)]
    points = [0] * len(statbook.keys())
    
    for i, deer in enumerate(reindeer_stats):
        for t in range(time+1):
            d = calc_d(deer, t)
            distances[t][i] = d
    
    for row in distances:
         max_v = max(row)
         max_i = [i for i, j in enumerate(row) if j == max_v]
         
         for i in max_i:
             points[i] += 1 
    
    return (list(statbook.keys())[points.index(max(points))], max(points))
    
new_result = new_fastest_deer(reindeer_stats, contest_time)
print(f"With the new rules, the winner of the contest is {new_result[0]} with {new_result[1]-1} points!")