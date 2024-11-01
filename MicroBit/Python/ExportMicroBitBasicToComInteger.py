# Source: https://github.com/EloiStree/2024_11_31_ReadHardwareToIndexInteger
# Where to execute: https://python.microbit.org/v/3/reference

from microbit import *

int_press_count =0
bool_a_pressing =False
bool_b_pressing =False
bool_touch_logo_pressing =False
bool_touch_0_pressing =False
bool_touch_1_pressing =False
bool_touch_2_pressing =False

bool_use_UART =True

if bool_use_UART:
    #https://python.microbit.org/v/3/api/microbit.uart
    uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=None, rx=None)
    

while True:

    bool_a_pressing = button_a.is_pressed()
    bool_b_pressing = button_b.is_pressed()
    bool_touch_logo_pressing = pin_logo.is_touched()
    bool_touch_0_pressing = pin0.is_touched()
    bool_touch_1_pressing = pin1.is_touched()
    bool_touch_2_pressing = pin2.is_touched()
    
    byte_light_level_255 = display.read_light_level()
    byte_light_level_9 = round(9.0-(byte_light_level_255/255.0)*9.0)
    if(byte_light_level_9>9):
        byte_light_level_9=9
    if(byte_light_level_9<0):
        byte_light_level_9=0
    # https://python.microbit.org/v/3/reference/light-level
    display.set_pixel(0,4,int(byte_light_level_9))
    
    byte_temperature_level_55 = temperature()
    byte_temperature_level_9 = round(((byte_temperature_level_55+5)/55)*9.0)
    if(byte_temperature_level_9>9):
        byte_temperature_level_9=9
    if(byte_temperature_level_9<0):
        byte_temperature_level_9=0
    # https://python.microbit.org/v/3/reference/temperature
    display.set_pixel(1,4,byte_temperature_level_9)
    
    #int_compass_360 = compass.heading()
    #byte_compass_9 =(int_compass_360/360.0)*9.0
    # https://python.microbit.org/v/3/reference/compass
    # Need a manual setup for tilt
    #display.set_pixel(2,4,int(byte_compass_9))

    int_microphone_255 = microphone.sound_level()
    byte_microphone_9 = round((int_microphone_255/255.0)*9.0)
    if(byte_microphone_9>9):
        byte_microphone_9=9
    if(byte_microphone_9<0):
        byte_microphone_9=0
    #https://python.microbit.org/v/3/reference/microphone
    display.set_pixel(3,4,byte_microphone_9)
    
    byte_button_a= 0
    if bool_a_pressing:
        byte_button_a=9

    byte_button_b= 0
    if bool_b_pressing:
        byte_button_b=9

    byte_touch_0_pressing_9 = 0
    if bool_touch_0_pressing :
        byte_touch_0_pressing_9=9
    
    byte_touch_1_pressing_9 = 0
    if bool_touch_1_pressing :
        byte_touch_1_pressing_9=9
    
    byte_touch_2_pressing_9 = 0
    if bool_touch_2_pressing :
        byte_touch_2_pressing_9=9
        
    byte_touch_logo_pressing_9 = 0
    if bool_touch_logo_pressing :
        byte_touch_logo_pressing_9=9
    
    
    display.set_pixel(0,0,byte_button_a)
    display.set_pixel(1,0,byte_button_b)
    display.set_pixel(0,1,byte_touch_0_pressing_9)
    display.set_pixel(1,1,byte_touch_1_pressing_9)
    display.set_pixel(2,1,byte_touch_2_pressing_9)
    display.set_pixel(3,1,byte_touch_logo_pressing_9)
    
    
    int_log =1700000000
    int_log+= byte_button_a 
    int_log+= byte_button_b * 10
    int_log+= byte_touch_0_pressing_9 * 100
    int_log+= byte_touch_1_pressing_9 * 1000
    int_log+= byte_touch_2_pressing_9 * 10000
    int_log+= byte_touch_logo_pressing_9 * 100000
    int_log+= byte_microphone_9 * 1000000
    int_log+= byte_light_level_9 * 10000000

    if not bool_use_UART:
        print(int_log)
        data = [int_log & 0xFF,         # Least significant byte
                (int_log >> 8) & 0xFF,  # Next byte
                (int_log >> 16) & 0xFF, # Next byte
                (int_log >> 24) & 0xFF] # Most significant byte
        print(data)
        
    if bool_use_UART:
        # Manually extract bytes in little-endian order
        data = [int_log & 0xFF,         # Least significant byte
                (int_log >> 8) & 0xFF,  # Next byte
                (int_log >> 16) & 0xFF, # Next byte
                (int_log >> 24) & 0xFF] # Most significant byte
        uart.write(bytes([0,0,0,0]))
        uart.write(bytes(data))
    sleep(100)
    #sleep(1000)