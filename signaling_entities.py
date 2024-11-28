# Define super class 'signaling entities' to be imported to subclasses

# Import package for abstract class
from abc import ABC, abstractmethod

# Create class for macromolecules entities (make sure that it is an abstract class)
class SignalingEntities(ABC):
    def __init__(self, name:str):
        # Provide name for each signaling entity
        self.name = name
        # Make standard output zero (inactive)
        self.output = 0

    @abstractmethod
    # All macro entities will activate when 'x' is bigger than a certain threshold
    def activate(self):
        """Determine if activation of signaling entity occurs based on 'x' and certain threshold."""
        pass