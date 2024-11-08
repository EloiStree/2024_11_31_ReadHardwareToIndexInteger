

// ##########  RECEIVED INTEGER AS BYTES
/// CONVERT FOUR BYTE IN LITTLE ENDIAN FORMAT TO SIGNED INTEGER 32 BITS
// byte bytes[4] = {0xC0, 0x1D, 0xFE, 0xFF};  // Little-endian encoding of -123456
// int32_t result = parseLittleEndian(bytes[0], bytes[1], bytes[2], bytes[3]);
int32_t parseLittleEndian(byte b0, byte b1, byte b2, byte b3) {
  // Combine bytes in little-endian order
  return ((int32_t)b0) | ((int32_t)b1 << 8) | ((int32_t)b2 << 16) | ((int32_t)b3 << 24);
}

// ##########  SEND INTEGER TO BYTES
// CONVERT SIGNE INTEGER INTO FOUR BYTES IN LITTLE ENDIAN
// USE: int32_t value = -123456; byte bytes[4];  intToBytes(value, bytes);
void intToBytes(int32_t value, uint8_t bytes[4]) {
  bytes[0] = value & 0xFF;         // Extract the lowest 8 bits
  bytes[1] = (value >> 8) & 0xFF;  // Shift right by 8 bits and extract the next 8 bits
  bytes[2] = (value >> 16) & 0xFF; // Shift right by 16 bits and extract the next 8 bits
  bytes[3] = (value >> 24) & 0xFF; // Shift right by 24 bits and extract the highest 8 bits
}



