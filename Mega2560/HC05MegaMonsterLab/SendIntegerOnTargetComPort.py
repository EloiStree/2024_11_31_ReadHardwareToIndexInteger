import serial.tools.list_ports
import random
import time
import struct
import threading


# Will be the open port
integer_type= 1300000000
wait_between_send = 0.01
wait_pressing =0.01
wait_for_receive = 0.01

#string_device_id = "5583834323335131E111"
string_device_id="98DA5001A5A3"


def deal_with_received_integer(integer: int):
    print(f"Received: {integer}")





##-----------------------------------------------------------------------------------  ###
def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Device: {port.device}")
        print(f"Name: {port.name}")
        print(f"Description: {port.description}")
        print(f"HWID: {port.hwid}")
        print(f"VID: {port.vid}")
        print(f"PID: {port.pid}")
        print(f"Serial Number: {port.serial_number}")
        print(f"Location: {port.location}")
        print(f"Manufacturer: {port.manufacturer}")
        print(f"Product: {port.product}")
        print(f"Interface: {port.interface}")
        print("-" * 40)
        
def find_device_com(string_id):
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.serial_number == string_id:
            return port.device
    for port in ports:
        if  string_id in port.hwid:
            return port.device
    return None
    

def send_integer(open_port: serial.Serial,integer:int):
  
    integer_to_send = integer
    integer_to_send +=integer_type
    byte_array_integer_little = struct.pack("<I", integer_to_send)
    open_port.write(byte_array_integer_little)
    debug_byte_255 =f"{byte_array_integer_little[0]}  {byte_array_integer_little[1]}  {byte_array_integer_little[2]}  {byte_array_integer_little[3]}"
    print(f"Sent: {integer_to_send}|{byte_array_integer_little}|{debug_byte_255}")
    time.sleep(0.1)

def send_zero(open_port: serial.Serial):
    byte_array_integer_little = struct.pack("<I", 0)
    open_port.write(byte_array_integer_little)
    print(f"Sent: 0 0 0 0")
    time.sleep(0.1)
# def print_received_while_true(open_port):
#     while open_port.in_waiting > 0:
#         print(f"R{open_port.in_waiting}: {open_port.read(open_port.in_waiting).decode('utf-8')}")
#     time.sleep(0.001)

def send_integer_press(open_port, integer):
    integer_to_send = integer
    integer_to_send +=1000
    send_zero(open_port)
    send_integer(open_port,integer_to_send)
    
def send_integer_release(open_port, integer):
    integer_to_send = integer
    integer_to_send +=2000
    send_zero(open_port)
    send_integer(open_port,integer_to_send)

def send_integer_to_port( open_port, integer):
    send_integer_press(open_port,integer)
    time.sleep(wait_pressing)
    send_integer_release(open_port,integer)
    time.sleep(wait_between_send)


def send_integer_random_to_port( open_port):
    send_integer_to_port(open_port,random.randrange(22,53))


if __name__ == "__main__":
    
    list_serial_ports()
    string_com_name = find_device_com(string_device_id)
    print(string_com_name)
    baudrate= 115200
    baudrate= 9600
    open_port = serial.Serial(string_com_name, baudrate)
    # Create a thread with print_received_while_true
    # Create a thread to run the side_task function
    
    
    while(True):
        
        if False:
            for _ in range(1,4):
                send_integer_random_to_port( open_port)
        
        for i in range(22,54):
            send_integer_to_port(open_port, i)
            d=5
            
            
            b = open_port.read_all()
            if len(b)>=8 and b[0]==0 and b[1]==0 and b[2]==0 and b[3]==0:
                integer_received = struct.unpack("<I", b[4:8])[0]
                deal_with_received_integer(integer_received)
                
                
            
                
            time.sleep(0.001)
            
            
