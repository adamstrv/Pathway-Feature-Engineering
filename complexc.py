#Complex C

# Import super class
from signaling_entities import SignalingEntities

class ComplexC(SignalingEntities):
    def __init__(self, name:str, input1:float, input2:float):
        # Call base class to define name variable
        super().__init__(name)
        # Store input data in variables
        self.inputK2 = input1
        self.inputK3 = input2
    
    def activate(self, threshold: float = 0.15):
        # Set conditions for activation
        if self.inputK2 > threshold and self.inputK3 > threshold:
            self.output = (self.inputK2,self.inputK3)
            #testing check
            print(self.output)
        # Print error message only when unnecessary
        elif not (self.inputK2 > threshold and self.inputK3 > threshold) and self.inputK2 > 0 and self.inputK3 > 0:
            self.output = 0
            print(f"Error: The values of K2 ({self.inputK2:.2f}) and K3 ({self.inputK3:.2f}) do not both exceed the threshold.")
            print(f"Needs to be a minimal of {threshold:.2f}.")
        return self.output
    