import time
import board
import busio
import sys
import pulseio
import analogio

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


# Servo Motor SG90
import pwmio
from adafruit_motor import servo


# Initialize the mouse object
mouse  = Mouse(usb_hid.devices)
consumer = ConsumerControl(usb_hid.devices)


# RED TOUCH https://github.com/EloiStree/HelloInput/issues/148  https://amzn.to/3UDIVhn
pin_2_HW763_red  = digitalio.DigitalInOut(board.GP2)
pin_2_HW763_red.direction = digitalio.Direction.INPUT
pin_2_HW763_red.pull = digitalio.Pull.UP  
# RED TOUCH https://github.com/EloiStree/HelloInput/issues/148  https://amzn.to/3UDIVhn
pin_3_HW763_red  = digitalio.DigitalInOut(board.GP3)
pin_3_HW763_red.direction = digitalio.Direction.INPUT
pin_3_HW763_red.pull = digitalio.Pull.UP

# BLUE TOUCH https://github.com/EloiStree/HelloInput/issues/148  https://amzn.to/3UDIVhn
pin_6_HW139_blue  = digitalio.DigitalInOut(board.GP6)
pin_6_HW139_blue.direction = digitalio.Direction.INPUT
pin_6_HW139_blue.pull = digitalio.Pull.UP

# Hall Effect https://github.com/EloiStree/HelloInput/issues/44  https://amzn.to/3YVsvn4
pin_7_ky003  = digitalio.DigitalInOut(board.GP7)
pin_7_ky003.direction = digitalio.Direction.INPUT
pin_7_ky003.pull = digitalio.Pull.UP



# Joystick Pin button 
pin_22_joystick_button  = digitalio.DigitalInOut(board.GP22)
pin_22_joystick_button.direction = digitalio.Direction.INPUT
pin_22_joystick_button.pull = digitalio.Pull.UP


# Relay 
pin_18_relay_classic = digitalio.DigitalInOut(board.GP18)
pin_18_relay_classic.direction = digitalio.Direction.OUTPUT

# Octocoupler
pin_19_octocoupler = digitalio.DigitalInOut(board.GP19)
pin_19_octocoupler.direction = digitalio.Direction.OUTPUT



# Laser https://github.com/EloiStree/HelloInput/issues/172 https://amzn.to/40WhVhp
pin_21_KY008_laser= digitalio.DigitalInOut(board.GP21)
pin_21_KY008_laser.direction = digitalio.Direction.OUTPUT

# LED https://github.com/EloiStree/HelloInput/issues/265
pin_20_led330ohm= digitalio.DigitalInOut(board.GP20)
pin_20_led330ohm.direction = digitalio.Direction.OUTPUT


pin_A28_light_resistor = analogio.AnalogIn(board.GP28)
pin_A27_XJoystick = analogio.AnalogIn(board.GP27)
pin_A26_YJoystick = analogio.AnalogIn(board.GP26)



# Four Pins button 
pin_8_arcade_button = digitalio.DigitalInOut(board.GP8)
pin_8_arcade_button.direction = digitalio.Direction.INPUT
pin_8_arcade_button.pull = digitalio.Pull.UP

# Cherry Pins button 
pin_9_pression_button = digitalio.DigitalInOut(board.GP9)
pin_9_pression_button.direction = digitalio.Direction.INPUT
pin_9_pression_button.pull = digitalio.Pull.UP

# Arcade Pins button
pin_10_arcade_button = digitalio.DigitalInOut(board.GP10)
pin_10_arcade_button.direction = digitalio.Direction.INPUT
pin_10_arcade_button.pull = digitalio.Pull.UP

# Pression Pins button
pin_11_pression_button = digitalio.DigitalInOut(board.GP11)
pin_11_pression_button.direction = digitalio.Direction.INPUT
pin_11_pression_button.pull = digitalio.Pull.UP
# Pression Pins button
pin_12_button = digitalio.DigitalInOut(board.GP12)
pin_12_button.direction = digitalio.Direction.INPUT
pin_12_button.pull = digitalio.Pull.UP


# Servo Motor SG90
#pin_16_SG90_servo = pwmio.PWMOut(board.GP16, duty_cycle=0, frequency=50)
#my_servo = servo.Servo(pin_16_SG90_servo, min_pulse=500, max_pulse=2500)  # Adjust if needed for your servo

pin_16_SG90_write = digitalio.DigitalInOut(board.GP16)
pin_16_SG90_write.direction = digitalio.Direction.OUTPUT
pin_16_SG90_write.value = False



# SERVRO MOTOR SG90 START
int_20000=20000
int_left=500
int_middle=1500
int_right=2500
int_repeat =3
def turn_left_by_middle(pin):
    turn_middle(pin)
    turn_left(pin)

def turn_right_by_middle(pin):
    turn_middle(pin)
    turn_right(pin)
    
def turn_left(pin):
    for _ in range(int_repeat):
        pin.value =True
        time.sleep(int_left / 1_000_000)
        pin.value =False
        time.sleep((int_20000-int_left)/1_000_000)
def turn_middle(pin):
    for _ in range(int_repeat):
        pin.value =True
        time.sleep(int_middle / 1_000_000)
        pin.value =False
        time.sleep((int_20000-int_middle)/1_000_000)
def turn_right(pin):
    for _ in range(int_repeat):
        pin.value =True
        time.sleep(int_right / 1_000_000)
        pin.value =False
        time.sleep((int_20000-int_right)/1_000_000)