int digitalLenght = 11;
int analogLenght = 16;
int digitalPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
int digitalValue[] = {0,0,0,0,0,0,0,0,0,0,0,0};
int analogPins[] = {A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15};
int analogValue0To1024[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
int analogValue0To9[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};

bool useDebugPrint=false;


// Allow to remap the pin cable
int MapRealPinFromWantedPing(int wantedPin){
  switch(wantedPin){
      case 23: return 23;
      case 24: return 22;
      case 25: return 25;
      case 26: return 24;
      case 27: return 27;
      case 28: return 26;
      case 29: return 29;
      case 30: return 28;
      
      case 31: return 36;
      case 32: return 37;
      case 33: return 34;
      case 34: return 35;
      case 35: return 32;
      case 36: return 33;
      case 37: return 30;
      case 38: return 31;

      case 39: return 44;
      case 40: return 45;
      case 41: return 42;
      case 42: return 43;
      case 43: return 40;
      case 44: return 41;
      case 45: return 38;
      case 46: return 39;

      case 47: return 47;
      case 48: return 48;
      case 49: return 49;
      case 50: return 50;
      case 51: return 51;
      case 52: return 52;
      case 53: return 53;
  }
  return 23;
}


// Allow to remap the pin cable
bool MapInverseFromWantedPin(int wantedPin){
  switch(wantedPin){
      case 23: return true;
      case 24: return true;
      case 25: return true;
      case 26: return true;
      case 27: return true;
      case 28: return true;
      case 29: return true;
      case 30: return true;

      case 31: return false;
      case 32: return false;
      case 33: return false;
      case 34: return false;
      case 35: return false;
      case 36: return false;
      case 37: return false;
      case 38: return false;
      
      case 39: return false;
      case 40: return false;
      case 41: return false;
      case 42: return false;
      case 43: return false;
      case 44: return false;
      case 45: return false;
      case 46: return false;
      
      case 47: return true;
      case 48: return true;
      case 49: return true;
      case 50: return true;
      case 51: return true;
      case 52: return true;
      case 53: return true;
  }
  return 23;
}


int M(int wantedPin){return MapRealPinFromWantedPing(wantedPin);}
int V(int wantedPin, bool wantedVolt){
    bool inverse= MapInverseFromWantedPin(wantedPin);
    if (inverse){
      return wantedVolt ? LOW: HIGH;
    }
    return wantedVolt? HIGH:LOW;
}




void SetRelay(int wantedPin, int isOn){
 digitalWrite(M(wantedPin),V(wantedPin, isOn));

}

void dealWithReceivedInteger(int32_t integerReceived){
          
          if(useDebugPrint)
          Serial.println("Received Int:"+String(integerReceived));

          switch (integerReceived) {
                case 1300001023: SetRelay(23,false); break;
                case 1300002023: SetRelay(23,true); break;
                case 1300001024: SetRelay(24,false); break;
                case 1300002024: SetRelay(24,true); break;
                case 1300001025: SetRelay(25,false); break;
                case 1300002025: SetRelay(25,true); break;
                case 1300001026: SetRelay(26,false); break;
                case 1300002026: SetRelay(26,true); break;
                case 1300001027: SetRelay(27,false); break;
                case 1300002027: SetRelay(27,true); break;
                case 1300001028: SetRelay(28,false); break;
                case 1300002028: SetRelay(28,true); break;
                case 1300001029: SetRelay(29,false); break;
                case 1300002029: SetRelay(29,true); break;
                case 1300001030: SetRelay(30,false); break;
                case 1300002030: SetRelay(30,true); break;
                case 1300001031: SetRelay(31,false); break;
                case 1300002031: SetRelay(31,true); break;
                case 1300001032: SetRelay(32,false); break;
                case 1300002032: SetRelay(32,true); break;
                case 1300001033: SetRelay(33,false); break;
                case 1300002033: SetRelay(33,true); break;
                case 1300001034: SetRelay(34,false); break;
                case 1300002034: SetRelay(34,true); break;
                case 1300001035: SetRelay(35,false); break;
                case 1300002035: SetRelay(35,true); break;
                case 1300001036: SetRelay(36,false); break;
                case 1300002036: SetRelay(36,true); break;
                case 1300001037: SetRelay(37,false); break;
                case 1300002037: SetRelay(37,true); break;
                case 1300001038: SetRelay(38,false); break;
                case 1300002038: SetRelay(38,true); break;
                case 1300001039: SetRelay(39,false); break;
                case 1300002039: SetRelay(39,true); break;
                case 1300001040: SetRelay(40,false); break;
                case 1300002040: SetRelay(40,true); break;
                case 1300001041: SetRelay(41,false); break;
                case 1300002041: SetRelay(41,true); break;
                case 1300001042: SetRelay(42,false); break;
                case 1300002042: SetRelay(42,true); break;
                case 1300001043: SetRelay(43,false); break;
                case 1300002043: SetRelay(43,true); break;
                case 1300001044: SetRelay(44,false); break;
                case 1300002044: SetRelay(44,true); break;
                case 1300001045: SetRelay(45,false); break;
                case 1300002045: SetRelay(45,true); break;
                case 1300001046: SetRelay(46,false); break;
                case 1300002046: SetRelay(46,true); break;
                case 1300001047: SetRelay(47,false); break;
                case 1300002047: SetRelay(47,true); break;
                case 1300001048: SetRelay(48,false); break;
                case 1300002048: SetRelay(48,true); break;
                case 1300001049: SetRelay(49,false); break;
                case 1300002049: SetRelay(49,true); break;
                case 1300001050: SetRelay(50,false); break;
                case 1300002050: SetRelay(50,true); break;
                case 1300001051: SetRelay(51,false); break;
                case 1300002051: SetRelay(51,true); break;
                case 1300001052: SetRelay(52,false); break;
                case 1300002052: SetRelay(52,true); break;
                case 1300001053: SetRelay(53,false); break;
                case 1300002053: SetRelay(53,true); break;

                default: break; 
                }




}

//////////////////////////////////////////////////////////////////////////////////////




// SEND 
void printOnBothSerial(String text)
{
  if(useDebugPrint)
  Serial.println(text);
  if(useDebugPrint)
  Serial1.println(text);
}


bool startWithModulo2Pin=true;
bool startWithLowPin=true;
bool startWithHighPin=true;
void setup() {
//A

  Serial.begin(9600);
  Serial1.begin(9600);

  Serial.println("Setting up pins 23-55 as OUTPUT");
  for (int i = 23; i <= 55; i++) {
      pinMode(i, OUTPUT);
  }
  Serial.println("Setting all pins 23-55 to LOW");
  for (int i = 23; i <= 55; i++) {

    if(startWithModulo2Pin){
      if (i%2==0){
        SetRelay(i, true);
      }
      else{
        
        SetRelay(i, false);
      }
    }
    if(startWithLowPin){ 
        SetRelay(i, false);}
    if(startWithHighPin){    
        SetRelay(i, true);}
    
  }
  for (int i = 0; i < digitalLenght; i++) {
    pinMode(digitalPins[i], INPUT_PULLUP );
  }
   for (int i = 0; i < analogLenght; i++) {
    pinMode(analogPins[i], INPUT);
  }

}

void ReadValue(){

    for (int i = 0; i < digitalLenght; i++) {
        digitalValue[i] = digitalRead(digitalPins[i]);
    }
    for (int i = 0; i < analogLenght; i++) {
        analogValue0To1024[i] = analogRead(analogPins[i]);
        analogValue0To9[i] = map(analogValue0To1024[i], 0, 1024, 0, 9);
    }

}
void DisplayFullInformationOnPins(){

    if (useDebugPrint){
      
      if (false)
      for (int i = 0; i < digitalLenght; i++) {
          Serial.print("Digital Pin ");
          Serial.print(digitalPins[i]);
          Serial.print(" Value ");
          Serial.println(digitalValue[i]);
      }
      if (false)
      for (int i = 0; i < analogLenght; i++) {
          Serial.print("Analog Pin ");
          Serial.print(analogPins[i]);
          Serial.print(" Value 0-1024 ");
          Serial.print(analogValue0To1024[i]);
          Serial.print(" Value 0-9 ");
          Serial.println(analogValue0To9[i]);
      }
    }

}

void SendIntegerToSerial1(uint32_t value){
    uint8_t  bytes[4];
    intToBytes(value, bytes);
    for(int i=0; i<4;i++)
      Serial1.write(0);
    for(int i=0; i<4;i++)
      Serial1.write(bytes[i]);
  
}


float frameTimeMS=1;
int32_t frame;

int indexModulo4;
byte buffer[4];

void loop() {

  if(frame==0){

   
  }

  // put your main code here, to run repeatedly:
  frame++;
  if(frame%200==0)
  {

    Serial.println(""+String(frame));
    SendIntegerToSerial1(frame);
    DisplayFullInformationOnPins();
  }
  ReadValue();

  if(Serial.available())
  {
    Serial.println("Serial0:"+String(Serial.read()));
  }
  if(Serial1.available())
  {
    byte b =Serial1.read();
    //DEBUG THE BYTE RECEIVED
    //Serial.println("Serial1:"+String(b));
    buffer[indexModulo4]= b;
    indexModulo4++;
    if(indexModulo4>3){

      int32_t integer=parseLittleEndian(buffer[0], buffer[1],buffer[2],buffer[3]);
      //Serial.println("Received Int:"+String(integer));
      dealWithReceivedInteger(integer);
      indexModulo4=0;
    }
    if(buffer[0]==0 && buffer[1]==0 &&buffer[2]==0&& buffer[3]==0){
      Serial.println("Index at Zero");
    }
  }
  // DONT TOUCH
  delay(frameTimeMS);
}
