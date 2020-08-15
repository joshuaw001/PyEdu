class PointAdditionError(Exception):
    def __init__(self, a, b):
        self.message = f"can't apply {a} and {b} into a set"
        super().__init__(self.message)

class PointSubtractionError(Exception):
    def __init__(self, a, b):
        self.message = f"can't calculate distance from {a} to {b}"
        super().__init__(self.message)
