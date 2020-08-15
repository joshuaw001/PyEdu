class PointStyle(BaseStyle):
    """
    style object for class Point()
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
        resets all style options
        to their default values.
        """
        
        self.configs["x"]     = 0
        self.configs["y"]     = 0
        self.configs["bg"]    = (0,0,0)
        self.configs["label"] = ""
        self.configs["size"]  = 1
        
