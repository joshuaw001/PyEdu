class WrongConfigError(Exception):
    def __init__(self,name):
        self.name = name
        self.message = "configured option named {self.name} doesn't exist."
        super().__init__(self.message)
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
        zxdrg 
