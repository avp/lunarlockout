from pq import PriorityQueue
from writer import writeResultToFile

def runAStar(start_dict, h):

  def get_f(state):
    return h(state) + state.get_g()

  start_state = State(start_dict)
  q = PriorityQueue(get_f)
  q.put(start_state)

  popped = 0
  while not q.empty():
    state = q.get()
    popped += 1
    if state.is_solved():
      print("found answer")
      print(popped)
      writeResultToFile("astar_results.txt", start_state, popped)
      return
    moves = state.get_moves()
    for move in moves:
      q.put(state.make_move(move))




