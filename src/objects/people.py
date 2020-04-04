import numpy as np

class boy:

    def __init__(self, _age):
        self.age = _age
        self.age_np = np.array([self.age]*10)

    def get_age(self):
        return self.age
