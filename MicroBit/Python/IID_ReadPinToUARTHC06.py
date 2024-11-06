#/*
# * ----------------------------------------------------------------------------
# * "PIZZA LICENSE":
# * https://github.com/EloiStree wrote this file.
# * As long as you retain this notice you
# * can do whatever you want with this stuff.
# * If you think my code made you win a day of work,
# * send me a good 🍺 or a 🍕 at
# *  - https://www.patreon.com/eloiteaching
# * May the code be with you.
# * ----------------------------------------------------------------------------
# */


# Documentation of HC06 Read Input:
# Info https://github.com/EloiStree/HelloInput/issues/140
# Video: https://youtu.be/ZfXLz6KvF6k  https://github.com/EloiStree/HelloEloiTeachingVideo/issues/99
# Buttons I use for the demo:
# https://github.com/EloiStree/HelloInput/issues/148

from microbit import *
import struct

#THIS IS PRINT IN REPL CONSOLE
print("Hello UART !")

# https://makecode.microbit.org/device/pins
# /!\ /!\ /!\ /!\
# YOU CANT USE HARDWARE THAT SEND VOLT AS INPUT AS START STATE ON THE PIN 5 AND 11
# THE MICRO BIT 5 11 is for A AND B.
# IF BOTH ARE TRUE IT TRIGGER THE BLUETOOTH MODE
# AS YOUR CODE COME AFTER THE BOOT OF THE DEVICE 
# YOU CANT FIX IT WITHOUT FLASHING A CUSTOM FIRMWARE VERSION
# YOU CAN STILL USE THEM AS CLASSIC BUTTON
# /!\ /!\ /!\ /!\



display.off()

# PIN 2 IS TOUCH CAPACITIVE AND IT IS IMPORTANT FOR ME
pin2.set_touch_mode(pin2.CAPACITIVE)
# PIN LOG IS TOUCH AND "External"
pin_logo.set_touch_mode(pin_logo.CAPACITIVE)
pin3.set_pull(pin3.PULL_UP)
pin4.set_pull(pin4.PULL_UP)
pin5.set_pull(pin5.PULL_UP)
pin11.set_pull(pin11.PULL_UP)
pin12.set_pull(pin12.PULL_UP)
pin16.set_pull(pin16.PULL_UP)


# AS SOON AS UART INIT IS CALL print(...) IS EQUALS TO uart.write(...)
# Set up UART with default baud rate (115200) on pins P1 (TX) and P2 (RX)
# VERIFIED ON V2.21
uart.init(baudrate=9600, tx=pin1, rx=pin0)
sleep(500)



## THIS IS PRINT ON THE RECEIVER
print("HELLO YOU !")
print("I AM MICRO:BIT V2.21")



# WHAT CAN BE READ AS PIN ANALOGIC ?
analog_pin=[
    #pin0, # USE RX FOR HC06
    #pin1, # USE TX FOR HC06
    pin2, # USABLE AS TOUCH
    pin10,   # USABLE AS TOUCH
]
# WHAT CAN BE READ AS PIN DIGITAL
digital_pin=[
    pin3,#P3	No	Yes	Shared with LED matrix
    pin4,#P4	No	Yes	Shared with LED matrix
    pin5,#P5	No	Yes	Connected to A button
    pin11,#P11	No	Yes	Connected to B button
    pin12,#P12	No	Yes	Free digital input
    pin16,#P16	No	Yes	Free digital input
]



# SEND 0000 to allows the com to know that Integer or Index Integer follow
start_with_0000_bytes =True
# SEND SOME PRINT DEBUG TO KNOW WHAT HAPPENING
bool_send_as_text=True

# SEND INTEGER AS 4 BYTES LITTLE ENDIAN
bool_send_as_integer_4bytes=True

# SEND PLAYER INDEX WITH INTEGER AS 8 BYTES IN LITTLE ENDIAN
bool_send_as_indexInteger_8bytes=True

# REPRESENT THE USER/PLAYER ID YOU WANT HIM TO HAVE
user_index=-404



int_to_send_current=0
int_to_send_previous=0


# LET'S START WORKING
while True:

    int_to_send_previous = int_to_send_current
    # THE TWO FIRST BYTE IS THE TYPE OF DATA
    int_value:int =1500000000

    # COMPRESS THE VALUE AS DIGIT IN THE INTEGER
    byte_09_pin10 = (pin10.read_analog()/1023.0)*9.0
    bool_01_logo= pin_logo.is_touched()
    bool_01_pin2= pin2.is_touched()
    inverse_value =1 # 0 = non inverse  1 = inverse
    bool_01_pin3= pin3.read_digital()==inverse_value if 1 else 0 
    inverse_value =1
    bool_01_pin4= pin4.read_digital()==inverse_value if 1 else 0
    inverse_value =1
    bool_01_pin5= pin5.read_digital()==inverse_value if 1 else 0
    inverse_value =1
    bool_01_pin11= pin11.read_digital()==inverse_value if 1 else 0
    inverse_value =1
    bool_01_pin12= pin12.read_digital()==inverse_value if 1 else 0
    inverse_value =1
    bool_01_pin16= pin16.read_digital()==inverse_value if 1 else 0


    # 11111111 Byte  0-255
    # 1 0 bit

    #AA = Button A Press
    #AB = Button A Release
    #AC = Button B press
    #AD = Button B release
    #58*58 =2500+ Variante.


    #1899887766 18 gamepad 99 jhl 88 jvl  77 jhr 66 jvr
    #1364874546 1111111 1 11111111 11111111 1111111

    # MIDI TYPEDATA DATA 1   DATA2
    # MIDI TYPE     NOTE     VELOCITY
    # MIDI NOTE ON  56       127 
    # MIDI NOTE OFF 56       127 
    # MIDI 11111111 11111111 11111111

    int_value+= int(round(byte_09_pin10)) #150000000N
    int_value+= bool_01_pin2  *10         #15000000N0
    int_value+= bool_01_pin3  *100        #1500000N00
    int_value+= bool_01_pin4  *1000       #150000N000
    int_value+= bool_01_pin5  *10000      #15000N0000
    int_value+= bool_01_pin11 *100000     #1500N00000
    int_value+= bool_01_pin12 *1000000    #150N000000
    int_value+= bool_01_pin16 *10000000   #15N0000000
    if bool_01_logo==1:
        int_value+= bool_01_logo * 10


    int_to_send_current = int_value

    if int_to_send_current != int_to_send_previous:
        
        if bool_send_as_text:
           #print(("\nAnalog:"+str(pin10.read_analog())))
           print( "\nInt:" + str(int_value) )
        if bool_send_as_integer_4bytes: 
           if start_with_0000_bytes:
               uart.write(b'0000')
           bytes_little_endian = struct.pack("<I", int_value)
           uart.write(bytes_little_endian)
        if bool_send_as_indexInteger_8bytes:
            if start_with_0000_bytes:
               uart.write(b'0000')
            bytes_little_endian = struct.pack("<II",user_index, int_value)
            uart.write(bytes_little_endian)
           

    
    if  uart.any():
        incoming = uart.readline()  #Wait for \n  or no bytes anymore
        ## ADD YOUR OWN CODE
        ## DO SOME ACTION
        print("In|"+(str(incoming)))
        #uart.write("Ok do ki")
    sleep(5)
