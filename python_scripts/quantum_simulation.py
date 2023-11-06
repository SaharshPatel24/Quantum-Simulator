# quantum_simulation.py
from qiskit import QuantumCircuit, transpile, execute, Aer
import json

def simulate_quantum_circuit(qiskit_config):
    qasm_code = qiskit_config.get('qasm', '')
    qiskit_circuit = QuantumCircuit.from_qasm_str(qasm_code)
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qiskit_circuit, simulator)
    job = execute(compiled_circuit, simulator)
    qiskit_result = job.result().get_counts(qiskit_circuit)

    return {
        "qiskit_results": qiskit_result
    }
