import failclasses
class PointStyle:
    """
    1. style object for class Point()
    2. args:
       keyword values only
       (labeled "**opts")
    """
    def __init__(self,**opts):
        self.valid_opts = ["x","y","bg","label","size"]
        self.configs    = {}
        if opts == {}:
            # defaults
            self.configs["x"]     = 0
            self.configs["y"]     = 0
            self.configs["bg"]    = (0,0,0)
            self.configs["label"] = ""
            self.configs["size"]  = 1
        for i,j in opts:
            if i in self.valid_opts:
                self.configs[i] = j
            else:
                raise WrongConfigError(i)
                break
    def defaults():
        """
        1. resets all style options
           to their default values.
        2. args:
           no args valid.
        
        3. default values:
           * x     = 0
           * y     = 0
           * bg    = (0,0,0) <<in the format (r,g,b)>>
           * label = "" << no default label value>>
           * size  = 1
       
        """
        
        self.configs["x"]     = 0
        self.configs["y"]     = 0
        self.configs["bg"]    = (0,0,0)
        self.configs["label"] = ""
        self.configs["size"]  = 1
        
class Point:
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
