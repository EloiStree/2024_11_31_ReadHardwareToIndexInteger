import time
import board
import busio
import sys

import digitalio
import usb_hid
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

from adafruit_hid.mouse import Mouse


from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Initialize the mouse object
mouse  = Mouse(usb_hid.devices)
consumer = ConsumerControl(usb_hid.devices)

#
#
## All the pin to use.
## CircuitPython uses board for pin definitions
pins_id = [
    board.GP2, board.GP3,  board.GP6,
    board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16,
    board.GP17, board.GP18, board.GP19, board.GP20, board.GP21,
    board.GP22, board.GP26, board.GP27, board.GP28
]

print("Hello World")
print(f"sys.implementation: {sys.implementation}")
print(f"sys.version: {sys.version}")

# Initialize UART interfaces in CircuitPython
uart = busio.UART(board.GP0, board.GP1, baudrate=9600, bits=8, parity=None, stop=1)
uartble = busio.UART(board.GP4, board.GP5, baudrate=9600, bits=8, parity=None, stop=1)

# Setup MIDI
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], midi_out=usb_midi.ports[1], in_channel=0, out_channel=0)

# Initialize the keyboard
keyboard = Keyboard(usb_hid.devices)


usePrintlog = True

def set_all_to(value):
    # Placeholder for GPIO or action setting function
    print(f"Set all to {value}")

def uartToAction(c0, c1):
    timestamp_ms = int(time.monotonic() * 1000)
    if usePrintlog:
        print("Timestamp in milliseconds:", timestamp_ms)
        print(f"C0:{c0} C1:{c1}")
    # 48 * 10  = 480
    if c1 == '1':
        if c0 == '!':
            set_all_to(True)
        elif c0 == 'A':
            midi.send(NoteOn(60, 120))  # Note on with velocity 120
        elif c0 == 'a':
            midi.send(NoteOff(60, 120))  # Note off with velocity 120
            print("Add Code")
        elif c0 == 'B':
            print("Add Code")
        elif c0 == 'C':
            print("Hello World")
        elif c0 == 'D':
            print("Bye World")
        # Add additional cases as needed

# Initialize variables for character tracking
charOne, charTwo = ' ', ' '
charOne2, charTwo2 = ' ', ' '



use_learning_loop = True

keyboard.release_all()

if use_learning_loop:
    
    
    bool_experiment_midi=False
    if bool_experiment_midi:
        float_time_between_note=0.1;
        for i in range(10, 100):
            midi.send(NoteOn(i, 120))  # Note on with velocity 120
            time.sleep(float_time_between_note)
            midi.send(NoteOff(i, 120))  # Note off with velocity 120
            time.sleep(float_time_between_note)
    
    bool_experiment_keyboard=False
    if bool_experiment_keyboard:
        # Keycode : https://docs.circuitpython.org/projects/hid/en/latest/api.html
        # https://docs.circuitpython.org/projects/hid/en/latest/api.html
        for i in range(0, 10):
            
            keyboard.press(Keycode.LEFT_ARROW)
            time.sleep(0.1)
            keyboard.release(Keycode.LEFT_ARROW)
            time.sleep(0.1)
        time.sleep(10)
     
    bool_mouse_experiment=False
    if bool_mouse_experiment:
        for i in range(0, 10):
            mouse.move(x=10)
            time.sleep(0.5)
            mouse.move(x=-10)
            time.sleep(0.5)
            mouse.move(y=10)
            time.sleep(0.5)
            mouse.move(y=-10)
            time.sleep(0.5)
            mouse.move(wheel=5)
            time.sleep(0.5)
            mouse.move(wheel=-5)
            time.sleep(0.5)        
            mouse.press(Mouse.LEFT_BUTTON)
            time.sleep(0.5)
            mouse.release(Mouse.LEFT_BUTTON )
            time.sleep(0.5)        
            mouse.press(Mouse.LEFT_BUTTON)
            time.sleep(0.5)
            mouse.release(Mouse.LEFT_BUTTON )
            time.sleep(0.5)
        time.sleep(10)    
    
    bool_consumer_experiment=True
    if bool_consumer_experiment:
        for i in range(0, 10):
            # Volume up
            consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
            time.sleep(1)
            # Volume up
            consumer.send(ConsumerControlCode.VOLUME_INCREMENT)  # Increase volume
            time.sleep(1)
            # Volume down
            consumer.send(ConsumerControlCode.VOLUME_DECREMENT)  # Decrease volume
            time.sleep(1)
            # Mute
            consumer.send(ConsumerControlCode.MUTE)  # Toggle mute
            time.sleep(1)
            # Play/Pause media
            consumer.send(ConsumerControlCode.PLAY_PAUSE)  # Play/Pause media
            time.sleep(1)
            # Next track
            consumer.send(ConsumerControlCode.SCAN_NEXT_TRACK)  # Next track on media player
            time.sleep(1)
            # Previous track
            consumer.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)  # Previous track
            time.sleep(1)
            # Stop media
            consumer.send(ConsumerControlCode.STOP)  # Stop media playback
            time.sleep(1)
            try:
                # Launch the "Home" screen (on supported OS)
                consumer.send(ConsumerControlCode.HOME)  # Simulate pressing the "Home" key
            except:
                pass
            
            bool_want_use_power=False
            if bool_want_use_power:
                consumer.send(ConsumerControlCode.POWER)
                time.sleep(1)
            consumer.send(ConsumerControlCode.WWW_HOME)
            time.sleep(1)
            consumer.send(ConsumerControlCode.EMAIL)
            time.sleep(1)
            
        
    bool_experiment_gamepad=False
    if bool_experiment_gamepad:
        for i in range(0, 10):
            #keyboard.press(Keycode.LEFT_ARROW)
            #time.sleep(0.1)
            #keyboard.release(Keycode.LEFT_ARROW)
            #time.sleep(0.1)
            pass
        time.sleep(10)

use_uart_loop = True
while use_uart_loop:
    
    # Check for data on UART0
    if uart.in_waiting > 0:
        data = uart.read(1)
        if data:
            uart.write(data)
            try:
                c = data.decode('utf-8')
                #print(c)
                #0-9
                if c.isdigit():
                    charTwo = c
                    uartToAction(charOne, charTwo)
                else:
                    charOne = c
                if usePrintlog:
                    print(f"Code Point: {str(data)} {str(charOne)} {str(charTwo)}")
            except Exception as e:
                print("An error occurred:", e)

    # Check for data on UART1
    if uartble.in_waiting > 0:
        data2 = uartble.read(1)
        
        if data2:
            uartble.write(data2)
            try:
                c2 = data2.decode('utf-8')
                #print(c2)
                if c2.isdigit():
                    charTwo2 = c2
                    uartToAction(charOne2, charTwo2)
                else:
                    charOne2 = c2
                if usePrintlog:
                    print(f"Code Point: {str(data2)} {str(charOne2)} {str(charTwo2)}")
            except Exception as e:
                print("An error occurred:", e)

    # Small delay to avoid excessive looping
    time.sleep(0.01)
