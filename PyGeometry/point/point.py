class Point(Component):
    def __init__(self,stylesettings=PointStyle()):
        self.settings = stylesettings
        self.coords   = []
        self.coords  += self.settings.configs["x"]
        self.coords  += self.settings.configs["y"]
    def __sub__(self,other):
        if type(other) == "<class '__main__.Point'>":
            return math.sqrt(((other.coords[0] - self.coords[0])**2)+((other.coords[1] - self.coords[1])**2))
        else:
            raise PointSubtractionError()
    def __add__(self,other):
        if type(other) == "<class '__main__.Point'>":
            return math.sqrt(((other.coords[0] - self.coords[0])**2)+((other.coords[1] - self.coords[1])**2))
        else:
            raise PointAdditionError()
