# Receptors, for R1 and R2

# Import super class
from signaling_entities import SignalingEntities

class Receptor(SignalingEntities):
    def __init__(self, name: str, input: float):
        # Call super class to define name variable
        super().__init__(name)
        # Store input data in variables
        self.input = input
    
    def activate(self):
        # Activate receptor if there is an input
        if self.input > 0:
            self.output = self.input
        else:
            self.output = 0 
        return self.output