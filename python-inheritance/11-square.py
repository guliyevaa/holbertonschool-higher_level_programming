def __str__(self):
    """Return the square description [Square] width/height"""
    w = self._Rectangle__width
    h = self._Rectangle__height
    return "[Square] {}/{}".format(w, h)
