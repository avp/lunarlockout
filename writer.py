from __future__ import print_function

def writeResultToFile(filename, start_state, popped):
  f = open(filename, 'a')
  print(start_state, file=f)
  print(popped, file=f)


