import socket
import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from time import sleep

backend = Aer.get_backend('aer_simulator')

def generate_key(size):
    return [random.randint(0, 1) for _ in range(size)]

def measure_circuit(circuit, basis):
    for i in range(len(basis)):
        if basis[i] == 1:
            circuit.h(i)
    circuit.measure(range(len(basis)), range(len(basis)))
    t_circuit = transpile(circuit, backend)
    job = backend.run(t_circuit, shots=1)
    result = job.result()
    counts = result.get_counts(circuit)
    outcome = max(counts, key=counts.get)
    measurement = [int(outcome[i]) for i in range(len(basis))]
    return measurement

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65434))  # Connect to Eve
    print("Connected to Eve.")

    try:
        while True:
            # Generate Alice's random key and basis
            alice_key = generate_key(12)  # Example size of 12
            alice_basis = generate_key(len(alice_key))
            alice_circuit = QuantumCircuit(len(alice_key), len(alice_key))
            
            # Prepare Alice's state
            for i, bit in enumerate(alice_key):
                if bit == 1:
                    alice_circuit.x(i)
                if alice_basis[i] == 1:
                    alice_circuit.h(i)
            
            alice_measurement = measure_circuit(alice_circuit, alice_basis)
            print(f"Alice's measurement: {alice_measurement}")

            # Send Alice's data to Eve
            message = f"{alice_measurement}|{alice_basis}"
            client_socket.sendall(message.encode())
            print("Alice's data sent to Eve.")

            # Receive the shared key from Eve
            try:
                eve_data = client_socket.recv(1024).decode()
                if not eve_data:
                    raise ValueError("No data received from Eve.")
                print(f"Received shared key from Eve: {eve_data}")

            except ValueError as ve:
                print(f"Value error: {ve}")
                break  # Exit loop if no data received

            #sleep(5)  # Sleep for a bit before the next iteration

    except (socket.error, ValueError) as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()

