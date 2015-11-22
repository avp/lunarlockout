class State:

  def __init__(self, positions):
    """
    Positions: Dictionary mapping strings ("X", "A", etc) to tuples (row,col).
    e.g. {"X": (0,0), "Y": (2,2), ...}
    """
    pass

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
    pass
