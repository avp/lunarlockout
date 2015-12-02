from logger import log_result
from state import State
from collections import deque

def run_bfs(start_dict, start_name):
  start_state = State(start_dict)
  visited = {}
  visited[start_state] = True
  q = deque([start_state])
  q.append(start_state)

  popped = 0
  while len(q) > 0:
    state = q.popleft()
    popped += 1
    if state.is_solved():
      log_result("bfs_results.txt", start_state, start_name, state, popped)
      return
    moves = state.get_moves()
    print(state)
    for move in moves:
      next_state = state.make_move(move)
      if move not in visited:
        q.append(next_state)
        visited[next_state] = True
  print("failed to solve")




