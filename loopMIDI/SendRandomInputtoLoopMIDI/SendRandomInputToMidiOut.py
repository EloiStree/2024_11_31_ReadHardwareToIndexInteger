"""

This script show how you can send some note with velocity to a midi port in with python    
The code is by default set to loopMIDI port.
https://www.tobias-erichsen.de/software/loopmidi.html
    
"""

# pip install mido python-rtmidi
import mido
import time
import random
# Define the MIDI port name (make sure it matches your loopMIDI port name)
port_name = "loopMIDI Port"  # Replace with the exact name of your loopMIDI port

# Define the MIDI note parameters
note_number = 60+random.randrange(-20,20)  # MIDI note number for Middle C
velocity = 64+random.randrange(-20,20)     # Note velocity
delay = 1.0 +random.random()*0.5      # Delay in seconds

try:
    # List all available MIDI output ports
    print("Available MIDI output ports:")

    selected_port= ""
    list_of_port = mido.get_output_names()
    for port in list_of_port:
        print(port)
        if port_name in port:
            selected_port= port
    
        
    if len(selected_port) == 0:
        print(f"Could not find the MIDI port '{port_name}'.")
        exit()
    else:
        print(f"Found the MIDI port '{selected_port}'")
        
    with mido.open_output(selected_port) as port:
        print(f"Sending MIDI notes to '{port_name}' every {delay} seconds.")
        
        while True:
            # Send a Note On message
            note_on = mido.Message('note_on', note=note_number, velocity=velocity)
            port.send(note_on)
            print(f"Sent Note On: {note_number}")

            # Delay before sending Note Off
            time.sleep(0.1)

            # Send a Note Off message
            note_off = mido.Message('note_off', note=note_number, velocity=velocity)
            port.send(note_off)
            print(f"Sent Note Off: {note_number}")

            # Wait for the specified delay before the next loop
            time.sleep(delay)

except KeyboardInterrupt:
    print("\nScript terminated by user.")
except IOError:
    print(f"Could not find the MIDI port '{port_name}'. Check if loopMIDI is running and the port name is correct.")
