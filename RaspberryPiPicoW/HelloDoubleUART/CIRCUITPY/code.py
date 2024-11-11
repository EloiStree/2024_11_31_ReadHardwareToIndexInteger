import time
import board
import busio
import sys

## All the pin to use.
## CircuitPython uses board for pin definitions
pins_id = [
    board.GP2, board.GP3,  board.GP6,
    board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16,
    board.GP17, board.GP18, board.GP19, board.GP20, board.GP21,
    board.GP22, board.GP26, board.GP27, board.GP28
]

print("Hello World")
print(f"sys.implementation: {sys.implementation}")
print(f"sys.version: {sys.version}")

# Initialize UART interfaces in CircuitPython
uart = busio.UART(board.GP0, board.GP1, baudrate=9600, bits=8, parity=None, stop=1)
uartble = busio.UART(board.GP4, board.GP5, baudrate=9600, bits=8, parity=None, stop=1)

usePrintlog = True

def set_all_to(value):
    # Placeholder for GPIO or action setting function
    print(f"Set all to {value}")

def uartToAction(c0, c1):
    timestamp_ms = int(time.monotonic() * 1000)
    if usePrintlog:
        print("Timestamp in milliseconds:", timestamp_ms)
        print(f"C0:{c0} C1:{c1}")
    # 48 * 10  = 480
    if c1 == '1':
        if c0 == '!':
            set_all_to(True)
        elif c0 == '"':
            print("Add Code")
        elif c0 == '#':
            print("Add Code")
        elif c0 == 'A':
            print("Hello World")
        elif c0 == 'a':
            print("Bye World")
        # Add additional cases as needed

# Initialize variables for character tracking
charOne, charTwo = ' ', ' '
charOne2, charTwo2 = ' ', ' '

while True:
    # Check for data on UART0
    if uart.in_waiting > 0:
        data = uart.read(1)
        if data:
            uart.write(data)
            try:
                c = data.decode('utf-8')
                #print(c)
                #0-9
                if c.isdigit():
                    charTwo = c
                    uartToAction(charOne, charTwo)
                else:
                    charOne = c
                if usePrintlog:
                    print(f"Code Point: {str(data)} {str(charOne)} {str(charTwo)}")
            except Exception as e:
                print("An error occurred:", e)

    # Check for data on UART1
    if uartble.in_waiting > 0:
        data2 = uartble.read(1)
        
        if data2:
            uartble.write(data2)
            try:
                c2 = data2.decode('utf-8')
                #print(c2)
                if c2.isdigit():
                    charTwo2 = c2
                    uartToAction(charOne2, charTwo2)
                else:
                    charOne2 = c2
                if usePrintlog:
                    print(f"Code Point: {str(data2)} {str(charOne2)} {str(charTwo2)}")
            except Exception as e:
                print("An error occurred:", e)

    # Small delay to avoid excessive looping
    time.sleep(0.01)
