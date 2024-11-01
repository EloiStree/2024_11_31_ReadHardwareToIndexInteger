
"""
This script show how you can read some midi in and sent it as integer by UDP to an II application.
II stand for Index Integer. It is used in my application and game to have shared server with the community.
Index is a user and value is the action or log to use.
https://github.com/EloiStree/IID

"""
# pip install mido python-rtmidi

import mido
import socket
import time

# Constants
int_type = 1600000000
midi_to_use = 'loopMIDI Port'

# Network settings
ipv4 = "127.0.0.1"
port = 3615

# Debugging
use_print = True
use_print = False

bool_use_index = True
use_index = 456




def send_integer_to_udp(value: int):
    
    if bool_use_index:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            byte_index = use_index.to_bytes(4, byteorder='little')
            byte_value = value.to_bytes(4, byteorder='little')
            s.sendto(byte_index + byte_value, (ipv4, port))
            if use_print:
                print(f"Sent {value} to {ipv4}:{port}")
            s.close()
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(value.to_bytes(4, byteorder='little'), (ipv4, port))
            if use_print:
                print(f"Sent {value} to {ipv4}:{port}")
            s.close()

# Find the MIDI port
selected_port = ""
for port_name in mido.get_input_names():
    print(port_name)
    if midi_to_use in port_name:
        selected_port = port_name
        break

if selected_port:
    try:
        # Open MIDI input port
        with mido.open_input(selected_port) as inport:
            print(f"Listening for MIDI messages on {selected_port}...")
            for msg in inport:
                byte_data = msg.bytes()
                integer_value = int.from_bytes(byte_data, byteorder='little')
                integer_value += int_type
                if use_print:
                    print(f"Bytes: {byte_data} -> Int: {integer_value}")
                
                # Send the integer value to UDP
                send_integer_to_udp(integer_value)
                
    except KeyboardInterrupt:
        print("Stopped listening for MIDI messages.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Closed MIDI port.")
else:
    print(f"Error: MIDI port '{midi_to_use}' not found.")


time.sleep(10)