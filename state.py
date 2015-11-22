class State:

  def __init__(self, positions, g=0):
    """
    Positions: Dictionary mapping strings ("X", "A", etc) to tuples (row,col).
    e.g. {"X": (0,0), "Y": (2,2), ...}
    """
    self.positions = positions
    self.g = g

  def get_positions(self):
    """
    Returns dictionary of pods to positions tuple
    """
    return self.positions

  def get_g(self):
    """
    Returns number of moves to this state
    """
    return self.g

  def __eq__(self, other):
    return (
        isinstance(other, self.__class__) and
        self.positions == other.get_positions()
        )

  def __ne__(self, other):
    return not self.__eq__(other)

  def get_moves(self):
    """
    Returns:
    List of moves, where a move is of the form (pod, pos)
    e.g. [("X", (0,1)), ("A", (2,0)), ...]
    """
    DELTAS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    occupied = set(self.positions.values())
    def can_move(pod, dir):
      (dr,dc) = DELTAS[dir]
      (r0,c0) = self.positions[pod]
      for i in xrange(2, 5): # Start at 2 because not moving is pointless
        (r,c) = (r0 + i*dr, c0 + i*dc)
        if r < 0 or r > 4 or c < 0 or c > 4:
          return None
        if (r,c) in occupied:
          return (r-dr,c-dc)
      return None

    moves = []
    for pod in ('X', 'A', 'B', 'C', 'D', 'E'):
      for dir in ('U', 'D', 'L', 'R'):
        move = can_move(pod, dir)
        if move:
          moves.append(move)
    return moves

  def make_move(self, (pod, pos)):
    """
    Returns a NEW state where the pod has been moved in direction dir.
    REQUIRES: (pod,dir) is a valid move.
    """
    positions = {}
    for a, b in self.positions.iteritems():
      if pod == a:
        positions[a] = pos
      else:
        positions[a] = b
    return State(positions, self.g + 1)

  def is_solved(self):
    """
    Returns true if the game has been solved, i.e. "X" is at position (2,2)
    """
    return self.positions['X'] == (2,2)
