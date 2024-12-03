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
        min_input = min(self.inputK2, self.inputK3)
        if min_input > threshold:
            self.output = min_input

        # Print error message only when necessary
        elif not (min_input > threshold) and self.inputK2 > 0 and self.inputK3 > 0:
            self.output = 0
            print(f"The values of K2 ({self.inputK2:.2f}) and K3 ({self.inputK3:.2f}) do not both exceed the threshold.")
            print(f"One of the two inputs needs to exceed {threshold:.2f}.")
        return self.output
    