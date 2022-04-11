class Rectangle:
  def __init__(self, x=0, y=0, h=0, w=0):
    '''This function initializes a Rectangle object
    args: self, x (int), y (int), h (int), w (int)'''
    if x <0:
      x = 0
    if y <0:
      y = 0
    if h <0:
      h=0
    if w <0:
      w = 0
    self.x = x
    self.y = y
    self.height = h
    self.width = w
  def __str__(self):
    '''Determines the string of a Rectangle object
    args: self (Rectangle object)
    returns: str'''
    return  f"(x : {self.x}, y: {self.y}) width: {self.width}, height: {self.height}"