# SERVRO MOTOR SG90 END


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
    
    bool_consumer_experiment=False
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
        
        
    bool_pin_2_state= False
    bool_pin_3_state= False
    bool_pin_6_state= False
    bool_pin_7_state= False
    bool_pin_16_state= False
    bool_pin_17_state= False
    bool_pin_22_state= False
    bool_pin_8_state= False
    bool_pin_9_state= False
    bool_pin_10_state= False
    bool_pin_11_state= False
    bool_pin_12_state= False
    
    bool_switch_light_changed = True
    bool_switch_light_pins = False
    
    bool_is_joystick_left = False
    bool_is_joystick_right = False
    bool_is_joystick_up = False
    bool_is_joystick_down = False
    bool_is_joystick_left_previous = False
    bool_is_joystick_right_previous = False
    bool_is_joystick_up_previous = False
    bool_is_joystick_down_previous = False
    
    
    
    while True:
        
        if bool_pin_2_state != pin_2_HW763_red.value:
            bool_pin_2_state = pin_2_HW763_red.value
            if pin_2_HW763_red.value:
                print("Pin 2 on")
            else:
                print("Pin 2 off")
            bool_switch_light_pins= not bool_switch_light_pins
            bool_switch_light_changed=True
            
                
        if bool_pin_3_state != pin_3_HW763_red.value:
            bool_pin_3_state = pin_3_HW763_red.value
            if pin_3_HW763_red.value:
                print("Pin 3 on")
            else :
                print("Pin 3 off")
        if bool_pin_6_state != pin_6_HW139_blue.value:
            bool_pin_6_state = pin_6_HW139_blue.value
            if pin_6_HW139_blue.value:
                print("Pin 6 on")
            else :
                print("Pin 6 off")
        if bool_pin_7_state != pin_7_ky003.value:
            bool_pin_7_state = pin_7_ky003.value
            if pin_7_ky003.value:
                print("Pin 7 on")
            else :
                print("Pin 7 off")
     
        if bool_pin_8_state != pin_8_arcade_button.value:
            bool_pin_8_state = pin_8_arcade_button.value
            if pin_8_arcade_button.value:
                print("Pin 8 on")
            else :
                print("Pin 8 off")
        if bool_pin_9_state != pin_9_pression_button.value:
            bool_pin_9_state = pin_9_pression_button.value
            if pin_9_pression_button.value:
                print("Pin 9 on")
            else :
                print("Pin 9 off")
        if bool_pin_10_state != pin_10_arcade_button.value:
            bool_pin_10_state = pin_10_arcade_button.value
            if pin_10_arcade_button.value:
                print("Pin 10 on")
            else :
                print("Pin 10 off")
                
        if bool_pin_11_state != pin_11_pression_button.value:
            bool_pin_11_state = pin_11_pression_button.value
            if pin_11_pression_button.value:
                print("Pin 11 on")
            else :
                print("Pin 11 off")
                
        if bool_pin_12_state != pin_12_button.value:
            bool_pin_12_state = pin_12_button.value
            if pin_12_button.value:
                print("Pin 12 on")
            else :
                print("Pin 12 off")
      
      
        if bool_pin_22_state != pin_22_joystick_button.value:
            bool_pin_22_state = pin_22_joystick_button.value
            if pin_22_joystick_button.value:
                print("Pin 22 on")
            else :
                print("Pin 22 off")
            print(f"X: {pin_A27_XJoystick.value}, Y: {pin_A26_YJoystick.value}")
            
        if bool_switch_light_changed:
            bool_switch_light_changed=False
            pin_20_led330ohm.value = bool_switch_light_pins
            pin_21_KY008_laser.value = bool_switch_light_pins
            pin_18_relay_classic.value = bool_switch_light_pins
            pin_19_octocoupler.value = bool_switch_light_pins
            print(f"Analog A28: {pin_A28_light_resistor.value}")
            print(f"Analog A27 X: {pin_A27_XJoystick.value}")
            print(f"Analog A26 Y: {pin_A26_YJoystick.value}")
            
            
        joystick_x = pin_A27_XJoystick.value
        joystick_y = pin_A26_YJoystick.value
        if joystick_x < 1000:
            bool_is_joystick_left = True
            bool_is_joystick_right = False
        elif joystick_x > 60000:
            bool_is_joystick_left = False
            bool_is_joystick_right = True
        else:
            bool_is_joystick_left = False
            bool_is_joystick_right = False
        
        if joystick_y < 1000:
            bool_is_joystick_up = True
            bool_is_joystick_down = False
        elif joystick_y > 60000:
            bool_is_joystick_up = False
            bool_is_joystick_down = True
        else:
            bool_is_joystick_up = False
            bool_is_joystick_down = False
        
        
        
        if bool_is_joystick_left != bool_is_joystick_left_previous:
            bool_is_joystick_left_previous = bool_is_joystick_left
            if bool_is_joystick_left:
                print("Joystick Left Start")
                turn_left_by_middle(pin_16_SG90_write)
            else:
                print("Joystick Left End")
                turn_middle(pin_16_SG90_write)
                
        if bool_is_joystick_right != bool_is_joystick_right_previous:
            bool_is_joystick_right_previous = bool_is_joystick_right
            if bool_is_joystick_right:
                print("Joystick Right Start")
                turn_right_by_middle(pin_16_SG90_write)
            else:
                print("Joystick Right End")
                turn_middle(pin_16_SG90_write)
                
        if bool_is_joystick_up != bool_is_joystick_up_previous:
            bool_is_joystick_up_previous = bool_is_joystick_up
            if bool_is_joystick_up:
                print("Joystick Up Start")
            else:
                print("Joystick Up End")
        if bool_is_joystick_down != bool_is_joystick_down_previous:
            bool_is_joystick_down_previous = bool_is_joystick_down
            if bool_is_joystick_down:
                print("Joystick Down Start")
            else:
                print("Joystick Down End")
                
            
                
        time.sleep(0.01)
        #print(".")
        
        

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




