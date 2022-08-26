from math import cos,sin,pi




class QuantumCircuit:
    def __init__(self, numQubits):  #numQubits(int): number of numQubits
        if (numQubits == 0):
            print('Number of Qubits need to be more than 0')
        self.numQubits = numQubits
        self.Bits = numQubits   # redundant, delete after explore
        self.circuit = []        # a list of lists([gate_name, target_qubit] or [gate_name, target_qubit, theta])
    
    def add_gate(self, gate):
        self.circuit.append(gate)
    
    def x(self, target_qubit ):
        self.add_gate(['x',target_qubit ])

    def z(self, target_qubit ):
        self.rz(target_qubit , pi) 

    def y(self, target_qubit ):
        self.rz(target_qubit , pi)
        self.x(target_qubit )

    def h(self, target_qubit ):
        self.add_gate(['h', target_qubit])

    def cx(self, control, target):
        self.add_gate(['cx',control, target])

    def rx(self, target_qubit , theta):
        self.add_gate(['rx',target_qubit , theta])
    
    def ry(self, target_qubit , theta):
        self.rx(target_qubit , pi/2)
        self.h(target_qubit)
        self.rx(target_qubit , theta)
        self.h(target_qubit)
        self.rx(target_qubit , -pi/2)

    def rz(self, target_qubit , theta):
        self.h(target_qubit)
        self.rx(target_qubit, theta)
        self.h(target_qubit)

    def m(self, target_qubit , target):
        self.add_gate(['m', target_qubit, target])

    def __repr__(self):
        return str(self.circuit)
