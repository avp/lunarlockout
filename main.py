from astar import run_astar
import heuristics

test_dict1 = {"X": (4,4), "A": (0,0), "B": (2,0), "C": (0,2), "D": (4,0), "E": (0,4)}
test_dict2 = {"X": (4,4), "A": (1,2), "B": (2,1), "C": (3,3), "D": (0,4)}

run_astar(test_dict2, heuristics.manhattan_distance)
#run_astar(test_dict1, heuristics.free_moves_to_center)
