#include <Joystick.h>

// Create Joystick instance
Joystick_ Joystick(JOYSTICK_DEFAULT_REPORT_ID, 
                   JOYSTICK_TYPE_MULTI_AXIS, 
                   5, 0,  // 5 buttons, 0 hat switches
                   true,  // xAxis
                   true,  // yAxis
                   true,  // zAxis
                   true,  // RxAxis
                   true,  // RyAxis
                   true,  // RzAxis
                   true,  // Rudder
                   true,  // Throttle
                   true,  // Accelerator
                   true,  // Brake
                   true);  // Steering                              

// Define button pin numbers
const int buttonPins[] = {2, 4, 7, 8, 12};
const int numButtons = sizeof(buttonPins) / sizeof(buttonPins[0]);

// Analog input pins for the Arduino Leonardo
const int analogPins[] = {A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10};
const int numAnalogs = sizeof(analogPins) / sizeof(analogPins[0]);

void setup() {
  // Initialize each button pin as an input with pull-up resistor
  for (int i = 0; i < numButtons; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }

  // Start Joystick
  Joystick.begin();
}

void loop() {
  // Read button states and set them in the Joystick library
  for (int i = 0; i < numButtons; i++) {
    // Read the button state (invert because INPUT_PULLUP)
    int buttonState = !digitalRead(buttonPins[i]);
    Joystick.setButton(i, buttonState);
  }

  // Read analog values and assign them to joystick axes
  Joystick.setXAxis(analogRead(analogPins[0]));
  Joystick.setYAxis(analogRead(analogPins[1]));
  Joystick.setZAxis(analogRead(analogPins[2]));
  Joystick.setRxAxis(analogRead(analogPins[3]));
  Joystick.setRyAxis(analogRead(analogPins[4]));
  Joystick.setRzAxis(analogRead(analogPins[5]));
  Joystick.setRudder(analogRead(analogPins[6]));
  Joystick.setThrottle(analogRead(analogPins[7]));
  Joystick.setAccelerator(analogRead(analogPins[8]));
  Joystick.setBrake(analogRead(analogPins[9]));
  Joystick.setSteering(analogRead(analogPins[10]));

  // Small delay to ensure the loop doesn't run too quickly
  delay(10);
}
