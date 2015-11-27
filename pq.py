class PriorityQueue(object):

  def __init__(self, f):
    self.pq = []
    self.f = f
    self.fVisited = {}

  def put(self, new_state):
    if new_state in self.fVisited:
      if new_state in self.pq:
        index = self.pq.index(new_state)
        if self.f(self.pq[index]) > self.f(new_state):
          self.fVisited[new_state] = self.f(new_state)
    else:
      insertion_index = len(self.pq)
      for index, state in enumerate(self.pq):
        new_f = self.f(new_state)
        old_f = self.f(state)
        if (new_f < old_f):
          insertion_index = index
          break
      self.pq.insert(insertion_index, new_state)
      self.fVisited[new_state] = self.f(new_state)

  def empty(self):
    return len(self.pq) == 0

  def get(self):
    return self.pq.pop(0)
