from logger import log_result
from state import State
from collections import deque
import time

def run_bfs(start_dict, start_name):
  print("running bfs")
  start_state = State(start_dict)
  visited = {}
  visited[start_state] = True
  q = deque([start_state])
  q.append(start_state)
  start_time = time.time()
  popped = 0
  while len(q) > 0:
    elapsed_time = time.time() - start_time

    if elapsed_time > 60 * 5:
      log_result("bfs_results.txt", start_state, start_name, state, popped, ended_early = True)
      return popped

    state = q.popleft()
    popped += 1
    if state.is_solved():
      log_result("bfs_results.txt", start_state, start_name, state, popped)
      return popped
    moves = state.get_moves()
    for move in moves:
      next_state = state.make_move(move)
      if move not in visited:
        q.append(next_state)
        visited[next_state] = True
  print("failed to solve bfs!")
