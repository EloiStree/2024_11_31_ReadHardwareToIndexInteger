# LIST IN PYTHON THE COM DEVICE INFORMATION, MIDI and HID.

import serial.tools.list_ports
import random
import time
import struct
import threading

# pip install mido
import mido


# pip uninstall hidapi
# pip install pyhidapi
# Did not worked for my device
# import hid

# pip install xinput
import xinput

# pip install  pyusb
import usb.core
import usb.util

# pip install inputs
import inputs



def list_midi_devices_in():
    for device in mido.get_input_names():
        print(device)
        ## Give More information
        try:
            print(mido.open_input(device).info())
        except:
            pass
        
def list_midi_devices_out():
    for device in mido.get_output_names():
        print(device)
        ## Give More information
        try:
            print(mido.open_output(device).info())
        except:
            pass


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
        
        
def list_hid_devices():
    # Find all USB devices
    devices = usb.core.find(find_all=True)
    for device in devices:
        try:
            # Only look at HID class devices
            if device.bDeviceClass == 0 or device.bDeviceClass == 3:
                print(f"Device ID       : {device.idVendor:04x}:{device.idProduct:04x}")
                print(f"Vendor ID       : {device.idVendor:04x}")
                print(f"Product ID      : {device.idProduct:04x}")
                # Open the HID device you are interested in (based on vendor and product ID)
                
                try:
                    print(f"Serial Number   : {usb.util.get_string(device, device.iSerialNumber)}")
                except:
                    pass
                try:
                    print(f"Manufacturer    : {usb.util.get_string(device, device.iManufacturer)}")
                except:
                    pass
                try: 
                    print(f"Product         : {usb.util.get_string(device, device.iProduct)}")
                except:
                    pass
                
                print("-" * 40)
                
        except usb.core.USBError as e:
            print(f"Could not access device information: {e}")
            
        
while True:
            
    print("############# SERIAL PORTS #############")
    list_serial_ports()

    print("############# MIDI IN #############")
    list_midi_devices_in()

    print("############# MIDI out #############")
    list_midi_devices_out()

    print("############# HID DEVICES #############")
    list_hid_devices()


    print("############# Gamepad #############")

    devices = inputs.devices.gamepads
    for device in devices:
        if hasattr(device, 'id'):
            print(f"Device ID: {device.id}")
        if hasattr(device, 'name'):
            print(f"Device Name: {device.name}")
        if hasattr(device, 'type'):
            print(f"Device Type: {device.type}")
        if hasattr(device, 'active'):
            print(f"Device Active: {device.active}")
        
        # List all buttons and axes if the attributes exist
        if hasattr(device, 'buttons'):
            print(f"Device Buttons: {device.buttons}")
        if hasattr(device, 'axes'):
            print(f"Device Axes: {device.axes}")
        
        print("------")
    
    read_console = input("Refresh ? (y/n)")
    