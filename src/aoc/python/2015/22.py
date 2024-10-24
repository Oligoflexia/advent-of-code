from python.utils.input_handler import get_input
import copy

input = get_input(2015, 22)

options = { 'M': {'cost': 53, 'dmg': 4},
            'D': {'cost': 73, 'dmg': 2, 'heal': 2},
            'S': {'cost': 113, 'dmg': 0, 'shield': 7},
            'P': {'cost': 173, 'dmg': 0, 'poison': True},
            'R': {'cost': 229, 'dmg': 0, 'mana': 101} }

b_hp = int(input.splitlines()[0][-2:])
b_dmg = int(input.splitlines()[1].split(" ")[-1])

states = { "": {'p_hp': 50, 
                'p_mana': 500, 
                'b_hp': b_hp,
                'spent_mana': 0, 
                'shield': [7, 0], 
                'regen': [101, 0], 
                'poisoned': [3, 0], 
                'next_options': ['M', 'D', 'S', 'P', 'R']}}

# lookup table? 
# save each node as a dict {recharge,blast: {b_hp: 10,,, etc}}
# create greedy path with permutation? 
# cheapest -> most expensive
def do_magic(state_dict:dict, next_move:str):
    global options
    
    match next_move:
        case 'M':
            state_dict['b_hp'] -= options['M']['dmg']
            state_dict['p_mana'] -= options['M']['cost']
            state_dict['spent_mana'] += options['M']['cost']
        case 'D':
            state_dict['b_hp'] -= options['D']['dmg']
            state_dict['p_hp'] += options['D']['heal']
            state_dict['p_mana'] -= options['D']['cost']
            state_dict['spent_mana'] += options['D']['cost']
        case 'S':
            state_dict['shield'] = [7, 6]
            state_dict['p_mana'] -= options['S']['cost']
            state_dict['spent_mana'] += options['S']['cost']
        case 'P':
            state_dict['poisoned'] = [3, 6]
            state_dict['p_mana'] -= options['P']['cost']
            state_dict['spent_mana'] += options['P']['cost']
        case 'R':
            state_dict['regen'] = [101, 5]
            state_dict['p_mana'] -= options['R']['cost']
            state_dict['spent_mana'] += options['R']['cost']

def determine_actions(state_dict:dict) -> list[str]:
    all_options = ['M', 'D', 'S', 'P', 'R']
    
    mana = state_dict['p_mana']
    
    if state_dict['regen'][1] > 0:
        mana += 101
    
    if mana < 229 or state_dict['regen'][1] > 1:
        all_options.remove('R')
    if mana < 173 or state_dict['poisoned'][1] > 1:
        all_options.remove('P')
    if mana < 113 or state_dict['shield'][1] > 1:
        all_options.remove('S')
    if mana < 73:
        all_options.remove('D')
    if mana < 53:
        all_options.remove('M')
    
    return all_options

