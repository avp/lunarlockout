from astar import run_astar
from bfs import run_bfs
import heuristics

hard_dict = {"X": (4,4), "A": (0,0), "B": (2,0), "C": (0,2), "D": (4,0), "E": (0,4)}
easy_dict = {"X": (4,4), "A": (1,2), "B": (2,1), "C": (3,3), "D": (0,4)}
med_dict = {"X": (0,2), "A": (0,0), "B": (2,1), "C": (4,1), "D": (2,4)}

#run_astar(easy_dict, heuristics.manhattan_distance)
run_astar(med_dict, heuristics.free_moves_to_center, "medium level")
run_astar(med_dict, heuristics.manhattan_distance, "medium level")
run_astar(med_dict, heuristics.free_moves_part_two, "medium level")
#run_bfs(med_dict, "medium level")
