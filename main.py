from astar import run_astar
from bfs import run_bfs
import heuristics

level_1 = {"X": (4,4), "A": (1,2), "B": (2,1), "C": (3,3), "D": (0,4)}
level_15 = {"X": (4,4), "A": (1,1), "B": (0,4), "C": (2,4), "D": (3,2)}
level_16 = {"X": (0,2), "A": (0,0), "B": (2,1), "C": (4,1), "D": (2,4)}
level_17 = {"X": (4,1), "A": (2,1), "B": (0,2), "C": (0,4), "D": (3,3)}
level_18 = {"X": (0,2), "B": (4,0), "C": (4,2), "D": (4,4)}
level_19 = {"X": (4,4), "B": (0,1), "C": (1,2), "D": (2,3), "E": (3,0), "F": (4,2)}
level_20 = {"X": (3,3), "B": (0,1), "C": (1,4), "D": (2,0), "E": (4,1)}
level_21 = {"X": (0,2), "A": (1,2), "B": (2,2), "C": (2,4), "D": (3,0), "E": (4,3)}
level_22 = {"X": (4,4), "A": (4,0), "B": (1,0), "C": (1,4), "D": (3,3)}
level_23 = {"X": (4,1), "A": (0,1), "B": (1,0), "C": (1,3), "D": (3,4)}
level_24 = {"X": (4,0), "A": (1,3), "B": (2,1), "C": (4,3), "D": (4,4)}
level_25 = {"X": (4,1), "A": (1,0), "B": (1,2), "C": (1,3), "D": (4,4)}
level_26 = {"X": (0,2), "A": (0,0), "B": (2,0), "C": (1,4), "D": (3,3)}
level_27 = {"X": (4,4), "A": (0,1), "B": (0,4), "C": (2,0), "D": (4,0), "E": (2,3)}
level_28 = {"X": (4,4), "A": (3,0), "B": (0,1), "C": (0,4), "D": (2,4)}
level_29 = {"X": (0,2), "A": (0,0), "B": (0,4), "C": (4,0), "D": (4,4)}
level_30 = {"X": (0,2), "A": (1,0), "B": (1,4), "C": (2,0), "D": (4,1), "E": (4,3)}
level_31 = {"X": (3,3), "A": (0,0), "B": (0,2), "C": (1,4), "D": (2,0), "E": (4,1)}
level_32 = {"X": (4,1), "A": (0,1), "B": (1,4), "C": (4,0), "D": (4,2)}
level_33 = {"X": (4,4), "A": (0,0), "B": (0,1), "C": (1,4), "D": (3,0), "E": (4,3)}
level_34 = {"X": (4,4), "A": (0,2), "B": (0,4), "C": (2,0), "D": (4,0), "E": (3,3)}
level_35 = {"X": (0,2), "A": (0,0), "B": (0,4), "C": (4,0), "D": (4,4), "E": (1,2)}
level_36 = {"X": (0,2), "A": (1,0), "B": (1,4), "C": (3,0), "D": (3,4), "E": (4,2)}
level_37 = {"X": (3,3), "A": (0,0), "B": (0,3), "C": (0,4), "D": (3,0)}
level_38 = {"X": (4,1), "A": (2,0), "B": (2,1), "C": (0,4), "D": (0,2), "E": (4,4)}
level_39 = {"X": (4,4), "A": (0,0), "B": (2,0), "C": (0,2), "D": (4,0), "E": (0,4)}
level_40 = {"X": (4,1), "A": (0,0), "B": (0,2), "C": (0,4), "D": (3,4)}

board_names = ["level 1"] + ["level " + str(i) for i in range(15,41)]
boards = [level_1, level_15, level_16, level_17, level_18, level_19, level_20,
          level_21, level_22, level_23, level_24, level_25, level_26,
          level_27, level_28, level_29, level_30, level_31, level_32,
          level_33, level_34, level_35, level_36, level_37, level_38,
          level_39, level_40]

bfs_pops = 0
manhattan_distance_pops = 0
free_moves_to_center_pops = 0
free_moves2_pops = 0
free_moves3_pops = 0
for i in xrange(len(boards)):
  board = boards[i]
  name = board_names[i]
  print("solving board " + name)
  bfs_pops += run_bfs(board, name)
  manhattan_distance_pops += run_astar(board, heuristics.manhattan_distance, name)
  free_moves_to_center_pops += run_astar(board, heuristics.free_moves_to_center, name)
  free_moves2_pops += run_astar(board, heuristics.free_moves2, name)
  free_moves3_pops += run_astar(board, heuristics.free_moves3, name)


n = len(board_names)
print("bfs average: " + str(bfs_pops / n))
print("manhattan average: " + str(manhattan_distance_pops / n))
print("free moves to center average: " + str(free_moves_to_center_pops / n))
print("free moves 2 average: " + str(free_moves2_pops / n))
print("free moves 3 average: " + str(free_moves3_pops / n))
