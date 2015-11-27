from astar import run_astar
import heuristics

test_dict = {"X": (4,4), "A": (0,0), "B": (2,0), "C": (0,2), "D": (4,0), "E": (0,4)}

#run_astar(test_dict, heuristics.manhattan_distance)
run_astar(test_dict, heuristics.free_moves_to_center)
