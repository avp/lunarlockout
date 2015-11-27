import math

def manhattan_distance(state):
    current_position = state.get_positions()['X']
    row = current_position[0]
    col = current_position[1]
    return abs(row - 2) + abs(col - 2)

def free_moves_to(row, col, positions):
    num_free_moves = []

    for position in positions:
        free_moves = 0
        if row != position[0]:
            free_moves += 1
        if col != position[1]:
            free_moves += 1
        num_free_moves.append(free_moves)

    return num_free_moves


def free_moves_to_center(state):
    current_position = state.get_positions()['X']
    row = current_position[0]
    col = current_position[1]
    return free_moves_to(row, col, [(2,2)])[0]

def free_moves_part_two(state):
    positions = state.get_positions()
    min_free_moves = 2

    for key in positions:
        if key != 'X':
            row = positions[key][0]
            col = positions[key][1]
            free_moves = free_moves_to(row, col, [(1,2),(3,2),(2,1),(2,3)])
            for move in free_moves:
                if move < min_free_moves:
                    min_free_moves = move

    return min_free_moves + free_moves_to_center(state)




