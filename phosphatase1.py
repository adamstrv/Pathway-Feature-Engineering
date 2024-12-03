# Phosphatase, for P1

# Import super class
from signaling_entities import SignalingEntities
# Import math package
import math

class Phosphatase(SignalingEntities):
    def __init__(self, name:str, input:float):
        # Call super class to define name variable
        super().__init__(name)
        # Store input data in variables
        self.input = input

    def activate(self, threshold:float=0.1):
        # Activate phosphatase if K1 signal breaches threshold
        # Because of lower threshold of P1, when K1 is activated, P1 is always activated as well
        if self.input > threshold:
            self.output = 1 / (1 + math.exp(self.input - threshold))
        # Still make case for unactivation to reduce error sensibility
        elif not (self.input > threshold) and self.input > 0:
            self.output = 0
            print("The signal from K1 is not big enough for the phosphotase (1) to breach through to the next signal.")
        return self.output