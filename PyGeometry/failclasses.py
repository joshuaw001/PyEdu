class WrongConfigError(Exception):
    def __init__(self,name):
        self.name = name
        self.message = "configured option named {self.name} doesn't exist."
        super().__init__(self.message)
