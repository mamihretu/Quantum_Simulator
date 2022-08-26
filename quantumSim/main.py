from quantumSimulator  import QuantumSimulator
from quantumCircuit import QuantumCircuit
from math import cos,sin,pi



if __name__ == "__main__":
    print('Quantum Simulator for Developers project')
    qc = QuantumCircuit(5)
    qc.h(0)
    qc.x(1)
    qc.rx(2,pi)
    qc.z(0)
    qc.h(1)
    qc.cx(0,1)
    qc.cx(1,0)
    qc.m(0,0)

    print('\ncircuit:') 
    print(qc)
    
    print('\nsimulate and show state_vector:') 
    quantumSimulator =  QuantumSimulator(qc)
    result = quantumSimulator.run()
    print(result)

    print('\nsimulate 1024 shots and show the counts:') 
    result = quantumSimulator.run(1024, "counts")
    print(result)