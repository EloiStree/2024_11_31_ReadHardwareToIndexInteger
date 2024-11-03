import serial
import time

# Replace 'COM3' with your Pico's COM port
PORT = 'COM14'  
BAUDRATE = 115200  # Standard baud rate for MicroPython

def main():
    try:
        # Open serial connection
        with serial.Serial(PORT, BAUDRATE, timeout=1) as ser:
            time.sleep(2)  # Allow time for the connection to establish

            while True:
                print(".")
                # Wait for response and read it
                time.sleep(0.1)  # Small delay for the Pico to process the command
                response = ser.read(ser.in_waiting or 1)  # Read available data
                
                if response:  # Check if there's any response
                    decoded_response = response.decode('utf-8', errors='ignore')  # Decode bytes to string
                    print("Reading response... " + decoded_response)

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
