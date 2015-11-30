from pq import PriorityQueue
from logger import log_result
from state import State

def run_astar(start_dict, h):

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
      log_result("astar_results.txt", start_state, state, popped, h)
      return
    moves = state.get_moves()
    print(state)
    print(h(state))
    for move in moves:
      q.put(state.make_move(move))
  print("failed to solve")




