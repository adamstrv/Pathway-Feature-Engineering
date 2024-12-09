# Apoptosis A

# Import super class
from signaling_entities import SignalingEntities

class ApoptosisA(SignalingEntities):
    def __init__(self, name:str, input:float):
        # Call base class to define name variable
        super().__init__(name)
        # Store input data in variables
        self.inputC = input

    def activate(self, threshold:float=0.1):
        # Activate kinase if C signal breaches threshold

        if self.inputC > threshold:
            self.output = True
        elif not (self.inputC > threshold) and self.inputC > 0:
            self.output = 0
        return self.output