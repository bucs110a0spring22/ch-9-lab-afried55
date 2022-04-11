from Rectangle import Rectangle
class Surface:
  def __init__(self, filename = '', x=0, y=0, h=0, w=0):
     '''This function initializes a Surface object
    args: self, filename (str), x (int), y (int), h (int), w (int)'''
     self.image = filename
     self.rect = Rectangle(x,y,h,w)
  def getRect(self):
    '''This function returns self.rect of the Surface object
    args: self (Surface object)
    returns: self.rect (Rectangle object)'''
    return self.rect
     