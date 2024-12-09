# Kinase, for K2

# Import super class
from signaling_entities import SignalingEntities

class Kinase2(SignalingEntities):
    def __init__(self, name:str, input:float):
        # Call base class to define name variable
        super().__init__(name)
        # Store input data in variables
        self.input = input

    def activate(self, threshold:float=0.2):
        # Activate kinase if K1 signal breaches threshold
 
        if self.input > threshold:
            self.output = self.input + threshold
        elif (self.input < threshold) and self.input > 0:
            self.output = 0
        return self.output