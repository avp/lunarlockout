from __future__ import print_function

def log_result(filename, start_state, popped, heuristic):
  print("logged")
  f = open(filename, 'a')
  print(start_state, file=f)
  print(heuristic.__name__, file=f)
  print(popped, file=f)
  f.close()


