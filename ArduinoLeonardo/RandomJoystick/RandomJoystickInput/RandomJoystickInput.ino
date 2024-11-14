#include <Joystick.h>
#include <Arduino.h>

// Create a Joystick object with 24 buttons and 2 analog triggers
Joystick_ Joystick(JOYSTICK_DEFAULT_REPORT_ID, JOYSTICK_TYPE_GAMEPAD,
                   24,  // Number of buttons
                   0,   // Number of hat switches
                   true, true, false,   // X, Y, Z for joystick 1
                   true, true, false,   // X, Y, Z for joystick 2
                   false, false,        // Rudder, Throttle
                   false, false, false  // Accelerator, Brake, Steering
);

void setup() {
  // Initialize the joystick
  Joystick.begin();
  randomSeed(analogRead(0));  // Seed random number generator with noise from analog pin
}

void loop() {
  // Generate random values for joystick 1 (X and Y axes)
  int joystick1X = random(-127, 128);  // Random value between -127 and 127
  int joystick1Y = random(-127, 128);  // Random value between -127 and 127
  Joystick.setXAxis(joystick1X);
  Joystick.setYAxis(joystick1Y);

  // Generate random values for joystick 2 (X and Y axes)
  int joystick2X = random(-127, 128);  // Random value between -127 and 127
  int joystick2Y = random(-127, 128);  // Random value between -127 and 127
  Joystick.setRxAxis(joystick2X);
  Joystick.setRyAxis(joystick2Y);

  // Generate random values for two analog triggers (0 to 255 range)
  int trigger1 = random(0, 256);  // Random value between 0 and 255
  int trigger2 = random(0, 256);  // Random value between 0 and 255
  Joystick.setZAxis(trigger1);
  Joystick.setRzAxis(trigger2);

  // Set random states for 24 buttons
  for (int i = 0; i < 24; i++) {
    bool buttonState = random(0, 2);  // Randomly 0 (not pressed) or 1 (pressed)
    Joystick.setButton(i, buttonState);
  }

  delay(100);  // Update every 100 ms
}
