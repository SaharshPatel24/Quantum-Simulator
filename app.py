# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from python_scripts.quantum_simulation import simulate_quantum_circuit

app = Flask(__name__)

CORS(app)

@app.route('/api/configure-simulation', methods=['POST'])
def configure_simulation():
    data = request.get_json()
    qiskit_config = data.get('qiskit_config', {})

    try:
        simulation_results = simulate_quantum_circuit(qiskit_config)
        return jsonify(simulation_results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
