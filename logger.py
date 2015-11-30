from __future__ import print_function

def log_result(filename, start_state, end_state, popped, heuristic, log_moves = False):
  f = open(filename, 'a')
  print("***************************", file=f)
  print("Start State:", file=f)
  print(start_state, file=f)
  print("", file=f)

  if log_moves:
    states, moves = end_state.get_path()
    for i in xrange(len(moves)):
      print("Move " + str(i), file = f)
      print(moves[i], file = f)
      print(states[i], file = f)
      print("", file=f)

  print("Heuristic Used: " + heuristic.__name__, file=f)
  print(heuristic.__name__, file=f)
  print("Number of Popped States: " + str(popped), file=f)
  print("***************************", file=f)
  f.close()


