class State:

  def __init__(self, positions, g):
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
    List of moves, where a move is of the form (pod, direction)
    e.g. [("X", "L"), ("A", "D"), ...]
    """
    pass

  def make_move(self, (pod, dir)):
    """
    Returns a new state where the pod has been moved in direction dir.
    REQUIRES: (pod,dir) is a valid move.
    """
    pass

  def is_solved(self):
    """
    Returns true if the game has been solved, i.e. "X" is at position (2,2)
    """
    return self.positions['X'] == (2,2)
