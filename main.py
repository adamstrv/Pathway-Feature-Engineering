# Main code to predict apoptosis occurrence and code signal pathway

# Call all (sub)classes of signaling ententies needed in pathway
from receptors import Receptor
from kinase1 import Kinase1
from phosphatase1 import Phosphatase
from kinase2 import Kinase2

# Code signal pathway
def simulation(r1, r2):
    """
    Models a signaling pathway between macromolecular entities. Each element in the pathway contributes a signal of a given 
    strength to the next element, potentially leading to cell apoptosis. The downstream element (apoptosis)
    is only activated if the cumulative signal input exceeds a specific threshold. 
    Determines how every signal received by the receptors (beginning of the pathway) will determine the final 
    cellular apoptosis.  
    Input: external stimuli r1 and r2 (floats)
    Output: occurrence of apoptosis (boolean)
    """
    # Make case for interaction between R1 and R2 receptors and input stimuli 
    # Define receptor 1 and 2
    R1 = Receptor(name='R1', input = r1)
    R2 = Receptor(name='R2', input = r2)

    # See if R1 and R2 are activated and obtain their outputs
    R1_output = R1.activate()
    R2_output = R2.activate()
    # Print error message if R1 and R2 are =< 0
    if R1_output <= 0:
        print("Error: Unvalid input stimulation provided for R1")
    if R2_output <= 0:
        print("Error: Unvalid input stimulation provided for R2")

    # Make case for interaction between R1, R2 and K1
    # Define kinase 1, K1
    K1 = Kinase1(name='K1', input1=R1_output, input2=R2_output)
    # See if K1 is activated and obtain output
    K1_output = K1.activate()

    # Make case for interaction between K1 and P1
    # Define phosphatase 1, P1
    P1 = Phosphatase(name='P1', input=K1_output)
    # See if P1 is activated and obtain output
    P1_output = P1.activate()

    # Make case for interaction between K1 and K2
    # Define kinase 2, K2
    K2 = Kinase2(name='K2', input=K1_output)
    # See if K2 is activated and obtain output
    K2_output = K2.activate()


simulation(0.6, 0.6)

