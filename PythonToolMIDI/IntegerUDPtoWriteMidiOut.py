
import socket
import struct
import mido
from mido import Message

# Set up the UDP socket
UDP_IP = "127.0.0.1" 
UDP_IP = "0.0.0.0"  # Localhost (use 0.0.0.0 to listen on all interfaces)
UDP_PORT = 3600      # Port to listen on
UDP_PORT = 3615      # Port to listen on
int_type = 1600000000

midi_out_name = 'Microsoft GS Wavetable Synth'
midi_out_name = 'MPK mini play'





selected_port = ""
for port_name in mido.get_output_names():
    print(port_name)
    if midi_out_name in port_name:
        selected_port = port_name
        

if not selected_port:
    print(f"Could not find MIDI output port with name '{midi_out_name}'.")
    exit(1)

print(f"Selected MIDI output port: {selected_port}")
# Initialize MIDI output
midi_out = mido.open_output(selected_port)



# Set up the UDP listener
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}...")

try:
    while True:
        # Receive data from the socket
        data, addr = sock.recvfrom(16)  # Expecting 4 bytes (integer size)
        int_value=0
        if len(data) == 4:
            int_value = int.from_bytes(data, byteorder='little')
        elif len(data) == 8:
            int_value = int.from_bytes(data[4:], byteorder='little')
        elif len(data) == 16:
            int_value = int.from_bytes(data[4:], byteorder='little')
        else:
            continue

        print(f"Received integer value: {int_value}")
        int_value %=100000000
        print(f"Received integer modulo value: {int_value}")        
        new_int_as_bytes = int.to_bytes(int_value, 4, byteorder='little')
        print(f"Integer as bytes: {new_int_as_bytes[0]} {new_int_as_bytes[1]} {new_int_as_bytes[2]} {new_int_as_bytes[3]}")
        midi_message = new_int_as_bytes[0:3]
        print(f"Sending MIDI message: {new_int_as_bytes[0]} {new_int_as_bytes[1]} {new_int_as_bytes[2]}")
        # descript what is the midi_message with mido
        message_debug = mido.Message.from_bytes(midi_message)
        print(f"Message description: {message_debug}")
        midi_out.send(Message.from_bytes(midi_message))

except KeyboardInterrupt:
    print("UDP listener stopped.")
finally:
    sock.close()
    midi_out.close()
