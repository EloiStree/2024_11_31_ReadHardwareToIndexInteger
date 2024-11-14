If you are doing some IOT in the context of Hello Input.

It is most probably to trigger motor, step motor or servo motor.


To do that you need two circuit.
- The microcontroller one
- The 5-12 volt of the motors

So let's explore how to use this kind of tools.
Note that for 15-30 € You can buy a Micro:bit + H05 + Keyestudio board. And it is all you would need ^^.  
See:  NoIID_WriteToSG90ServoMotor.py   

Here we explore the Raspberry Pi Pico W on Circuit Python.

So let's start


--------------------

🚧 Need to be construct later. 🚧

-------------------


#SG90 

Info: https://github.com/EloiStree/HelloInput/issues/139 

```

 Servo Motor SG90 https://github.com/EloiStree/HelloInput/issues/139 
 Not usable on Raspberry Pi Pico without Motor Driver https://amzn.to/40vOYs6
import pwmio
from adafruit_motor import servo




# Servo Motor SG90
#pin_16_SG90_servo = pwmio.PWMOut(board.GP16, duty_cycle=0, frequency=50)
#my_servo = servo.Servo(pin_16_SG90_servo, min_pulse=500, max_pulse=2500)  # Adjust if needed for your servo

 SG 90
 SERVRO MOTOR SG90 START
 NEED SERVO MOTOR SG90
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
 SERVRO MOTOR SG90 END


```