def simulate_round(cur_state:str, next_move:str) -> dict:
    global states 
    state_conditions = copy.deepcopy(states[cur_state])
    new_options = []
    
    state_conditions['p_hp'] -= 1
    
    if state_conditions['p_hp'] <= 0:
        return {cur_state+next_move: {'p_hp': state_conditions['p_hp'], 
                'p_mana': state_conditions['p_mana'], 
                'b_hp': state_conditions['b_hp'],
                'spent_mana': state_conditions['spent_mana'], 
                'shield': state_conditions['shield'], 
                'regen': state_conditions['regen'], 
                'poisoned': state_conditions['poisoned'], 
                'next_options': new_options}}
    
    if state_conditions['regen'][1] > 0:
        state_conditions['p_mana'] += state_conditions['regen'][0]
        state_conditions['regen'][1] -= 1
    
    if state_conditions['shield'][1] > 0:
        state_conditions['shield'][1] -= 1
        
    if state_conditions['poisoned'][1] > 0:
        state_conditions['b_hp'] -= state_conditions['poisoned'][0]
        state_conditions['poisoned'][1] -= 1
        
    if state_conditions['b_hp'] <= 0:
        return {cur_state+next_move: {'p_hp': state_conditions['p_hp'], 
                'p_mana': state_conditions['p_mana'], 
                'b_hp': state_conditions['b_hp'],
                'spent_mana': state_conditions['spent_mana'], 
                'shield': state_conditions['shield'], 
                'regen': state_conditions['regen'], 
                'poisoned': state_conditions['poisoned'], 
                'next_options': new_options}}
    
    do_magic(state_conditions, next_move)
    
    if state_conditions['b_hp'] <= 0:
        return {cur_state+next_move: {'p_hp': state_conditions['p_hp'], 
                'p_mana': state_conditions['p_mana'], 
                'b_hp': state_conditions['b_hp'],
                'spent_mana': state_conditions['spent_mana'], 
                'shield': state_conditions['shield'], 
                'regen': state_conditions['regen'], 
                'poisoned': state_conditions['poisoned'], 
                'next_options': new_options}}
    
    if state_conditions['regen'][1] > 0:
        state_conditions['p_mana'] += state_conditions['regen'][0]
        state_conditions['regen'][1] -= 1
        
    if state_conditions['poisoned'][1] > 0:
        state_conditions['b_hp'] -= state_conditions['poisoned'][0]
        state_conditions['poisoned'][1] -= 1
        
    if state_conditions['b_hp'] <= 0:
        return {cur_state+next_move: {'p_hp': state_conditions['p_hp'], 
                'p_mana': state_conditions['p_mana'], 
                'b_hp': state_conditions['b_hp'],
                'spent_mana': state_conditions['spent_mana'], 
                'shield': state_conditions['shield'], 
                'regen': state_conditions['regen'], 
                'poisoned': state_conditions['poisoned'], 
                'next_options': new_options}}
    
    global b_dmg
    
    if state_conditions['shield'][1] > 0:
        if b_dmg - 7 <= 0:
            state_conditions['p_hp'] -= 1
        else: 
            state_conditions['p_hp'] -= b_dmg - 7
        state_conditions['shield'][1] -= 1
    else:
        state_conditions['p_hp'] -= b_dmg
    
    new_options = determine_actions(state_conditions)
    
    state_conditions['next_options'] = new_options
    
    return {cur_state+next_move: {'p_hp': state_conditions['p_hp'], 
                'p_mana': state_conditions['p_mana'], 
                'b_hp': state_conditions['b_hp'],
                'spent_mana': state_conditions['spent_mana'], 
                'shield': state_conditions['shield'], 
                'regen': state_conditions['regen'], 
                'poisoned': state_conditions['poisoned'], 
                'next_options': new_options}}

def is_loss(state_dict):
    print(state_dict)
    dic = [i for i in state_dict.values()][0]
    if dic['p_hp'] <= 0 or len(dic['next_options']) == 0:
        return True
    else:
        False

def is_win(state_dict):
    dic = [i for i in state_dict.values()][0]
    if dic['b_hp'] <= 0:
        return True
    else:
        return False

def greedy_bfs_w_pruning():
    global states
    
    lowest_score = float('inf')
    
    solved_state = {}
    
    round = 0
    
    while len([key for key in states if len(key) == round]) > 0:
        for element in [key for key in states if len(key) == round]:
            for option in states[element]['next_options']:
                new_state = simulate_round(element, option)
                if is_win(new_state):
                    if lowest_score > new_state[element+option]['spent_mana']:
                        lowest_score = new_state[element+option]['spent_mana']
                        solved_state = new_state
                elif is_loss(new_state):
                    pass
                elif [i for i in new_state.values()][0]['spent_mana'] > lowest_score:
                        pass
                else:
                    states[[i for i in new_state.keys()][0]] = [i for i in new_state.values()][0]
        round += 1
    return lowest_score, solved_state

print(greedy_bfs_w_pruning())

