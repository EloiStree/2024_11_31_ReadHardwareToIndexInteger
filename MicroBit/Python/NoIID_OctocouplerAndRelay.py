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


# Documentation of Octocoupler 817 Module:
# - https://github.com/EloiStree/HelloInput/issues/142


from microbit import *

# WE WANT THE TIME TO BE ACCURATE
import time

## TO USE ALL PINS YOU NEED TO TURN OFF THE SCREEN
display.off()

# Hello you
print("Hello 817 Module Octocoupler (v)(;,,;)(v)")
# Buy: https://amzn.to/4eiL4pI


# List of all the pin tha can be use for write
# Check and verified
# /!\ They are usable only if you don't use Led Display /!\ 
output_pins = [
    pin0,
    pin1,
    pin2,
    pin3,
    pin4,
    pin6,
    pin7,
    pin8,   # SPECIAL but usable?
    pin9,
    pin10, 
    pin12,  # RESERVED ? ACCESSIBILITY
    pin13,  # CLOCK
    pin14,  # SPI BUS
    pin15,  # SPI BUS
    pin16,  # CHIP SELECT

    #pin5,  # BUTTON A INPUT EXTERNAL
    #pin11, # BUTTON B INPUT EXTERNAL
    #pin17, # 3V for PAD
    #pin18, # 3V for PAD
    #pin19, # I2C COM
    #pin20, # I2C COM
    #pin21, # GROUND
    #pin22, # GROUND
    ]

output_pins_inverse=[
    False,#pin0,
    False,#pin1,
    False,#pin2,
    False,#pin3,
    False,#pin4,
    False,#pin6,
    False,#pin7,
    False,#pin8,   # SPECIAL but usable?
    False,#pin9,
    False,#pin10, 
    False,#pin12,  # RESERVED ? ACCESSIBILITY
    False,#pin13,  # CLOCK
    False,#pin14,  # SPI BUS
    False,#pin15,  # SPI BUS
    False,#pin16,  # CHIP SELECT

    
]



## WANTED STATE WITH PREVIOUS STATE
int_state_previous=0
int_state =-1


#WARNING: using sleep and sleep_ms did not worked for (maybe because of round)
# So I used sleep_us

# Example of how you can send of step of the frequence to use
# Note: LEFT vs RIGHT https://www.youtube.com/watch?v=cPepfbNBcKg
def turn_on_pin(pin, inverse):
    pin.write_digital(inverse==True if 0 else 1)
    
def turn_off_pin(pin, inverse):
    pin.write_digital(inverse==True if 1 else 0)
    
def turn_on_index(index):
    if index<0:
        return
    if index>=len(output_pins):
        return
        
    turn_on_pin(output_pins[index],output_pins_inverse[index])
    
def turn_off_index(index):
    if index<0:
        return
    if index>=len(output_pins):
        return
    turn_off_pin(output_pins[index],output_pins_inverse[index])


def turn_new_on_old_off(new, old):
    turn_on_index(new)
    turn_off_index(old)
    



while True:
    sleep(0.1)
    ## CHECK FOR BUTTONS PRESSING A LEFT B RIGHT LOGO MIDDLE
    int_state_previous=int_state
    if button_a.was_pressed():
        int_state+=-1
    if button_b.was_pressed():
        int_state+=+1
    if(pin_logo.is_touched()):
        int_state=0
    if int_state<0:
        int_state=0
    # NOTE: WE COULD HAVE 16 'Relay' BUT WE HAVE ONLY 14 PIN TO WRITE
    if int_state>=len(output_pins):
        int_state=len(output_pins)-1

    # ONLY CALL A TURN IF THE VALUE CHANGED
    if int_state!=int_state_previous:
        print("Previous: "+str(int_state_previous)+" New: "+ str(int_state))
        turn_new_on_old_off(int_state, int_state_previous)
    
       
    
    
