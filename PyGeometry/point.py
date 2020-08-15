class PointStyle:
    def __init__(self,**opts):
        self.valid_opts = ["x","y","bg","label","size"]
        self.configs    = {}
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
    pass
