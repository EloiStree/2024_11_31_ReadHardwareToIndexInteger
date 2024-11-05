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


# Documentation of SG90 Servo Motor:
# Info https://github.com/EloiStree/HelloInput/issues/139
# Video: https://github.com/EloiStree/HelloEloiTeachingVideo/issues/96


from microbit import *

# WE WANT THE TIME TO BE ACCURATE
import time

## TO USE ALL PINS YOU NEED TO TURN OFF THE SCREEN
display.off()

# Hello you
print("Hello SG90 (v)(;,,;)(v)")

# SG90 Work on frequence of 20 ms
int_20000=20000

# 1000ms is suppose to be left
#But I needed to tweak it for mine
int_left=500

#1500ms is middle
int_middle=1500

#2000ms is suppose to be right
#But I needed to tweak it for mine
int_right=2500

# List of all the pin tha can be use for Servo Motor SG90
# Check and verified
# /!\ They are usable only if you don't use Led Display /!\ 
# DISABLE THE ONE YOU DONT USE IF YOU WANT TO WIN N*STEP*20ms
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




#WARNING: using sleep and sleep_ms did not worked for (maybe because of round)
# So I used sleep_us

# Example of how you can send of step of the frequence to use
# Note: LEFT vs RIGHT https://www.youtube.com/watch?v=cPepfbNBcKg
def turn_left(pin):
    pin.write_digital(1)
    time.sleep_us(int_left)
    pin.write_digital(0)
    time.sleep_us(int_20000-int_left)

def turn_middle(pin):
    pin.write_digital(1)
    time.sleep_us(int_middle)
    pin.write_digital(0)
    time.sleep_us(int_20000-int_middle)

def turn_right(pin):
    pin.write_digital(1)
    time.sleep_us(int_right)
    pin.write_digital(0)
    time.sleep_us(int_20000-int_right)



# SUPPOSED TO WORK.
# But write_digital  take some random ms out of the equation that break the frequence
"""
def turn_all_delay(ms):
    for pin in output_pins:
        pin.write_digital(1)
    time.sleep_us(ms)
    for pin in output_pins:
        pin.write_digital(0)
    time.sleep_us(int_20000-ms)

def turn_all_mid():
    turn_all_delay(int_middle)
    
def turn_all_left():
    turn_all_delay(int_left)
    
def turn_all_right():
    turn_all_delay(int_right)
"""       

## NUMBER OF STEP YOU WANT TO USE IN THE FREQUENCE
int_step=3


## WANTED STATE WITH PREVIOUS STATE
int_state_previous=0
int_state =-1

## SET MIDDLE AS DEFAULT
if True:
    print("Middle Start")
    for pin in output_pins:
        for i in range(int_step):
            turn_middle(pin)


while True:

    ## CHECK FOR BUTTONS PRESSING A LEFT B RIGHT LOGO MIDDLE
    int_state_previous=int_state
    if button_a.was_pressed():
        int_state+=-2
    if button_b.was_pressed():
        int_state+=2
    if(pin_logo.is_touched()):
        int_state=0
    if int_state<-1:
        int_state=-1
    if int_state>1:
        int_state=1

    # ONLY CALL A TURN IF THE VALUE CHANGED
    if int_state!=int_state_previous:

        # GO TO MIDDLE BEFORE TURNING SEEM TO WORK WELL
        print("Turn Middle")
        for pin in output_pins:
            for i in range(int_step):
                turn_middle(pin)

        # MOVE ALL TO LEFT ONE AFTER AN OTHER
        if int_state==-1:
            print("Turn Left")
            for pin in output_pins:
                for i in range(int_step):
                    turn_left(pin)

        
        # MOVE ALL TO RIGHT ONE AFTER AN OTHER
        if int_state==1:
            print("Turn right")
            for pin in output_pins:
                for i in range(int_step):
                    turn_right(pin)
    
       
    
    
