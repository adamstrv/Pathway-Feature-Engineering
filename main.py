# Main code to predict apoptosis occurrence and code signal pathway

# Call all (sub)classes of signaling ententies needed in pathway
from receptors import Receptor
from kinase1 import Kinase1
from phosphatase1 import Phosphatase
from kinase2 import Kinase2
from kinase3 import Kinase3
from complexc import ComplexC
from apoptosisa import ApoptosisA

# Code signal pathway
def simulation(r1:float, r2:float):
    """
    Models a signaling pathway between macromolecular entities. Each element in the pathway contributes a signal of a given 
    strength to the next element, potentially leading to cell apoptosis. The downstream element (apoptosis)
    is only activated if the cumulative signal input exceeds a specific threshold. 
    Determines how every signal received by the receptors (beginning of the pathway) will determine the final 
    cellular apoptosis.  
    Input: external stimuli r1 and r2 (floats)
    Output: occurrence of apoptosis (boolean)
    """
    if not isinstance(r1, (float)) or not isinstance(r2, (float)):
        print('Error: Input type external stimuli must be float')
        return 
    
    else:
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

        # Make case for interaction between K1 and K2
        # Define kinase 2, K2
        K2 = Kinase2(name='K2', input=K1_output)
        # See if K2 is activated and obtain output
        K2_output = K2.activate()
        
        # Make case for interaction between K1 and P1
        # Define phosphatase 1, P1
        P1 = Phosphatase(name='P1', input=K1_output)
        # See if P1 is activated and obtain output
        P1_output = P1.activate()
        
        # Make case for interaction between P1 and K3
        # Define kinase 3, K3
        K3 = Kinase3(name='K3', input=P1_output)
        # See if K3 is activated and obtain output
        K3_output = K3.activate()

        # Make case for interaction between K2, K3 and C
        # Define complex C, C
        C = ComplexC(name='C', input1=K2_output, input2=K3_output)
        # See if C is activated and obtain     
        C_output = C.activate()
        
        # Make case for interaction between C and A
        # Define complex A, A
        A = ApoptosisA(name='A', input=C_output)
        # See if A is activated and obtain   
        A_output = A.activate()
        
        # Make list of outputs to check whether apoptosis will take place
        outputs = [R1_output, R2_output, K1_output, K2_output, K3_output, P1_output, C_output, A_output]
        if 0 in outputs:
            A_output = False
        return A_output


