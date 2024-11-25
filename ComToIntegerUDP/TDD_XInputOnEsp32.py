import socket
import threading

# Define the UDP IP address and ports
UDP_IP = "127.0.0.1"
SEND_PORT = 7046
RECEIVE_PORT = 7045

# Create a UDP socket for sending
send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create a UDP socket for receiving
receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_socket.bind((UDP_IP, RECEIVE_PORT))

# Function to send a message
def send_message(message):
    message+="\n"
    send_socket.sendto(message.encode(), (UDP_IP, SEND_PORT))
    print(f"Sent message: {message}")

# Function to receive a message
def receive_message():
    while True:
        data, addr = receive_socket.recvfrom(1024)  # buffer size is 1024 bytes
        print(f"Received message: {data.decode()} from {addr}")

# Example usage
if __name__ == "__main__":
    # Start the receiver in a new thread
    receiver_thread = threading.Thread(target=receive_message)
    receiver_thread.daemon = True
    receiver_thread.start()

    # Send a message
    send_message("Hello, UDP!")

    # Keep the main thread alive to allow the receiver thread to run
    while True:
        user_input = input("Enter message to send: ")
        send_message(user_input)
        pass