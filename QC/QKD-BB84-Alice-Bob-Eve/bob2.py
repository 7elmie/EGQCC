import socket
import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

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
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65435))  # Port for Bob
    server_socket.listen(1)
    print("Bob is listening for connections...")

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Connected to Eve from {addr}")

            try:
                while True:
                    # Receive data from Eve
                    data = conn.recv(1024).decode()
                    if not data:
                        raise ValueError("No data received from Eve.")

                    alice_measurement, alice_basis = data.split('|')
                    alice_measurement = list(map(int, alice_measurement.strip('[]').split(',')))
                    alice_basis = list(map(int, alice_basis.strip('[]').split(',')))
                    
                    print(f"Bob received Alice's data: {alice_measurement}, {alice_basis}")

                    # Simulate Bob's measurement
                    bob_basis = generate_key(len(alice_measurement))
                    bob_circuit = QuantumCircuit(len(alice_measurement), len(alice_measurement))
                    for i, bit in enumerate(alice_measurement):
                        if bit == 1:
                            bob_circuit.x(i)
                        if bob_basis[i] == 1:
                            bob_circuit.h(i)
                    
                    bob_measurement = measure_circuit(bob_circuit, bob_basis)
                    print(f"Bob's measurement: {bob_measurement}")

                    # Send Bob's measurement to Eve
                    message = str(bob_measurement)
                    conn.sendall(message.encode())
                    print(f"Message sent to Eve: {message}")

            except ValueError as ve:
                print(f"Value error: {ve}")

            finally:
                conn.close()

    except Exception as e:
        print(f"Server error: {e}")

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

