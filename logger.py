from __future__ import print_function

def log_result(filename, start_state, start_name, end_state, popped, heuristic=None, log_moves = False, ended_early=False):
  f = open(filename, 'a')
  print("***************************", file=f)
  print("Start State: " + start_name, file=f)
  print(start_state, file=f)
  print("", file=f)

  if log_moves and not ended_early:
    states, moves = end_state.get_path()
    for i in xrange(len(moves)):
      print("Move " + str(i), file = f)
      print(moves[i], file = f)
      print(states[i], file = f)
      print("", file=f)

  if heuristic is not None:
    print("Heuristic Used: " + heuristic.__name__, file=f)
    print(heuristic.__name__, file=f)

  if ended_early:
    print("Had to end early due to taking excessive time, popped states is lower than actual", file = f)
  print("Number of Popped States: " + str(popped), file=f)
  print("***************************", file=f)
  f.close()


