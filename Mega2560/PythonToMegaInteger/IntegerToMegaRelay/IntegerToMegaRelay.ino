#include <Arduino.h>
bool usePrintLn = true;

int byteBuffer1024Index = 0;
byte byteBuffer1024[1024];

signed long parseLittleEndian(byte b0,byte b1,byte b2,byte b3) {
  // Combine bytes in little-endian order
  return (unsigned long)b0 | ((unsigned long)b1 << 8) | ((unsigned long)b2 << 16) | ((unsigned long)b3 << 24);
}

void setup() {
    Serial.begin(9600);
    Serial.println("Serial communication started: 9600 baud");

    Serial.println("Setting up pins 23-55 as OUTPUT");
    for (int i = 23; i <= 55; i++) {
        pinMode(i, OUTPUT);
    }
    Serial.println("Setting all pins 23-55 to LOW");
    for (int i = 23; i <= 55; i++) {
        digitalWrite(i, LOW);
    }
    byteBuffer1024Index = 0;
    Serial.println("Ready to receive 4 bytes");
}

int frame = 0;

void loop() {
    if (frame == 0) {
        Serial.println("Hello Mega");
    }

    // Sleep for one second
    delay(1000);
    frame++;
    if (frame>100000)
      frame =0;
    
    Serial.println("frame: " );
    //byteBuffer1024Index=0;

    int length = Serial.available();
    for (int i = 0; i < length; i++) {
        byte b = Serial.read();
        byteBuffer1024[byteBuffer1024Index] = b;

        Serial.print("Index: ");
        Serial.print(byteBuffer1024Index);
        Serial.print(" Byte: ");
        Serial.println(b);
        byteBuffer1024Index++;
    }
    
        if(byteBuffer1024Index >= 4){
            Serial.print(byteBuffer1024Index);
            while(byteBuffer1024Index >= 3) 
            {
                 byteBuffer1024Index = -3;
                
                Serial.print(byteBuffer1024Index);
                // Copy the first 4 bytes to buffer
                byte b0= byteBuffer1024[byteBuffer1024Index];
                byte b1= byteBuffer1024[byteBuffer1024Index+1];
                byte b2= byteBuffer1024[byteBuffer1024Index+2];
                byte b3= byteBuffer1024[byteBuffer1024Index+3];

                // Reset index for the next set of bytes
                

                // Parse the little-endian value
                signed long value_little_endian = parseLittleEndian(b0,b1,b2,b3);
                Serial.print(b0);
                Serial.print(b1);
                Serial.print(b2);
                Serial.print(b3);
                Serial.println();
                Serial.println(value_little_endian);

                // Handle specific values with digitalWrite
                switch (value_little_endian) {
                case 1879048224: digitalWrite(42,LOW); break;
                case 1828716576: digitalWrite(42,HIGH); break;
                    case 1300001023: digitalWrite(23,LOW); break;
                case 1300002023: digitalWrite(23,HIGH); break;
                case 1300001024: digitalWrite(24,LOW); break;
                case 1300002024: digitalWrite(24,HIGH); break;
                case 1300001025: digitalWrite(25,LOW); break;
                case 1300002025: digitalWrite(25,HIGH); break;
                case 1300001026: digitalWrite(26,LOW); break;
                case 1300002026: digitalWrite(26,HIGH); break;
                case 1300001027: digitalWrite(27,LOW); break;
                case 1300002027: digitalWrite(27,HIGH); break;
                case 1300001028: digitalWrite(28,LOW); break;
                case 1300002028: digitalWrite(28,HIGH); break;
                case 1300001029: digitalWrite(29,LOW); break;
                case 1300002029: digitalWrite(29,HIGH); break;
                case 1300001030: digitalWrite(30,LOW); break;
                case 1300002030: digitalWrite(30,HIGH); break;
                case 1300001031: digitalWrite(31,LOW); break;
                case 1300002031: digitalWrite(31,HIGH); break;
                case 1300001032: digitalWrite(32,LOW); break;
                case 1300002032: digitalWrite(32,HIGH); break;
                case 1300001033: digitalWrite(33,LOW); break;
                case 1300002033: digitalWrite(33,HIGH); break;
                case 1300001034: digitalWrite(34,LOW); break;
                case 1300002034: digitalWrite(34,HIGH); break;
                case 1300001035: digitalWrite(35,LOW); break;
                case 1300002035: digitalWrite(35,HIGH); break;
                case 1300001036: digitalWrite(36,LOW); break;
                case 1300002036: digitalWrite(36,HIGH); break;
                case 1300001037: digitalWrite(37,LOW); break;
                case 1300002037: digitalWrite(37,HIGH); break;
                case 1300001038: digitalWrite(38,LOW); break;
                case 1300002038: digitalWrite(38,HIGH); break;
                case 1300001039: digitalWrite(39,LOW); break;
                case 1300002039: digitalWrite(39,HIGH); break;
                case 1300001040: digitalWrite(40,LOW); break;
                case 1300002040: digitalWrite(40,HIGH); break;
                case 1300001041: digitalWrite(41,LOW); break;
                case 1300002041: digitalWrite(41,HIGH); break;
                case 1300001042: digitalWrite(42,LOW); break;
                case 1300002042: digitalWrite(42,HIGH); break;
                case 1300001043: digitalWrite(43,LOW); break;
                case 1300002043: digitalWrite(43,HIGH); break;
                case 1300001044: digitalWrite(44,LOW); break;
                case 1300002044: digitalWrite(44,HIGH); break;
                case 1300001045: digitalWrite(45,LOW); break;
                case 1300002045: digitalWrite(45,HIGH); break;
                case 1300001046: digitalWrite(46,LOW); break;
                case 1300002046: digitalWrite(46,HIGH); break;
                case 1300001047: digitalWrite(47,LOW); break;
                case 1300002047: digitalWrite(47,HIGH); break;
                case 1300001048: digitalWrite(48,LOW); break;
                case 1300002048: digitalWrite(48,HIGH); break;
                case 1300001049: digitalWrite(49,LOW); break;
                case 1300002049: digitalWrite(49,HIGH); break;
                case 1300001050: digitalWrite(50,LOW); break;
                case 1300002050: digitalWrite(50,HIGH); break;
                case 1300001051: digitalWrite(51,LOW); break;
                case 1300002051: digitalWrite(51,HIGH); break;
                case 1300001052: digitalWrite(52,LOW); break;
                case 1300002052: digitalWrite(52,HIGH); break;
                case 1300001053: digitalWrite(53,LOW); break;
                case 1300002053: digitalWrite(53,HIGH); break;

                default: break; 
                }

                if (usePrintLn) {
                    // Print the reconstructed integer
                    Serial.println("Reconstructed integer: " + String(value_little_endian));
                }
            }
            byteBuffer1024Index=0;
        }
           
        
}
