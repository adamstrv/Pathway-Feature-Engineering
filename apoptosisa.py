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
            print(self.output)
        # Print error message only when necessary
        elif not (self.inputC > threshold) and self.inputC > 0:
            self.output = False
            print(self.output)
            print("Error: The signal from C is not big enough for the Apoptose (A) to breach through to the next signal.")
        return self.output