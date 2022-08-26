import random
from math import cos,sin,pi

r2=0.70710678118 # 1/sqrt(2)


class QuantumSimulator:
    def __init__(self, quantum_circuit):
        self.circuit = quantum_circuit.circuit
        self.numQubits =  quantum_circuit.numQubits
        self.Bits =  self.numQubits
        self.state_vector = []
    
    def initialize_state_vector(self):
        self.state_vector = [[0.0,0.0] for _ in range(2**self.numQubits)] 
        self.state_vector[0] = [1.0,0.0] 
        print("initialization = ", self.state_vector)

    def superposition(self, x, y):
        '''For two elements of the state_vector, x and y, return (x+y)/sqrt(2) and (x-y)/sqrt(2)'''
        return [[r2*(x[0]+y[0]),r2*(x[1]+y[1])],
                [r2*(x[0]-y[0]),r2*(x[1]-y[1])]]
    
    def turn(self, x, y, theta):
        '''For two elements of the state_vector, x and y, return cos(theta/2)*x - i*sin(theta/2)*y and cos(theta/2)*y - i*sin(theta/2)*x'''
        part1 = [x[0]*cos(theta/2)+y[1]*sin(theta/2),x[1]*cos(theta/2)-y[0]*sin(theta/2)]
        part2 = [y[0]*cos(theta/2)+x[1]*sin(theta/2),y[1]*cos(theta/2)-x[0]*sin(theta/2)]
        return [ part1, part2]
    
    def probability(self, shots):
        probabilities = []
        for index, value in enumerate(self.state_vector): 
            real_part = value[0]
            imaginary_part = value[1]
            probabilities.append(real_part**2+imaginary_part**2)
        output = []
        for shot in range(shots):
            cumu = 0
            un = True
            r = random.random()
            for index, probability in enumerate(probabilities):
                cumu += probability
                if(r < cumu and un):
                    raw_output = "{0:b}".format(index)
                    raw_output = ("0"*(self.numQubits-len(raw_output))) + raw_output
                    output.append(raw_output)
                    un=False

        return output

    def get_counts(self, shots):
        probabilities = self.probability(shots)
        counts = {}
        for element in probabilities:
            if(element in counts):
                counts[element]+=1
            else:
                counts[element]=1
        return counts

    def run(self, shots=1024, format="state_vector"):
        self.initialize_state_vector()
        for gate in self.circuit:         # loop through all gates listed by circuit
            if gate[0] in ['x','h','rx']:
                print("APPLIED GATE:",gate[0], "to", gate[1])
                targetQubit = gate[1]
                for counter_qubit in range(2**targetQubit):
                    for counter_state in range(int(2**(self.numQubits-targetQubit-1))):
                        qb0=counter_qubit+(2**targetQubit+1)*counter_state
                        qb1=qb0+(2**targetQubit)
                        print("before:",self.state_vector)
                        print("qb0:",qb0,"qb1",qb1)

                        
                        if gate[0]=='x':
                            self.state_vector[qb0], self.state_vector[qb1] = self.state_vector[qb1], self.state_vector[qb0]
                            
                        if gate[0]=='h': #condense this if statement with sequence unpacking
                            superpositionResult = self.superposition(self.state_vector[qb0],self.state_vector[qb1])
                            self.state_vector[qb0] = superpositionResult[0]
                            self.state_vector[qb1] = superpositionResult[1]
                            # self.state_vector[qb0], self.state_vector[qb1] = self.superposition(self.state_vector[qb0],self.state_vector[qb1])

                        if gate[0]=='rx':
                            theta = gate[2]
                            turn = self.turn(self.state_vector[qb0],self.state_vector[qb1],theta)
                            self.state_vector[qb0] = turn[0]
                            self.state_vector[qb1] = turn[1]
                        print("after:",self.state_vector)

            elif gate[0] == 'cx':
                control = gate[1]
                target = gate[2]

                [low,high] = sorted([control,target])
         
                for cx0 in range(2**low):
                    limit_cx2 = 2**(high-low-1)
                    for cx1 in range(limit_cx2):
                        for cx2 in range(2**(self.numQubits-high-1)):
                            qb0 = cx0 + 2**(low+1)*cx1 + 2**(high+1)*cx2 + 2**control  
                            qb1 = qb0 + 2**target 
                            self.state_vector[qb0],self.state_vector[qb1] = self.state_vector[qb1],self.state_vector[qb0]
            
        
        if format == "counts":
            return self.get_counts(shots)
        else:
            return self.state_vector
                           
    def __repr__(self):
        return str(self.state_vector)
