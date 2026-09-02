from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Initialize the Circuit
# We need 1 Qubit (to generate the randomness) and 1 Classical Bit (to store the result)
circuit = QuantumCircuit(1, 1)

# 2. Put the Qubit into Superposition
# The 'Hadamard' (H) gate puts the qubit into an exact 50/50 state of being 0 and 1
circuit.h(0)

# 3. Measure the Qubit
# This collapses the superposition down to a single classical result, storing it in bit 0
circuit.measure(0, 0)

# Print a visual representation of our circuit in the terminal
print("Our Quantum Circuit:")
print(circuit.draw())

# 4. Run the Circuit on a Local Simulator
simulator = AerSimulator()

# We "shoot" the circuit 100 times to see the statistical breakdown
job = simulator.run(circuit, shots=100)
result = job.result()

# 5. Get the Results
counts = result.get_counts(circuit)
print("\nResults of 100 quantum coin flips:", counts)

# (Optional) Display a bar chart of the results
plot_histogram(counts)
plt.show()