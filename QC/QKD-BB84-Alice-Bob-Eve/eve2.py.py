
# Eve - run 2nd

import socket
import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Define the backend for the simulation
backend = Aer.get_backend('aer_simulator')

# Define Security Variables
eve = 0
total = 0

def generate_key(size):
    return [random.randint(0, 1) for _ in range(size)]

def encode_key(key):
    circuit = QuantumCircuit(len(key), len(key))
    for i, bit in enumerate(key):
        if bit == 1:
            circuit.x(i)
    return circuit

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

# Modified qkd_protocol function
def qkd_protocol(alice_measurement, alice_basis, bob_measurement):
    # In a proper QKD, Alice would announce her basis and Bob would announce his basis.
    # If bases match, they would expect their bits to be the same.
    # Here, `bob_measurement` is being used as a proxy for Bob's announced basis for comparison.
    # Ideally, `bob_basis` (Bob's chosen measurement bases) should be passed here separately.

    shared_key = []
    # Alice and Bob discard the bits where their bases don't match
    for i in range(len(alice_measurement)):
        if alice_basis[i] == bob_measurement[i]: # Compare Alice's basis with Bob's measurement (proxy for Bob's basis)
            shared_key.append(alice_measurement[i]) # Keep Alice's bit if bases match (ideally Alice's bit == Bob's bit)

    return shared_key

def eve_intercept(alice_key, eve_basis):
    eve_measurement = measure_circuit(encode_key(alice_key), eve_basis)

    # Eve guesses the original key
    eve_guess = []
    for i in range(len(alice_key)):
        if eve_basis[i] == 0:
            eve_guess.append(eve_measurement[i])
        else:
            eve_guess.append(1 - eve_measurement[i])
    return eve_guess

def calculate_success_rate(total_attempts, successful_attempts):
    if total_attempts == 0:
        return 0
    return (successful_attempts / total_attempts) * 100

def main():
    global eve, total

    # Setup server socket to receive connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Added to allow port reuse
    server_socket.bind(('localhost', 65434))  # Port for Eve
    server_socket.listen(1)
    print("Eve is listening for connections...")

    try:
        # Accept Alice's connection
        alice_conn, alice_addr = server_socket.accept()
        print(f"Connected to Alice from {alice_addr}")

        # Connect to Bob
        bob_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bob_socket.connect(('localhost', 65435))  # Port for Bob
        print("Connected to Bob.")

        try:
            while True:
                # Receive data from Alice
                alice_data = alice_conn.recv(1024).decode()
                if not alice_data:
                    raise ValueError("No data received from Alice.")

                print(f"Eve received Alice's data: {alice_data}")

                # Forward Alice's data to Bob
                bob_socket.sendall(alice_data.encode())
                print(f"Data sent to Bob: {alice_data}")

                # Receive Bob's response
                bob_response = bob_socket.recv(1024).decode()
                if not bob_response:
                    raise ValueError("No response received from Bob.")

                print(f"Eve received Bob's response: {bob_response}")

                # Send Bob's response back to Alice
                alice_conn.sendall(bob_response.encode())
                print(f"Response sent to Alice: {bob_response}")

                # Track success rate
                alice_key = list(map(int, alice_data.split('|')[0].strip('[]').split(',')))
                alice_basis = list(map(int, alice_data.split('|')[1].strip('[]').split(',')))
                bob_measurement = list(map(int, bob_response.strip('[]').split(',')))
                shared_key = qkd_protocol(alice_key, alice_basis, bob_measurement)

                # Eve's attempt to intercept (simplified for demonstration)
                # In a real scenario, Eve would measure the qubits she intercepts.
                # Here, we simulate Eve trying to guess the shared key based on what she 'sees' being exchanged.
                # A better simulation would involve Eve's own measurement process affecting the quantum states.

                eve_guess = eve_intercept(alice_key, bob_measurement) # Using bob_measurement as a proxy for Eve's basis choice for comparison

                if shared_key == eve_guess:
                    eve += 1

                total += 1
                success_rate = calculate_success_rate(total, eve)
                print(f"Iteration: {total}, Eve's success rate: {success_rate:.5f}%")

        except ValueError as ve:
            print(f"Value error: {ve}")

        finally:
            alice_conn.close()
            bob_socket.close()

    except Exception as e:
        print(f"Server error: {e}")

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
