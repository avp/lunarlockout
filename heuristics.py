import math

def manhattan_distance(state):
  current_position = state.get_positions()['X']
  row = current_position[0]
  col = current_position[1]
  return abs(row - 2) + abs(col - 2)

def free_moves_to((row, col), positions):
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
  return int((row != 2) + (col != 2))

def free_moves2(state):
  positions = state.get_positions()
  min_free_moves = 2
  adjs = [(1,2),(3,2),(2,1),(2,3)]
  for (key, (row, col)) in positions.iteritems():
    if key != 'X':
      free_moves = free_moves_to((row, col), adjs)
      min_free_moves = min(min_free_moves, min(free_moves))
  return min_free_moves*10 + free_moves_to_center(state)

def free_moves3(state):
  positions = state.get_positions()
  min_free_moves = 3
  min_pos = None

  adjs = [(1,2),(3,2),(2,1),(2,3)]
  for (key, (row, col)) in positions.iteritems():
    if key != 'X':
      free_moves = free_moves_to((row, col), adjs)
      cur_min = min(free_moves)
      if cur_min < min_free_moves:
        min_free_moves = cur_min
        min_pos = adjs[free_moves.index(min_free_moves)]

  min_free_moves2 = 2
  mx, my = min_pos
  adjs = [(mx-1,my),(mx+1,my),(mx,my-1),(mx,my+1)]
  for (key, (row, col)) in positions.iteritems():
    if key != 'X':
      free_moves = free_moves_to((row, col), adjs)
      min_free_moves2 = min(min_free_moves2, min(free_moves))
  return min_free_moves2*100 + min_free_moves*10 + free_moves_to_center(state)
