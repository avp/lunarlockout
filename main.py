from astar import run_astar
from bfs import run_bfs
import heuristics

level_39 = {"X": (4,4), "A": (0,0), "B": (2,0), "C": (0,2), "D": (4,0), "E": (0,4)}
level_1 = {"X": (4,4), "A": (1,2), "B": (2,1), "C": (3,3), "D": (0,4)}
level_16 = {"X": (0,2), "A": (0,0), "B": (2,1), "C": (4,1), "D": (2,4)}
level_21 = {"X": (0,2), "A": (1,2), "B": (2,2), "C": (2,4), "D": (3,0), "E": (4,3)}
level_40 = {"X": (4,1), "A": (0,0), "B": (0,2), "C": (0,4), "D": (3,4)}

board_names = ["level 1", "level 16", "level 21", "level 39", "level 40"]
boards = [level_1, level_16, level_21, level_39, level_40]

for i in xrange(len(boards)):
  board = boards[i]
  name = board_names[i]
  if name != "level 39":
    run_bfs(board, name)
  run_astar(board, heuristics.manhattan_distance, name)
  run_astar(board, heuristics.free_moves_to_center, name)
  run_astar(board, heuristics.free_moves2, name)
  run_astar(board, heuristics.free_moves3, name)
